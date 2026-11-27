"""Automated QC on the *rendered MP4* (final_render_checklist + motion/scene checks).

Measures what can be measured objectively; visual judgement items are filled in by the
reviewer from the extracted frames (A/M/Z per shot + +/-3 frames around every cut).
"""
from __future__ import annotations

import json
import os
import subprocess

import numpy as np

from .core import FPS


def probe(mp4):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", mp4],
                       capture_output=True, text=True)
    j = json.loads(r.stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    a = next((s for s in j["streams"] if s["codec_type"] == "audio"), None)
    return {
        "video": f"{v['codec_name']} {v.get('profile')} {v['width']}x{v['height']} {v['pix_fmt']} "
                 f"{v['r_frame_rate']} fps, {int(v.get('nb_frames', 0))} frames",
        "video_kbps": round(int(v.get("bit_rate", 0)) / 1000),
        "audio": f"{a['codec_name']} {a['sample_rate']} Hz {a['channels']} ch {round(int(a.get('bit_rate', 0)) / 1000)} kbps" if a else None,
        "duration_s": round(float(j["format"]["duration"]), 3),
        "size_mb": round(int(j["format"]["size"]) / 1e6, 1),
    }


def loudness(mp4):
    from .vo import measure
    return measure(mp4)


def decode_small(mp4, w=320, h=180):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-vf", f"scale={w}:{h}", "-f", "rawvideo",
                        "-pix_fmt", "rgb24", "-"], capture_output=True)
    return np.frombuffer(r.stdout, np.uint8).reshape(-1, h, w, 3).astype(np.float32) / 255.0


def frame_diffs(frames):
    return np.abs(np.diff(frames, axis=0)).mean(axis=(1, 2, 3))


def detect_cuts(diffs, thr=0.06):
    """Frame indices n where frame n starts a new shot (big change vs n-1)."""
    return [i + 1 for i, d in enumerate(diffs) if d > thr]


def flash_frames(frames, diffs, thr=0.06):
    """Isolated frames: n differs strongly from both n-1 and n+1 while n-1 ~ n+1."""
    out = []
    for n in range(1, len(frames) - 1):
        if diffs[n - 1] > thr and diffs[n] > thr:
            if np.abs(frames[n - 1] - frames[n + 1]).mean() < thr * 0.5:
                out.append(n)
    return out


def lum_sat(img):
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    mx, mn = img.max(-1), img.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    return float(np.median(lum)), float(np.median(sat))


def extract(mp4, t, path):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", mp4, "-frames:v", "1", path], check=True)
    return path


def dark_run_widths(png, row, x0, x1, thr=0.18):
    """Widths (px) of dark runs along one row: a direct measurement of outline thickness."""
    from PIL import Image
    im = np.asarray(Image.open(png).convert("L"), np.float32) / 255.0
    seg = im[row, x0:x1] < thr
    runs, n = [], 0
    for v in seg:
        if v:
            n += 1
        elif n:
            runs.append(n)
            n = 0
    if n:
        runs.append(n)
    return runs


def transcribe_check(mp4, script_text, model="small.en"):
    """Re-transcribe the FINAL mix: if SFX/bed masked the VO, the word match drops."""
    import difflib
    import re

    import soundfile as sf
    from faster_whisper import WhisperModel
    from scipy.signal import resample_poly
    tmp = mp4 + ".qc.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", mp4, "-ac", "1", "-ar", "16000", tmp], check=True)
    aud, _ = sf.read(tmp, dtype="float32")
    os.remove(tmp)
    segs, _ = WhisperModel(model, device="cpu", compute_type="int8").transcribe(aud, language="en", beam_size=5)
    got = " ".join(s.text.strip() for s in segs)
    n = lambda s: [w for w in re.sub(r"[^a-z0-9 ]", " ", s.lower()).split() if w]
    ratio = difflib.SequenceMatcher(a=n(script_text), b=n(got)).ratio()
    return {"transcript": got, "word_match_ratio": round(ratio, 3)}
