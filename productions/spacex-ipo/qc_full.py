"""Automated QC for the full video (streaming, so 18k frames fit in memory).

    python qc_full.py <mp4> <out_dir>
"""
from __future__ import annotations

import json
import math
import os
import subprocess
import sys

import numpy as np

import common  # noqa: F401
import full
from common import WD
from crayon_engine import qc
from crayon_engine.core import FPS

MP4 = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
tl = full.build()
R = {"probe": qc.probe(MP4), "loudness": qc.loudness(MP4)}

# ---- stream frames at 320x180: diffs, flash frames, lum/sat samples
w, h = 320, 180
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", MP4, "-vf", f"scale={w}:{h}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                     stdout=subprocess.PIPE)
fs = w * h * 3
diffs, flashes, ls = [], [], {}
prev2 = prev1 = None
n = 0
while True:
    buf = p.stdout.read(fs)
    if len(buf) < fs:
        break
    fr = np.frombuffer(buf, np.uint8).reshape(h, w, 3).astype(np.float32) / 255.0
    if prev1 is not None:
        diffs.append(float(np.abs(fr - prev1).mean()))
    if prev2 is not None and len(diffs) >= 2:
        if diffs[-2] > 0.06 and diffs[-1] > 0.06 and float(np.abs(prev2 - fr).mean()) < 0.03:
            flashes.append(n - 1)
    if n % 10 == 0:
        ls[n] = qc.lum_sat(fr)
    prev2, prev1 = prev1, fr
    n += 1
p.wait()
d = np.array(diffs)
R["frames_decoded"] = n
R["flash_frames"] = flashes
planned = [round(s.start * FPS) for s in tl.shots[1:]]
cuts = [i + 1 for i, v in enumerate(d) if v > 0.06]
R["cuts_planned"] = len(planned)
R["cuts_detected_within_1f"] = sum(1 for c in planned if any(abs(c - x) <= 1 for x in cuts))

rows = []
for s in tl.shots:
    a, b = int(math.ceil(s.start * FPS)), int(s.end * FPS)
    seg = d[a:max(a + 1, b - 1)]
    first = next((wd for wd in WD.words if s.start <= wd["start"] < s.end), None)
    smp = [v for k, v in ls.items() if a <= k < b]
    rows.append(dict(id=s.id, start=round(s.start, 3), dur=round(s.dur, 2),
                     lead_to_vo=round(first["start"] - s.start, 3) if first else None,
                     cam_rate=round(s.camera().rate_per_s(s.dur) * 100, 2),
                     lum=round(float(np.median([x[0] for x in smp])), 3) if smp else None,
                     sat=round(float(np.median([x[1] for x in smp])), 3) if smp else None,
                     static_pct=round(float((seg < 1e-4).mean() * 100), 1) if seg.size else 0.0))
R["shots"] = rows
leads = [r["lead_to_vo"] for r in rows[1:] if r["lead_to_vo"] is not None]
R["lead_stats"] = {"n": len(leads), "min": min(leads), "max": max(leads), "median": float(np.median(leads)),
                   "in_0.1_0.3": sum(0.1 <= x <= 0.3 for x in leads)}
R["cam_rates_moving"] = sorted({abs(r["cam_rate"]) for r in rows if r["cam_rate"]})
R["dead_hold_shots"] = [r["id"] for r in rows if r["static_pct"] > 40 and not r["id"] in
                        ("SH070", "SH245", "SH505", "SH645", "SH935", "SH770", "SH930", "SH1110")]
R["dark_shots_lt_0.25_over_3s"] = [r["id"] for r in rows if r["lum"] is not None and r["lum"] < 0.25 and r["dur"] > 3
                                   and r["id"] not in ("SH070", "SH245", "SH505", "SH645", "SH935", "SH770", "SH930", "SH1110")]
sats = [v[1] for v in ls.values()]
R["sat_median_all_frames"] = round(float(np.median(sats)), 3)

# ---- frames around every cut (-1, 0, +1) in one decoding pass
sel = sorted({c + k for c in planned for k in (-1, 0, 1)})
expr = "+".join(f"eq(n\\,{x})" for x in sel)
cutdir = os.path.join(OUT, "cuts")
os.makedirs(cutdir, exist_ok=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", MP4, "-vf", f"select='{expr}',scale=320:180", "-vsync", "0",
                os.path.join(cutdir, "f_%05d.png")], check=True)
R["cut_frames_extracted"] = len(os.listdir(cutdir))
json.dump({"sel": sel}, open(os.path.join(cutdir, "index.json"), "w"))

# ---- re-transcribe the final mix
script = " ".join(l["say"] for l in WD.lines.values() if l["say"]).replace("I.P.O.", "IPO")
R["final_mix_transcript"] = qc.transcribe_check(MP4, script)
json.dump(R, open(os.path.join(OUT, "qc_auto_full.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in R.items() if k not in ("shots", "final_mix_transcript")}, indent=1))
print("transcript match", R["final_mix_transcript"]["word_match_ratio"])
