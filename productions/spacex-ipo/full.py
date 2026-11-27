"""FULL VIDEO (~10 min): The SpaceX IPO Explained Like You're 5.

Timeline = hook + chapter 1 opening (pilot shots, re-timed on the full VO) + chapters 1-5.
All cuts come from the full VO word timestamps (audio_full/words.json).

    python full.py render     # -> renders/spacex_ipo_full.mp4
    python full.py stills     # A/M/Z frames per shot -> /home/user/work/spacex-ipo/qc_full
    python full.py shotlist   # -> shotlist_full.md
    python full.py srt        # -> full.srt
    python full.py thumbnail  # -> assets/thumbnail.png (1280x720)
"""
from __future__ import annotations

import math
import os
import sys

import common  # noqa: F401  (sets CV_AUDIO before pilot is imported)
from common import AUD, LE, WD, H, W
import pilot
import shots_ch12
import shots_ch34
import shots_ch5
from crayon_engine import backgrounds as bgmod
from crayon_engine.core import FPS
from crayon_engine.timeline import Timeline

bgmod.BG_DESAT = 0.22  # QC finding #10 (pilot): backgrounds ~12% less saturated
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = "/home/user/work/spacex-ipo"


def total():
    import soundfile as sf
    info = sf.info(os.path.join(AUD, "vo_master.wav"))
    return round(info.frames / info.samplerate, 3)


def build():
    pil = [s for s in pilot.build().shots if s.id != "SH170"]
    shots = pil + shots_ch12.shots() + shots_ch34.shots() + shots_ch5.shots()
    shots.sort(key=lambda s: s.start)
    ids = [s.id for s in shots]
    assert len(ids) == len(set(ids)), "duplicate shot ids"
    return Timeline(shots, total())


def cues():
    p = [c for c in pilot.sfx_cues() if c[0] < WD.line(18)["start"] - 0.5]  # drop the pilot end-slate ticks
    return sorted(p + shots_ch12.cues() + shots_ch34.cues() + shots_ch5.cues())


def tc(sec):
    m, s = divmod(sec, 60)
    return f"{int(m):02d}:{s:05.2f}"


