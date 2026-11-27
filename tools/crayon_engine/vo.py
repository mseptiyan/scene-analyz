"""Voice-over pipeline: Kokoro TTS -> per-chapter WAV -> loudness -> word timestamps.

Usage:
    python -m crayon_engine.vo <vo_config.json> <out_dir>

Outputs in <out_dir>:
    vo_<chapter>.wav      per chapter, normalised to -14 LUFS / TP <= -1 dBTP
    vo_master.wav         all chapters + card silences concatenated (pilot timeline)
    words.json            word timestamps (faster-whisper on the TTS audio), aligned to the script text
    lines.json            start/end of every script line on the master timeline
"""
from __future__ import annotations

import difflib
import json
import os
import re
import subprocess
import sys

import numpy as np
import soundfile as sf

os.environ.setdefault("HF_HUB_DISABLE_XET", "1")


def _trim(aud: np.ndarray, sr: int, thr_db: float = -45.0, keep: float = 0.03) -> np.ndarray:
    """Trim leading/trailing silence, keep a few ms so consonants are not clipped."""
    if aud.size == 0:
        return aud
    thr = 10 ** (thr_db / 20)
    env = np.convolve(np.abs(aud), np.ones(256) / 256, mode="same")
    idx = np.where(env > thr)[0]
    if idx.size == 0:
        return aud
    k = int(keep * sr)
    return aud[max(0, idx[0] - k): min(aud.size, idx[-1] + k)]


def synth_lines(cfg: dict) -> dict:
    """Synthesize every line. Returns {chapter_id: [(line_id, say, audio, pause)]}."""
    from kokoro import KPipeline

    pipe = KPipeline(lang_code=cfg.get("lang_code", "a"))
    sr = cfg.get("sample_rate", 24000)
    out = {}
    for ch in cfg["chapters"]:
        if "lines" not in ch:
            continue
        rows = []
        for ln in ch["lines"]:
            parts = [a.numpy() if hasattr(a, "numpy") else np.asarray(a)
                     for _, _, a in pipe(ln["say"], voice=cfg["voice"], speed=cfg.get("speed", 1.0))]
            aud = _trim(np.concatenate(parts).astype(np.float32), sr)
            rows.append((ln["id"], ln["say"], aud, ln.get("pause", cfg.get("default_pause", 0.4))))
            print(f"  line {ln['id']}: {aud.size / sr:.2f}s", flush=True)
        out[ch["id"]] = rows
    return out


def loudnorm(src: str, dst: str, I: float = -14.0, TP: float = -1.2, LRA: float = 11.0) -> dict:
    """Hit -14 LUFS with true peak <= -1 dBTP.

    Speech TTS has a high crest factor, so a plain linear gain cannot reach -14 LUFS without
    the peaks going over. Step 1 applies gain to the target loudness and then a 4x-oversampled
    brickwall limiter (a true-peak approximation). Step 2 runs a two-pass linear loudnorm that
    only fine-tunes the level.
    """
    pre = measure(src)
    gain = I - pre["integrated_lufs"]
    tmp = dst + ".lim.wav"
    lim = 10 ** ((TP - 0.6) / 20)
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", src, "-af",
                    f"aresample=192000,volume={gain:.2f}dB,alimiter=limit={lim:.4f}:attack=1:release=60:level=false,"
                    "aresample=48000", "-c:a", "pcm_f32le", tmp], check=True)
    p1 = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", tmp, "-af",
         f"loudnorm=I={I}:TP={TP}:LRA={LRA}:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True)
    m = json.loads(p1.stderr[p1.stderr.rindex("{"): p1.stderr.rindex("}") + 1])
    af = (f"loudnorm=I={I}:TP={TP}:LRA={LRA}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", tmp, "-af", af,
                    "-ar", "48000", "-c:a", "pcm_s24le", dst], check=True)
    os.remove(tmp)
    return measure(dst)


