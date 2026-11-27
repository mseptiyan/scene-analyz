"""Handwritten text rendered from TTF outlines (fontTools -> cairo paths).

No fontconfig dependency: glyph outlines are read from the OFL fonts in ./fonts and replayed
as cairo paths. That gives per-letter control for the write-on effect (letter by letter,
reference §3.7) and an outer ink stroke for contrast (QC: text contrast >= 4.5:1).
"""
from __future__ import annotations

import math
import os
from functools import lru_cache

from fontTools.pens.basePen import BasePen
from fontTools.ttLib import TTFont

from .core import PAL, hx
from .draw import INK, fill_stroke, rrect, set_color

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
FONTS = {
    "hand": "PatrickHand-Regular.ttf",   # labels, dialogue, numbers
    "script": "Caveat-Bold.ttf",         # chapter cards, punchlines
    "marker": "Kalam-Bold.ttf",          # headlines, signs
}


class _RecPen(BasePen):
    def __init__(self, glyphset):
        super().__init__(glyphset)
        self.ops = []

    def _moveTo(self, p):
        self.ops.append(("M", p))

    def _lineTo(self, p):
        self.ops.append(("L", p))

    def _curveToOne(self, p1, p2, p3):
        self.ops.append(("C", (p1, p2, p3)))

    def _qCurveToOne(self, p1, p2):
        p0 = self._getCurrentPoint()
        c1 = (p0[0] + 2 / 3 * (p1[0] - p0[0]), p0[1] + 2 / 3 * (p1[1] - p0[1]))
        c2 = (p2[0] + 2 / 3 * (p1[0] - p2[0]), p2[1] + 2 / 3 * (p1[1] - p2[1]))
        self.ops.append(("C", (c1, c2, p2)))

    def _closePath(self):
        self.ops.append(("Z", None))

    _endPath = _closePath


class Font:
    def __init__(self, path):
        self.tt = TTFont(path)
        self.upm = self.tt["head"].unitsPerEm
        self.cmap = self.tt.getBestCmap()
        self.gs = self.tt.getGlyphSet()
        self.hmtx = self.tt["hmtx"]
        os2 = self.tt["OS/2"]
        self.cap = getattr(os2, "sCapHeight", 0) or int(self.upm * 0.7)
        self._cache = {}

    def glyph(self, ch):
        name = self.cmap.get(ord(ch)) or self.cmap.get(ord("?"))
        if name not in self._cache:
            pen = _RecPen(self.gs)
            self.gs[name].draw(pen)
            self._cache[name] = (pen.ops, self.hmtx[name][0])
        return self._cache[name]

    def width(self, text, size, tracking=0.0):
        return sum(self.glyph(c)[1] for c in text) * size / self.upm + tracking * size * max(0, len(text) - 1)


@lru_cache(maxsize=None)
def font(kind="hand") -> Font:
    return Font(os.path.join(FONT_DIR, FONTS.get(kind, kind)))


def _path(ctx, fnt, text, x, y, size, slant, tracking, jitter_seed=None):
    s = size / fnt.upm
    pen_x = 0.0
    for i, ch in enumerate(text):
        ops, adv = fnt.glyph(ch)
        if ops:
            ctx.save()
            ctx.translate(x + pen_x, y)
            if jitter_seed is not None:  # hand-made wobble: tiny per-letter rotation/baseline
                k = math.sin((i + 1) * 12.9898 + jitter_seed * 78.233) * 43758.5453 % 1.0
                ctx.translate(0, (k - 0.5) * size * 0.035)
                ctx.rotate((k - 0.5) * 0.05)
            ctx.transform(_shear(slant))
            ctx.scale(s, -s)
            for op, p in ops:
                if op == "M":
                    ctx.move_to(*p)
                elif op == "L":
                    ctx.line_to(*p)
                elif op == "C":
                    ctx.curve_to(*p[0], *p[1], *p[2])
                else:
                    ctx.close_path()
            ctx.restore()
        pen_x += adv * s + tracking * size
    return pen_x


def _shear(slant):
    import cairo
    return cairo.Matrix(1, 0, -slant, 1, 0, 0)


