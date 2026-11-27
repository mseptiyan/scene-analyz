"""Vector primitives: flat fill + uniform dark outline + one hard cel shadow (no gradients)."""
from __future__ import annotations

import math

import cairo

from .core import PAL, hx, shade

INK = hx(PAL["ink"])
KEY_LIGHT = (-1.0, -0.7)  # light from upper-left -> crescent shadows sit lower-right


def set_color(ctx, c, a: float = 1.0):
    r, g, b = hx(c)
    ctx.set_source_rgba(r, g, b, a)


def fill_stroke(ctx, fill=None, lw: float = 8, ink=INK, alpha: float = 1.0, preserve=False):
    """Fill the current path flat, then stroke it with a round-joined outline."""
    if fill is not None:
        set_color(ctx, fill, alpha)
        ctx.fill_preserve()
    if lw > 0:
        set_color(ctx, ink, alpha)
        ctx.set_line_width(lw)
        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        if preserve:
            ctx.stroke_preserve()
        else:
            ctx.stroke()
    elif not preserve:
        ctx.new_path()


def circle(ctx, x, y, r):
    ctx.new_sub_path()
    ctx.arc(x, y, max(r, 0.01), 0, 2 * math.pi)
    ctx.close_path()


def ellipse(ctx, x, y, rx, ry):
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(max(rx, 0.01), max(ry, 0.01))
    ctx.new_sub_path()
    ctx.arc(0, 0, 1, 0, 2 * math.pi)
    ctx.restore()
    ctx.close_path()


def rrect(ctx, x, y, w, h, r):
    r = max(0.0, min(r, w / 2, h / 2))
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    ctx.arc(x + r, y + r, r, math.pi, 1.5 * math.pi)
    ctx.close_path()


def poly(ctx, pts, close=True):
    ctx.move_to(*pts[0])
    for p in pts[1:]:
        ctx.line_to(*p)
    if close:
        ctx.close_path()


def bean(ctx, cx, top, w, h, bottom_flare: float = 1.08):
    """Egg/bean body: rounded shoulders, fuller rounded bottom (this IS the clothing)."""
    l, r = cx - w / 2, cx + w / 2
    bw = w * bottom_flare / 2
    b = top + h
    ctx.move_to(cx, top)
    ctx.curve_to(cx + 0.44 * w, top, r, top + 0.16 * h, r + (bw - w / 2) * 0.6, top + 0.48 * h)
    ctx.curve_to(cx + bw, top + 0.86 * h, cx + 0.34 * w, b, cx, b)
    ctx.curve_to(cx - 0.34 * w, b, cx - bw, top + 0.86 * h, l - (bw - w / 2) * 0.6, top + 0.48 * h)
    ctx.curve_to(l, top + 0.16 * h, cx - 0.44 * w, top, cx, top)
    ctx.close_path()


def crescent(ctx, path_fn, size: float, color, k: float = 0.2, light=KEY_LIGHT, alpha: float = 1.0):
    """One hard crescent shadow inside the shape drawn by `path_fn(ctx)`, on the side away
    from the key light. The cutter is the same shape shifted toward the light by k*size."""
    lx, ly = light
    n = math.hypot(lx, ly) or 1
    dx, dy = lx / n * k * size, ly / n * k * size
    ctx.save()
    path_fn(ctx)
    ctx.clip()
    ctx.new_path()
    ctx.rectangle(-1e5, -1e5, 2e5, 2e5)
    ctx.save()
    ctx.translate(dx, dy)
    path_fn(ctx)
    ctx.restore()
    ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
    set_color(ctx, color, alpha)
    ctx.fill()
    ctx.restore()


def shaded_shape(ctx, path_fn, fill, size, lw, shadow=None, k=0.2, light=KEY_LIGHT, ink=INK, alpha=1.0):
    """Flat fill + crescent shadow + outline, in that order."""
    path_fn(ctx)
    set_color(ctx, fill, alpha)
    ctx.fill()
    if shadow is not False:
        crescent(ctx, path_fn, size, shadow if shadow is not None else shade(fill), k, light, alpha)
    path_fn(ctx)
    fill_stroke(ctx, None, lw, ink, alpha)


def line(ctx, pts, lw, color=INK, alpha=1.0, curve=False):
    """Polyline (or smooth quadratic chain when curve=True) with round caps."""
    set_color(ctx, color, alpha)
    ctx.set_line_width(lw)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.move_to(*pts[0])
    if curve and len(pts) == 3:
        (x0, y0), (cx, cy), (x1, y1) = pts
        ctx.curve_to(x0 + 2 / 3 * (cx - x0), y0 + 2 / 3 * (cy - y0),
                     x1 + 2 / 3 * (cx - x1), y1 + 2 / 3 * (cy - y1), x1, y1)
    else:
        for p in pts[1:]:
            ctx.line_to(*p)
    ctx.stroke()


def contact_shadow(ctx, x, y, rx, ry=None, alpha=0.28):
    """Soft-ish contact ellipse under feet (flat, two concentric bands instead of blur)."""
    ry = ry or rx * 0.22
    for s, a in ((1.0, alpha * 0.55), (0.72, alpha)):
        ellipse(ctx, x, y, rx * s, ry * s)
        set_color(ctx, INK, a)
        ctx.fill()


def outlined_stroke(ctx, pts_fn, color, lw_inner, lw_ink):
    """A thick coloured stroke with an ink border (ropes, chart lines): ink wide, colour narrow."""
    for c, w in ((INK, lw_inner + 2 * lw_ink), (color, lw_inner)):
        pts_fn(ctx)
        set_color(ctx, c)
        ctx.set_line_width(w)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.stroke()
