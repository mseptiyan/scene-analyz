"""Shared helpers for the full-length production (chapters 1-5)."""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
sys.path.insert(0, HERE)
os.environ.setdefault("CV_AUDIO", "/home/user/work/spacex-ipo/audio_full")

from crayon_engine import backgrounds as bg  # noqa: E402,F401
from crayon_engine import character as ch  # noqa: E402,F401
from crayon_engine import fx  # noqa: E402,F401
from crayon_engine import props as pr  # noqa: E402,F401
from crayon_engine import props2 as p2  # noqa: E402,F401
from crayon_engine.core import FPS, PAL, H, W, Camera, clamp, drift, ease_in_out, ease_out, lerp, pop, shake  # noqa: E402,F401
from crayon_engine.text import balloon, label, text, write_on_chars  # noqa: E402,F401
from crayon_engine.timeline import Shot, Words  # noqa: E402

AUD = os.environ["CV_AUDIO"]
WD = Words(os.path.join(AUD, "words.json"), os.path.join(AUD, "lines.json"))


def T(line, token=None, nth=0, end=False):
    return WD.t(line, token, nth, end)


def C(line, token=None, lead=0.2, nth=0):
    """Cut time: 0.2 s before the phrase (reference median 0.22 s)."""
    return WD.cut(line, token, lead, nth)


def LE(line):
    return WD.line(line)["end"]


def LS(line):
    return WD.line(line)["start"]


def cam(rate, focus=(W / 2, H / 2), focus_end=None):
    return lambda d: drift(rate, d, focus, focus_end)


def scaled(ctx, x, y, s):
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(max(s, 1e-3), max(s, 1e-3))
    ctx.translate(-x, -y)


def pop_label(f, s, x, y, t0, size=60, color=PAL["paper"], arrow_to=None, write=False):
    k = pop(f.T, t0)
    if k <= 0:
        return
    scaled(f.ctx, x, y, k)
    chars = write_on_chars(f.T, t0, 28) if write else None
    label(f.ctx, f, s, x, y, size, color=color, arrow_to=arrow_to, chars=chars)
    f.ctx.restore()


def wlabel(f, s, x, y, t0, size=60, color=PAL["paper"], arrow_to=None, cps=26):
    """Write-on label starting at t0."""
    if f.T >= t0:
        label(f.ctx, f, s, x, y, size, color=color, arrow_to=arrow_to, chars=write_on_chars(f.T, t0, cps))


def popped(f, t0, x, y, fn, pre=False):
    """Draw fn() scaled by a pop starting at t0 around (x, y). pre=True pre-rolls 2 frames (on-cut pops)."""
    k = pop(f.T, t0 - (2 / 30 if pre else 0))
    if k <= 0:
        return
    scaled(f.ctx, x, y, k)
    fn()
    f.ctx.restore()


def S(id_, fn, start, camf=None, size="MS", angle="eye-level frontal", camtxt=None, action="", expr="—", txt="—",
      sfx="—", trans="hard cut"):
    return Shot(id_, fn, start, camf, dict(size=size, angle=angle, cam=camtxt or ("locked-off" if camf is None else "drift"),
                                           action=action, expr=expr, txt=txt, sfx=sfx, trans=trans))


def chapter_card(n, title):
    def draw(f):
        bg.card(f)
        c = write_on_chars(f.T, f.T - f.t + 0.12, 26)
        head = f"Chapter {n}"
        text(f.ctx, head, 960, 440, 70, color="#BDBDBD", kind="script", chars=c)
        text(f.ctx, title, 960, 610, 130, color=PAL["paper"], kind="script", chars=max(0, c - len(head)))
    return draw


def punch_card(lines, line_id, size=110):
    """Black punchline card; write-on paced to the VO line."""
    def draw(f):
        bg.card(f)
        t0, t1 = T(line_id), LE(line_id)
        total = sum(len(s) for s in lines)
        cps = max(14, total / max(0.6, (t1 - t0) * 0.85))
        c = write_on_chars(f.T, t0, cps)
        used = 0
        n = len(lines)
        for i, s in enumerate(lines):
            y = 540 - (n - 1) * size * 0.6 + i * size * 1.2 + size * 0.3
            text(f.ctx, s, 960, y, size, color=PAL["paper"], kind="script", chars=max(0, c - used))
            used += len(s)
    return draw


def cal(f, x, y, w, page, sub, t0=None, pages=None, interval=0.12):
    """Desk calendar as a time marker. Single page, or flip through `pages` from t0."""
    if pages:
        return pr.calendar(f, x, y, w, pages, f.T, t0, flip_dur=3 / 30, interval=interval, sub=sub)
    return pr.calendar(f, x, y, w, [page], f.T, f.T + 99, sub=sub)