def text(ctx, s, x, y, size=64, color=PAL["paper"], kind="hand", align="center", stroke=None,
         stroke_px=None, slant=0.0, tracking=0.0, chars=None, alpha=1.0, jitter=None, valign="baseline"):
    """Draw text. (x, y) is the baseline anchor; align left/center/right.
    `chars` = number of characters visible (write-on). `stroke` = outer ink border colour."""
    fnt = font(kind)
    full_w = fnt.width(s, size, tracking)
    vis = s if chars is None else s[:max(0, int(chars))]
    if not vis:
        return full_w
    x0 = x - full_w / 2 if align == "center" else x - full_w if align == "right" else x
    if valign == "middle":
        y = y + fnt.cap * size / fnt.upm / 2
    if stroke is not None:
        sw = stroke_px if stroke_px is not None else max(3.0, size * 0.09)
        _path(ctx, fnt, vis, x0, y, size, slant, tracking, jitter)
        set_color(ctx, stroke, alpha)
        ctx.set_line_width(sw * 2)
        ctx.set_line_join(1)  # round
        ctx.stroke()
    _path(ctx, fnt, vis, x0, y, size, slant, tracking, jitter)
    set_color(ctx, color, alpha)
    ctx.fill()
    return full_w


def write_on_chars(t, t0, cps=24.0):
    """Number of characters visible for a letter-by-letter write-on starting at t0."""
    return max(0, int((t - t0) * cps)) if t >= t0 else 0


def multiline(ctx, lines, x, y, size, lh=1.15, **kw):
    """Draw several lines centred around (x, y) (y = middle of the block). Write-on spans lines."""
    chars = kw.pop("chars", None)
    n = len(lines)
    top = y - (n - 1) * size * lh / 2
    used = 0
    for i, ln in enumerate(lines):
        c = None if chars is None else max(0, chars - used)
        text(ctx, ln, x, top + i * size * lh, size, chars=c, valign="middle", **kw)
        used += len(ln)


def balloon(ctx, f, s, x, y, tail_to, size=46, pad=22, kind="hand", fill=PAL["paper"], chars=None, scale=1.0):
    """Square-ish white dialogue balloon with a tail tick pointing at the speaker's mouth."""
    fnt = font(kind)
    w = fnt.width(s, size) + pad * 2
    h = size * 1.25 + pad * 1.2
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(scale, scale)
    bx, by = -w / 2, -h / 2
    tx, ty = (tail_to[0] - x) / max(scale, 1e-3), (tail_to[1] - y) / max(scale, 1e-3)
    # tail (drawn first so the body outline covers its base)
    base = max(bx + 30, min(bx + w - 30, tx * 0.35))
    ang_y = by + h if ty > 0 else by
    ctx.move_to(base - 18, ang_y)
    ctx.line_to(tx * 0.55, ty * 0.55 + (h / 2 if ty > 0 else -h / 2) * 0.45)
    ctx.line_to(base + 18, ang_y)
    ctx.close_path()
    fill_stroke(ctx, fill, f.lw(6))
    rrect(ctx, bx, by, w, h, 18)
    fill_stroke(ctx, fill, f.lw(6))
    # cover the tail seam
    ctx.move_to(base - 15, ang_y)
    ctx.line_to(base + 15, ang_y)
    set_color(ctx, fill)
    ctx.set_line_width(f.lw(8))
    ctx.stroke()
    text(ctx, s, 0, size * 0.36, size, color=INK, kind=kind, chars=chars, slant=0.12)
    ctx.restore()
    return w, h


def label(ctx, f, s, x, y, size=54, color=PAL["paper"], arrow_to=None, chars=None, kind="hand", slant=0.08):
    """Handwritten white label with ink stroke and an optional hand-drawn arrow."""
    if arrow_to is not None:
        ax, ay = arrow_to
        sx, sy = x, y + (size * 0.25 if ay > y else -size * 0.9)
        mx, my = (sx + ax) / 2 + (ay - sy) * 0.25, (sy + ay) / 2 - (ax - sx) * 0.12
        for c, wpx in ((INK, 12), (hx(color), 5)):
            ctx.move_to(sx, sy)
            ctx.curve_to(mx, my, mx, my, ax, ay)
            set_color(ctx, c)
            ctx.set_line_width(f.lw(wpx))
            ctx.set_line_cap(1)
            ctx.stroke()
        ang = math.atan2(ay - my, ax - mx)
        for c, wpx in ((INK, 12), (hx(color), 5)):
            for da in (2.6, -2.6):
                ctx.move_to(ax, ay)
                ctx.line_to(ax + math.cos(ang + da) * 26, ay + math.sin(ang + da) * 26)
            set_color(ctx, c)
            ctx.set_line_width(f.lw(wpx))
            ctx.set_line_cap(1)
            ctx.stroke()
    return text(ctx, s, x, y, size, color=color, kind=kind, stroke=PAL["ink"], stroke_px=f.lw(5),
                slant=slant, chars=chars)