def write_shotlist(tl, path):
    rows = []
    for i, s in enumerate(tl.shots, 1):
        m = s.meta
        camr = s.camera().rate_per_s(s.dur) * 100
        first = next((w for w in WD.words if s.start <= w["start"] < s.end), None)
        lead = f"{first['start'] - s.start:.2f}" if first else "—"
        vo = " ".join(w["word"] for w in WD.words if s.start <= w["start"] < s.end) or "— (no VO)"
        rows.append(f"| {i} | {s.id} | {tc(s.start)} | {s.dur:.2f}s | {m['size']} / {m['angle']} | {m['cam']} "
                    f"(measured {camr:+.1f}%/s) | {m['action']} | {m['expr']} | {m['txt']} | {m['sfx']} | {m['trans']} "
                    f"| {lead} | {vo} |")
    durs = sorted(s.dur for s in tl.shots)
    hdr = ("# Shot list: FULL VIDEO\n\n"
           "Format: `workflows/pre_production.md` §7.3 + sync columns. **Generated from the locked timeline** (`full.py shotlist`); "
           "the timecodes are the real cut points. Cut = start of the phrase's first word − 0.20 s.\n\n"
           f"Total: {tl.total:.2f} s ({tc(tl.total)}) · {len(tl.shots)} shots · {len(tl.shots) / tl.total * 60:.1f} shots/min · "
           f"median shot {durs[len(durs) // 2]:.2f} s · 30 fps · 1920×1080\n\n"
           "| # | Shot ID | TC in | Dur | Size/Angle | Camera | Characters & action | Expression | On-screen text | SFX/Music | Transition out | Cut→VO lead (s) | VO in shot |\n"
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    open(path, "w").write(hdr + "\n".join(rows) + "\n")


def write_srt(path):
    def ts(x):
        h, r = divmod(x, 3600)
        m, sec = divmod(r, 60)
        return f"{int(h):02d}:{int(m):02d}:{int(sec):02d},{int(round((sec % 1) * 1000)) % 1000:03d}"
    from script_text import display
    rows = [l for l in WD.lines.values() if l["say"]]
    with open(path, "w") as fh:
        for k, l in enumerate(rows, 1):
            fh.write(f"{k}\n{ts(l['start'])} --> {ts(l['end'] + 0.15)}\n{display(l['say'])}\n\n")


def thumbnail(path):
    """1280x720 thumbnail: Elon (shock) riding a rocket-chart that snaps into a red arrow, 'CUT IN HALF?!'."""
    import cairo
    from PIL import Image
    from crayon_engine import character as chm
    from crayon_engine import props as pr
    from crayon_engine import props2 as p2
    from crayon_engine.core import PAL, Frame
    from crayon_engine.text import text
    from looks import ELON, RETAIL
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(s)
    f = Frame(ctx=ctx, t=0.4, T=0.4, dur=1)
    bgmod.night_grid(f)
    pts = [(0.0, 0.15), (0.2, 0.35), (0.38, 0.55), (0.5, 0.9)]
    pr.chart(f, 120, 120, 1100, 700, pts, progress=1.0, color=PAL["money"], lw_px=22)
    p2.big_arrow(f, 700, 160, 720, 0.95, color=PAL["loss"], width=150)
    pr.rocket(f, 700, 430, 380, angle=1.45, flame=0.9)        # the rocket he rides
    chm.draw(f, ELON, 700, 405, 380, expr="shock", pose="arms_up", seed=7, shadow_floor=False)
    for i, x in enumerate((170, 1750)):
        chm.draw(f, RETAIL[i], x, 1180, 520, expr="shock", seed=8 + i, facing=0.6 if x < 960 else -0.6)
    text(ctx, "CUT IN", 1440, 380, 230, color=PAL["paper"], kind="marker", stroke=PAL["ink"], stroke_px=18)
    text(ctx, "HALF?!", 1440, 610, 250, color=PAL["gold"], kind="marker", stroke=PAL["ink"], stroke_px=18)
    tmp = path + ".1080.png"
    s.write_to_png(tmp)
    Image.open(tmp).convert("RGB").resize((1280, 720), Image.LANCZOS).save(path, optimize=True)
    os.remove(tmp)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "render"
    tl = build()
    if mode == "render":
        import numpy as np
        import soundfile as sf
        from crayon_engine import audio, render
        out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(WORK, "render_full", "spacex_ipo_full.mp4")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        vo, sr = sf.read(os.path.join(AUD, "vo_master.wav"), dtype="float64")
        pad = np.zeros(max(0, int(tl.total * sr) - vo.size) + int(0.05 * sr))
        sf.write(os.path.join(AUD, "_vo_padded.wav"), np.concatenate([vo, pad]), sr, subtype="PCM_24")
        mixwav = os.path.join(AUD, "mix_full.wav")
        print("mix", audio.mix(os.path.join(AUD, "_vo_padded.wav"), cues(), mixwav), flush=True)
        render.render(tl, out, mixwav, os.path.join(os.path.dirname(out), "_work"))
        print("rendered", out, tl.total)
    elif mode == "stills":
        from crayon_engine import render
        qc = sys.argv[2] if len(sys.argv) > 2 else os.path.join(WORK, "qc_full")
        os.makedirs(qc, exist_ok=True)
        only = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
        for s in tl.shots:
            if only and s.id not in only:
                continue
            for tag, tt in (("A", s.start + 1 / FPS), ("M", (s.start + s.end) / 2), ("Z", s.end - 2 / FPS)):
                render.still(tl, tt, os.path.join(qc, f"{s.id}_{tag}.png"))
        print("stills ok", len(tl.shots))
    elif mode == "shotlist":
        write_shotlist(tl, os.path.join(HERE, "shotlist_full.md"))
        print("shotlist ok")
    elif mode == "srt":
        write_srt(os.path.join(HERE, "full.srt"))
        print("srt ok")
    elif mode == "thumbnail":
        os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
        thumbnail(os.path.join(HERE, "assets", "thumbnail.png"))
        print("thumb ok")