def measure(path: str) -> dict:
    """Integrated loudness (LUFS) and true peak (dBTP) via ffmpeg ebur128."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    summ = r[r.rfind("Summary:"):]
    I = float(re.search(r"I:\s+(-?[\d.]+) LUFS", summ).group(1))
    tp = re.search(r"True peak:\s+Peak:\s+(-?[\d.]+|-inf) dBFS", summ, re.S)
    return {"integrated_lufs": I, "true_peak_dbtp": float(tp.group(1)) if tp else None}


def _norm_word(w: str) -> str:
    return re.sub(r"[^a-z0-9]", "", w.lower())


def align_words(master_wav: str, lines_meta: list, model_size: str = "small.en") -> list:
    """Run faster-whisper with word timestamps, then map the script words onto the
    recognised words (difflib), so every script word gets a time even if whisper mishears."""
    from faster_whisper import WhisperModel

    from scipy.signal import resample_poly

    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    aud, sr = sf.read(master_wav, dtype="float32")
    if aud.ndim > 1:
        aud = aud.mean(axis=1)
    g = np.gcd(int(sr), 16000)
    aud16 = resample_poly(aud, 16000 // g, int(sr) // g).astype(np.float32)
    segs, _ = model.transcribe(aud16, word_timestamps=True, language="en", beam_size=5,
                               vad_filter=False, condition_on_previous_text=False)
    rec = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
    script = []
    for lm in lines_meta:
        for w in lm["say"].replace("I.P.O.", "IPO").split():
            script.append((w, lm["id"], lm["start"], lm["end"]))
    a = [_norm_word(w) for w, *_ in script]
    b = [_norm_word(w) for w, *_ in rec]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    times = [None] * len(script)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            times[blk.a + k] = (rec[blk.b + k][1], rec[blk.b + k][2])
    words = []
    for i, (w, lid, ls, le) in enumerate(script):
        t = times[i]
        if t is None:  # interpolate inside the known line bounds
            prev = next((times[j] for j in range(i - 1, -1, -1) if times[j]), (ls, ls))
            nxt = next((times[j] for j in range(i + 1, len(times)) if times[j]), (le, le))
            t = (max(prev[1], ls), min(nxt[0], le))
            src = "interp"
        else:
            src = "whisper"
        words.append({"i": i, "word": w, "line": lid, "start": round(t[0], 3), "end": round(t[1], 3), "src": src})
    recog_text = " ".join(r[0] for r in rec)
    return clamp_to_lines(words, lines_meta), recog_text


def clamp_to_lines(words: list, lines_meta: list) -> list:
    """Whisper tends to place a segment's first word early. The assembly knows exactly where
    each line starts, so the first word of every line is pinned to that start (+20 ms) and all
    other words are clamped inside their line and kept monotonic."""
    bounds = {str(m["id"]): (m["start"], m["end"]) for m in lines_meta}
    prev_line = None
    last = 0.0
    for w in words:
        ls, le = bounds[str(w["line"])]
        if str(w["line"]) != prev_line:
            w["start"], w["src"] = round(ls + 0.02, 3), w["src"] + "+pinned"
            prev_line = str(w["line"])
        w["start"] = round(min(max(w["start"], ls, last), le), 3)
        w["end"] = round(min(max(w["end"], w["start"] + 0.05), le), 3)
        last = w["start"]
    return words


def build(cfg_path: str, out_dir: str) -> None:
    cfg = json.load(open(cfg_path))
    os.makedirs(out_dir, exist_ok=True)
    sr = cfg.get("sample_rate", 24000)
    print("[vo] synthesising with Kokoro voice", cfg["voice"], flush=True)
    synth = synth_lines(cfg)

    master, lines_meta, t = [], [], 0.0
    report = {"voice": cfg["voice"], "speed": cfg.get("speed", 1.0), "chapters": {}}
    for ch in cfg["chapters"]:
        if "silence" in ch:
            n = int(ch["silence"] * sr)
            master.append(np.zeros(n, np.float32))
            lines_meta.append({"id": ch["id"], "say": "", "start": round(t, 3), "end": round(t + ch["silence"], 3),
                               "chapter": ch["id"]})
            t += ch["silence"]
            continue
        chunk = []
        for lid, say, aud, pause in synth[ch["id"]]:
            lines_meta.append({"id": lid, "say": say, "start": round(t, 3), "end": round(t + aud.size / sr, 3),
                               "chapter": ch["id"]})
            chunk += [aud, np.zeros(int(pause * sr), np.float32)]
            t += aud.size / sr + pause
        ch_aud = np.concatenate(chunk)
        raw = os.path.join(out_dir, f"_raw_{ch['id']}.wav")
        sf.write(raw, ch_aud, sr)
        stats = loudnorm(raw, os.path.join(out_dir, f"vo_{ch['id']}.wav"))
        os.remove(raw)
        nwords = sum(len(s.split()) for _, s, _, _ in synth[ch["id"]])
        speech = sum(a.size for _, _, a, _ in synth[ch["id"]]) / sr
        report["chapters"][ch["id"]] = {**stats, "duration_s": round(ch_aud.size / sr, 2), "words": nwords,
                                        "wpm_speech_only": round(nwords / speech * 60, 1),
                                        "wpm_incl_pauses": round(nwords / (ch_aud.size / sr) * 60, 1)}
        master.append(ch_aud)

    raw = os.path.join(out_dir, "_raw_master.wav")
    sf.write(raw, np.concatenate(master), sr)
    report["master"] = loudnorm(raw, os.path.join(out_dir, "vo_master.wav"))
    # whisper on the 24 kHz raw audio (same timeline)
    print("[vo] aligning words with faster-whisper", flush=True)
    words, recog = align_words(raw, [m for m in lines_meta if m["say"]])
    os.remove(raw)
    report["whisper_text"] = recog
    report["words_from_whisper"] = sum(w["src"] == "whisper" for w in words)
    report["words_total"] = len(words)
    json.dump(words, open(os.path.join(out_dir, "words.json"), "w"), indent=1)
    json.dump(lines_meta, open(os.path.join(out_dir, "lines.json"), "w"), indent=1)
    json.dump(report, open(os.path.join(out_dir, "vo_report.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in report.items() if k != "whisper_text"}, indent=1))


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
