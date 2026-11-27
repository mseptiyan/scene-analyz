"""More generic props for finance explainers (all original, no real logos).
Conventions: (x, y) centre unless the name says base/bottom; outline 6-8 px via f.lw();
flat fill + one crescent shadow (shaded_shape)."""
from __future__ import annotations

import math

from .core import PAL, clamp, ease_in_out, ease_out, hx, lerp, shade, tint
from .draw import INK, circle, ellipse, fill_stroke, line, outlined_stroke, poly, rrect, set_color, shaded_shape
from .text import font, text


def _box(f, x, y, w, h, color, r=10, lw=7, k=0.10):
    shaded_shape(f.ctx, lambda c: rrect(c, x, y, w, h, r), color, max(w, h), f.lw(lw), k=k)


# ------------------------------------------------------------------ process / paperwork
def countdown_board(f, x, y, w, steps, lit, title="COUNTDOWN"):
    """Launch-style board with numbered steps; the first `lit` steps glow."""
    ctx = f.ctx
    h = 110 + len(steps) * 96
    _box(f, x - w / 2, y - h / 2, w, h, "#24303F", r=18)
    text(ctx, title, x, y - h / 2 + 70, 52, color=PAL["gold"], kind="marker", tracking=0.08)
    for i, s in enumerate(steps):
        yy = y - h / 2 + 140 + i * 96
        on = i < lit
        circle(ctx, x - w / 2 + 70, yy, 26)
        fill_stroke(ctx, "#5CE07A" if on else "#3A4656", f.lw(5))
        if on:
            circle(ctx, x - w / 2 + 70, yy, 40)
            set_color(ctx, "#5CE07A", 0.18)
            ctx.fill()
        text(ctx, f"{i + 1}. {s}", x - w / 2 + 120, yy + 16, 46, color="#F3F3F3" if on else "#7D8794",
             kind="marker", align="left")


def doc_stack(f, x, base_y, w, n=12, label=None, top_text=None):
    ctx = f.ctx
    for i in range(n):
        dx = math.sin(i * 1.7) * 8
        rrect(ctx, x - w / 2 + dx, base_y - (i + 1) * 16, w, 22, 4)
        fill_stroke(ctx, "#FBF8F0" if i % 2 else "#F1ECE0", f.lw(5))
    top = base_y - n * 16 - 6
    rrect(ctx, x - w / 2, top - w * 0.62, w, w * 0.62, 6)
    fill_stroke(ctx, "#FFFFFF", f.lw(6))
    for k in range(5):
        line(ctx, [(x - w * 0.38, top - w * 0.48 + k * w * 0.09), (x + w * 0.38, top - w * 0.48 + k * w * 0.09)],
             f.lw(3), hx("#B9B4A8"))
    if top_text:
        text(ctx, top_text, x, top - w * 0.50, w * 0.16, color=PAL["ink"], kind="marker")
    if label:
        text(ctx, label, x, base_y + 70, 56, color=PAL["paper"], kind="hand", stroke=PAL["ink"], stroke_px=f.lw(5))
    return top - w * 0.62


def envelope(f, x, y, w, label="CONFIDENTIAL", angle=0.0):
    ctx = f.ctx
    h = w * 0.62
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    rrect(ctx, -w / 2, -h / 2, w, h, 6)
    fill_stroke(ctx, "#F2E6C9", f.lw(6))
    poly(ctx, [(-w / 2, -h / 2), (0, h * 0.08), (w / 2, -h / 2)], close=False)
    fill_stroke(ctx, None, f.lw(5))
    circle(ctx, 0, h * 0.08, w * 0.06)
    fill_stroke(ctx, PAL["loss"], f.lw(4))
    text(ctx, label, 0, h * 0.38, w * 0.10, color=PAL["loss_sh"], kind="marker", tracking=0.06)
    ctx.restore()


def mailbox(f, x, base_y, w, label="SEC"):
    ctx = f.ctx
    rrect(ctx, x - 12, base_y - w * 0.9, 24, w * 0.9, 4)
    fill_stroke(ctx, "#5A5D66", f.lw(6))
    h = w * 0.7
    top = base_y - w * 0.9 - h
    ctx.new_path()
    ctx.move_to(x - w / 2, top + h)
    ctx.line_to(x - w / 2, top + w * 0.35)
    ctx.arc(x, top + w * 0.35, w / 2, math.pi, 2 * math.pi)
    ctx.line_to(x + w / 2, top + h)
    ctx.close_path()
    fill_stroke(ctx, "#2F5D8A", f.lw(7))
    rrect(ctx, x - w * 0.3, top + w * 0.25, w * 0.6, 16, 6)
    fill_stroke(ctx, "#11253A", f.lw(4))
    text(ctx, label, x, top + h * 0.82, w * 0.22, color=PAL["paper"], kind="marker", tracking=0.08)
    return (x, top + w * 0.25)


def diary(f, x, y, w, tabs, cover="S-1", open_p=1.0):
    """Open book; tabs = [(label, colour, visible_scale)]."""
    ctx = f.ctx
    h = w * 0.62
    for s in (-1, 1):
        px = x if s > 0 else x - w / 2
        rrect(ctx, px, y - h / 2, w / 2, h, 8)
        fill_stroke(ctx, "#FFFDF6", f.lw(7))
        for k in range(6):
            yy = y - h * 0.32 + k * h * 0.11
            line(ctx, [(px + w * 0.05, yy), (px + w * 0.45, yy)], f.lw(3), hx("#C9C3B6"))
    line(ctx, [(x, y - h / 2), (x, y + h / 2)], f.lw(6))
    text(ctx, cover, x - w / 4, y - h * 0.36, w * 0.08, color=PAL["ink"], kind="marker")
    for i, (lab, col, k) in enumerate(tabs):
        if k <= 0:
            continue
        ty = y - h * 0.32 + i * h * 0.27
        ctx.save()
        ctx.translate(x + w / 2, ty)
        ctx.scale(k, k)
        rrect(ctx, -10, -32, w * 0.24, 64, 10)
        fill_stroke(ctx, col, f.lw(6))
        text(ctx, lab, w * 0.10, 14, 38, color=PAL["paper"], kind="marker", stroke=PAL["ink"], stroke_px=f.lw(4))
        ctx.restore()


def laptop(f, x, base_y, w, screen="#DDEFF7"):
    ctx = f.ctx
    h = w * 0.62
    rrect(ctx, x - w / 2, base_y - h - 20, w, h, 12)
    fill_stroke(ctx, "#2B2B30", f.lw(7))
    rrect(ctx, x - w / 2 + 16, base_y - h - 4, w - 32, h - 32, 6)
    fill_stroke(ctx, screen, f.lw(4))
    poly(ctx, [(x - w * 0.62, base_y + 6), (x + w * 0.62, base_y + 6), (x + w / 2, base_y - 20), (x - w / 2, base_y - 20)])
    fill_stroke(ctx, "#4A4A52", f.lw(6))
    return (x, base_y - h / 2 - 20, w - 40, h - 40)


def bus(f, x, base_y, w, label="ROADSHOW", t=0.0, moving=0.0):
    ctx = f.ctx
    h = w * 0.42
    bob = math.sin(t * 22) * 3 * moving
    y0 = base_y - h - 40 + bob
    for wx in (x - w * 0.30, x + w * 0.30):
        circle(ctx, wx, base_y - 30, 42)
        fill_stroke(ctx, "#2A2A2E", f.lw(7))
        circle(ctx, wx, base_y - 30, 16)
        fill_stroke(ctx, "#9A9AA0", f.lw(4))
    shaded_shape(ctx, lambda c: rrect(c, x - w / 2, y0, w, h, 34), "#F2B630", w, f.lw(8), k=0.06)
    for i in range(4):
        rrect(ctx, x - w * 0.42 + i * w * 0.2, y0 + 26, w * 0.15, h * 0.34, 8)
        fill_stroke(ctx, "#BFE3F2", f.lw(5))
    rrect(ctx, x - w * 0.38, y0 + h * 0.58, w * 0.76, h * 0.26, 8)
    fill_stroke(ctx, "#1E1A1B", f.lw(5))
    text(ctx, label, x, y0 + h * 0.79, h * 0.2, color=PAL["gold"], kind="marker", tracking=0.08)
    return (x - w * 0.42 + w * 0.075, y0 + 26 + h * 0.17)  # first window centre


def table_front(f, x, top_y, w, h=180, color="#6B4A35"):
    _box(f, x - w / 2, top_y, w, h, color, r=10, k=0.05)
    line(f.ctx, [(x - w / 2 + 10, top_y + 22), (x + w / 2 - 10, top_y + 22)], f.lw(4), hx(shade(color, 0.7)))


def easel_chart(f, x, base_y, w, up=True):
    ctx = f.ctx
    h = w * 0.8
    for dx in (-0.3, 0.3):
        line(ctx, [(x + dx * w * 0.8, base_y), (x, base_y - h - 40)], f.lw(7), hx("#6B4A35"))
    rrect(ctx, x - w / 2, base_y - h - 20, w, h * 0.8, 6)
    fill_stroke(ctx, "#FFFFFF", f.lw(6))
    pts = [(x - w * 0.38, base_y - h * 0.35), (x - w * 0.1, base_y - h * 0.5), (x + w * 0.1, base_y - h * 0.45),
           (x + w * 0.38, base_y - h * 0.85)]
    line(ctx, pts, f.lw(8), hx(PAL["money"] if up else PAL["loss"]))


def ledger(f, x, y, w, entries, n_vis, title="ORDER BOOK"):
    ctx = f.ctx
    h = w * 0.66
    for s in (-1, 1):
        px = x if s > 0 else x - w / 2
        rrect(ctx, px, y - h / 2, w / 2, h, 8)
        fill_stroke(ctx, "#FFFDF6", f.lw(7))
    rrect(ctx, x - w / 2 - 14, y - h / 2 - 14, w + 28, h + 28, 14)
    fill_stroke(ctx, None, f.lw(6))
    line(ctx, [(x, y - h / 2), (x, y + h / 2)], f.lw(6))
    text(ctx, title, x - w / 4, y - h * 0.36, w * 0.06, color=PAL["ink"], kind="marker")
    for i, e in enumerate(entries[:n_vis]):
        col = 0 if i < 6 else 1
        row = i % 6
        ex = x - w * 0.46 + col * w * 0.5
        ey = y - h * 0.20 + row * h * 0.11 + (h * 0.06 if col == 0 else -h * 0.12)
        text(ctx, e, ex, ey, w * 0.045, color="#2F5D8A", kind="hand", align="left", slant=0.1)


def slip(f, x, y, w, s, angle=0.0):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    rrect(ctx, -w / 2, -w * 0.22, w, w * 0.44, 4)
    fill_stroke(ctx, "#FFFBEA", f.lw(4))
    text(ctx, s, 0, w * 0.07, w * 0.14, color="#2F5D8A", kind="hand")
    ctx.restore()


def price_slider(f, x, y, w, pos, lo="$??", hi="$??", marker_c=PAL["money"]):
    ctx = f.ctx
    outlined_stroke(ctx, lambda c: (c.move_to(x - w / 2, y), c.line_to(x + w / 2, y)), hx("#DDE3EA"), f.lw(18), f.lw(5))
    text(ctx, lo, x - w / 2, y + 80, 56, color=PAL["paper"], kind="hand", stroke=PAL["ink"], stroke_px=f.lw(5))
    text(ctx, hi, x + w / 2, y + 80, 56, color=PAL["paper"], kind="hand", stroke=PAL["ink"], stroke_px=f.lw(5))
    mx = x - w / 2 + w * clamp(pos)
    poly(ctx, [(mx, y - 18), (mx - 28, y - 64), (mx + 28, y - 64)])
    fill_stroke(ctx, marker_c, f.lw(6))


def price_tag(f, x, y, w, s, angle=-0.15, color="#FFF4D6", fg=PAL["money_sh"], sub=None):
    ctx = f.ctx
    h = w * 0.5
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    ctx.move_to(-w / 2, -h / 2)
    ctx.line_to(w * 0.3, -h / 2)
    ctx.line_to(w / 2, 0)
    ctx.line_to(w * 0.3, h / 2)
    ctx.line_to(-w / 2, h / 2)
    ctx.close_path()
    fill_stroke(ctx, color, f.lw(7))
    circle(ctx, w * 0.30, 0, h * 0.10)
    fill_stroke(ctx, PAL["paper"], f.lw(5))
    text(ctx, s, -w * 0.08, h * 0.17, h * 0.55, color=fg, kind="marker")
    if sub:
        text(ctx, sub, -w * 0.08, h * 0.42, h * 0.18, color=PAL["ink"], kind="hand")
    ctx.restore()


def stamp(f, x, y, w, s, k=1.0, color=PAL["loss"], angle=-0.2):
    """Rubber-stamp word (pops with k)."""
    if k <= 0:
        return
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    ctx.scale(k, k)
    h = w * 0.32
    rrect(ctx, -w / 2, -h / 2, w, h, 10)
    set_color(ctx, color)
    ctx.set_line_width(f.lw(9))
    ctx.stroke()
    text(ctx, s, 0, h * 0.24, h * 0.62, color=color, kind="marker", tracking=0.08)
    ctx.restore()


def padlock(f, x, y, s=1.0, closed=1.0):
    ctx = f.ctx
    w, h = 120 * s, 100 * s
    lift = (1 - closed) * 40 * s
    ctx.new_path()
    ctx.arc(x, y - h * 0.5 - lift, w * 0.32, math.pi, 2 * math.pi)
    set_color(ctx, INK)
    ctx.set_line_width(f.lw(26 * s))
    ctx.stroke()
    ctx.new_path()
    ctx.arc(x, y - h * 0.5 - lift, w * 0.32, math.pi, 2 * math.pi)
    set_color(ctx, "#B8BCC6")
    ctx.set_line_width(f.lw(14 * s))
    ctx.stroke()
    shaded_shape(ctx, lambda c: rrect(c, x - w / 2, y - h / 2, w, h, 14 * s), PAL["gold"], w, f.lw(7), k=0.12)
    circle(ctx, x, y - 6 * s, 10 * s)
    fill_stroke(ctx, INK, 0)
    poly(ctx, [(x - 5 * s, y), (x + 5 * s, y), (x + 3 * s, y + 24 * s), (x - 3 * s, y + 24 * s)])
    set_color(ctx, INK)
    ctx.fill()


def chalkboard(f, x, y, w, h, lines, chars=None, size=72):
    ctx = f.ctx
    rrect(ctx, x - w / 2 - 22, y - h / 2 - 22, w + 44, h + 44, 14)
    fill_stroke(ctx, "#8A5A3A", f.lw(7))
    rrect(ctx, x - w / 2, y - h / 2, w, h, 6)
    fill_stroke(ctx, "#2E4A3E", f.lw(6))
    n = len(lines)
    used = 0
    for i, ln in enumerate(lines):
        c = None if chars is None else max(0, chars - used)
        yy = y - (n - 1) * size * 0.7 + i * size * 1.4 + size * 0.3
        col = "#F5F1E3" if not ln.startswith("=") else PAL["gold"]
        text(ctx, ln.lstrip("="), x, yy, size, color=col, kind="hand", chars=c, jitter=i + 1)
        used += len(ln.lstrip("="))


def money_tower(f, x, base_y, w, h, color="#7DBF73", label=None, top_label=None, label_c=PAL["paper"]):
    """Stack of banded bills (height h). Returns the top y."""
    ctx = f.ctx
    band = 26
    n = max(1, int(h / band))
    for i in range(n):
        yy = base_y - (i + 1) * band
        dx = math.sin(i * 2.3) * 4
        rrect(ctx, x - w / 2 + dx, yy, w, band, 5)
        fill_stroke(ctx, color if i % 2 else tint(color, 1.08), f.lw(5))
        rrect(ctx, x - w * 0.08 + dx, yy, w * 0.16, band, 2)
        fill_stroke(ctx, "#F2E6C9", f.lw(3))
    top = base_y - n * band
    if top_label:
        text(ctx, top_label, x, top - 26, 64, color=label_c, kind="marker", stroke=PAL["ink"], stroke_px=f.lw(6))
    if label:
        text(ctx, label, x, base_y + 64, 46, color=PAL["paper"], kind="hand", stroke=PAL["ink"], stroke_px=f.lw(5))
    return top


def pie(f, x, y, r, frac, base="#E8E3D6", slice_c=PAL["gold"], label=None, ghost=None, start=-math.pi / 2):
    """Pie with one highlighted slice of `frac`; optional dashed `ghost` fraction outline."""
    ctx = f.ctx
    circle(ctx, x, y, r)
    fill_stroke(ctx, base, f.lw(7))
    if frac > 0:
        ctx.move_to(x, y)
        ctx.arc(x, y, r, start, start + 2 * math.pi * frac)
        ctx.close_path()
        fill_stroke(ctx, slice_c, f.lw(7))
    if ghost:
        ctx.save()
        ctx.set_dash([18, 14])
        ctx.move_to(x, y)
        ctx.arc(x, y, r + 14, start, start + 2 * math.pi * ghost)
        ctx.close_path()
        set_color(ctx, INK)
        ctx.set_line_width(f.lw(5))
        ctx.stroke()
        ctx.restore()
    if label:
        a = start + math.pi * frac
        text(ctx, label, x + math.cos(a) * r * 0.62, y + math.sin(a) * r * 0.62 + 22, r * 0.2, color=PAL["paper"],
             kind="marker", stroke=PAL["ink"], stroke_px=f.lw(6))


def green_shoe(f, x, y, w, angle=-0.05):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    h = w * 0.55

    def sp(c):
        c.move_to(-w * 0.5, h * 0.3)
        c.curve_to(-w * 0.52, -h * 0.2, -w * 0.32, -h * 0.55, -w * 0.12, -h * 0.5)
        c.curve_to(0, -h * 0.2, w * 0.1, -h * 0.05, w * 0.32, 0)
        c.curve_to(w * 0.55, h * 0.05, w * 0.55, h * 0.3, w * 0.45, h * 0.32)
        c.close_path()
    shaded_shape(ctx, sp, "#4FAE5A", w, f.lw(8), k=0.15)
    rrect(ctx, -w * 0.55, h * 0.26, w * 1.06, h * 0.16, 8)
    fill_stroke(ctx, "#F3F3F3", f.lw(7))
    for i in range(3):
        line(ctx, [(-w * 0.22 + i * w * 0.08, -h * 0.30 + i * h * 0.1), (-w * 0.05 + i * w * 0.08, -h * 0.25 + i * h * 0.1)],
             f.lw(5), hx("#F3F3F3"))
    ctx.restore()


def ballot_box(f, x, base_y, w):
    ctx = f.ctx
    h = w * 0.8
    _box(f, x - w / 2, base_y - h, w, h, "#D9DEE6", r=10)
    rrect(ctx, x - w * 0.3, base_y - h + 14, w * 0.6, 16, 6)
    fill_stroke(ctx, INK, f.lw(4))
    text(ctx, "VOTES", x, base_y - h * 0.38, w * 0.16, color=PAL["ink"], kind="marker", tracking=0.08)
    return (x, base_y - h + 22)


def ballot(f, x, y, w, angle=0.0):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    rrect(ctx, -w / 2, -w * 0.32, w, w * 0.64, 4)
    fill_stroke(ctx, PAL["paper"], f.lw(4))
    line(ctx, [(-w * 0.32, 0), (-w * 0.2, w * 0.12), (w * 0.05, -w * 0.16)], f.lw(6), hx(PAL["money"]))
    ctx.restore()


def bell(f, x, y, s=1.0, swing=0.0):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(swing)
    w = 220 * s

    def bp(c):
        c.move_to(-w * 0.12, -w * 0.5)
        c.curve_to(-w * 0.42, -w * 0.45, -w * 0.38, w * 0.05, -w * 0.5, w * 0.25)
        c.line_to(w * 0.5, w * 0.25)
        c.curve_to(w * 0.38, w * 0.05, w * 0.42, -w * 0.45, w * 0.12, -w * 0.5)
        c.close_path()
    shaded_shape(ctx, bp, PAL["gold"], w, f.lw(8), k=0.2)
    circle(ctx, 0, w * 0.33, w * 0.08)
    fill_stroke(ctx, PAL["gold_sh"], f.lw(6))
    circle(ctx, 0, -w * 0.55, w * 0.07)
    fill_stroke(ctx, PAL["gold"], f.lw(6))
    ctx.restore()


def popcorn(f, x, y, s=1.0, popped=0.0):
    """Kernel (popped=0) -> fluffy popcorn (popped=1)."""
    ctx = f.ctx
    if popped < 0.5:
        ellipse(ctx, x, y, 40 * s, 52 * s)
        fill_stroke(ctx, "#F2B630", f.lw(7))
        ellipse(ctx, x - 10 * s, y - 14 * s, 10 * s, 16 * s)
        set_color(ctx, "#FFE29A")
        ctx.fill()
        return
    k = 0.6 + 0.4 * ease_out((popped - 0.5) / 0.5)
    for (dx, dy, r) in ((-60, 10, 70), (55, 15, 72), (0, -50, 80), (-35, 60, 60), (40, 65, 58), (0, 20, 70)):
        circle(ctx, x + dx * s * k, y + dy * s * k, r * s * k)
        fill_stroke(ctx, "#FFF8E6", f.lw(7))
    ellipse(ctx, x + 10 * s, y + 85 * s * k, 30 * s, 20 * s)
    fill_stroke(ctx, "#F2B630", f.lw(5))


def paddle(f, x, y, s, n):
    ctx = f.ctx
    line(ctx, [(x, y), (x, y + 70 * s)], f.lw(8), hx("#6B4A35"))
    circle(ctx, x, y - 20 * s, 42 * s)
    fill_stroke(ctx, PAL["paper"], f.lw(6))
    text(ctx, str(n), x, y - 6 * s, 40 * s, color=PAL["ink"], kind="marker")


def weight(f, x, y, s, num, label=None, color="#3A3D45"):
    """Kettlebell-style weight with a number. (x, y) = centre of the body."""
    ctx = f.ctx
    r = 90 * s
    ctx.new_path()
    ctx.arc(x, y - r * 0.95, r * 0.45, math.pi, 2 * math.pi)
    set_color(ctx, INK)
    ctx.set_line_width(f.lw(30 * s))
    ctx.stroke()
    ctx.new_path()
    ctx.arc(x, y - r * 0.95, r * 0.45, math.pi, 2 * math.pi)
    set_color(ctx, color)
    ctx.set_line_width(f.lw(16 * s))
    ctx.stroke()

    def wp(c):
        c.move_to(x - r * 0.7, y - r * 0.75)
        c.line_to(x + r * 0.7, y - r * 0.75)
        c.curve_to(x + r * 1.15, y - r * 0.2, x + r * 1.05, y + r * 0.8, x, y + r * 0.85)
        c.curve_to(x - r * 1.05, y + r * 0.8, x - r * 1.15, y - r * 0.2, x - r * 0.7, y - r * 0.75)
        c.close_path()
    shaded_shape(ctx, wp, color, r * 2, f.lw(8), k=0.18)
    text(ctx, str(num), x, y + r * 0.35, r * 0.9, color=PAL["paper"], kind="marker", stroke=PAL["ink"], stroke_px=f.lw(5))
    if label:
        text(ctx, label, x, y + r * 1.55, 52 * s, color=PAL["paper"], kind="marker", stroke=PAL["ink"], stroke_px=f.lw(6))
    return (x, y - r * 1.4)


def chain(f, x0, y0, x1, y1, link=26):
    ctx = f.ctx
    L = math.dist((x0, y0), (x1, y1))
    n = max(1, int(L / link))
    ang = math.atan2(y1 - y0, x1 - x0)
    for i in range(n):
        cx, cy = lerp(x0, x1, (i + 0.5) / n), lerp(y0, y1, (i + 0.5) / n)
        ctx.save()
        ctx.translate(cx, cy)
        ctx.rotate(ang + (math.pi / 2 if i % 2 else 0))
        ellipse(ctx, 0, 0, link * 0.62, link * 0.32)
        set_color(ctx, INK)
        ctx.set_line_width(f.lw(9))
        ctx.stroke()
        ellipse(ctx, 0, 0, link * 0.62, link * 0.32)
        set_color(ctx, "#9EA3AE")
        ctx.set_line_width(f.lw(4))
        ctx.stroke()
        ctx.restore()


def contract(f, x, y, w, title="AGREEMENT", signed=0.0, sub=None):
    ctx = f.ctx
    h = w * 1.25
    rrect(ctx, x - w / 2, y - h / 2, w, h, 8)
    fill_stroke(ctx, "#FFFDF6", f.lw(7))
    text(ctx, title, x, y - h * 0.36, w * 0.09, color=PAL["ink"], kind="marker", tracking=0.06)
    if sub:
        text(ctx, sub, x, y - h * 0.24, w * 0.08, color=PAL["loss_sh"], kind="marker")
    for k in range(6):
        yy = y - h * 0.12 + k * h * 0.07
        line(ctx, [(x - w * 0.38, yy), (x + w * 0.38, yy)], f.lw(3), hx("#C9C3B6"))
    line(ctx, [(x - w * 0.38, y + h * 0.36), (x + w * 0.1, y + h * 0.36)], f.lw(3))
    if signed > 0:
        pts = [(x - w * 0.36 + i * w * 0.04, y + h * 0.33 + math.sin(i * 1.3) * 12) for i in range(int(12 * signed) + 1)]
        if len(pts) > 1:
            line(ctx, pts, f.lw(5), hx("#2F5D8A"))
    return (x - w * 0.36 + w * 0.48 * signed, y + h * 0.33)


def pen(f, x, y, s=1.0, angle=0.6):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    rrect(ctx, -10 * s, -130 * s, 20 * s, 120 * s, 6)
    fill_stroke(ctx, "#2F5D8A", f.lw(5))
    poly(ctx, [(-10 * s, -10 * s), (10 * s, -10 * s), (0, 12 * s)])
    fill_stroke(ctx, "#F3F3F3", f.lw(4))
    ctx.restore()


def knife(f, x, y, s=1.0, angle=0.0):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    poly(ctx, [(0, 0), (240 * s, -8 * s), (240 * s, 34 * s), (20 * s, 30 * s)])
    fill_stroke(ctx, "#DDE1E8", f.lw(6))
    rrect(ctx, 236 * s, -6 * s, 120 * s, 40 * s, 12)
    fill_stroke(ctx, "#6B4A35", f.lw(6))
    ctx.restore()


def suitcase(f, x, base_y, w, color="#8C5B3E", locked=True):
    ctx = f.ctx
    h = w * 0.7
    rrect(ctx, x - w * 0.18, base_y - h - 26, w * 0.36, 36, 10)
    set_color(ctx, INK)
    ctx.set_line_width(f.lw(9))
    ctx.stroke()
    _box(f, x - w / 2, base_y - h, w, h, color, r=12, k=0.12)
    for dx in (-0.3, 0.3):
        line(ctx, [(x + dx * w, base_y - h), (x + dx * w, base_y)], f.lw(5))
    if locked:
        padlock(f, x, base_y - h * 0.45, 0.42)


def dam(f, x0, x1, base_y, h, open_p=0.0, t=0.0, water_h=None):
    """Concrete dam wall with a gate; open_p releases a (small) flow."""
    ctx = f.ctx
    W_ = x1 - x0
    water_h = water_h or h * 0.85
    ctx.rectangle(x0 - 400, base_y - water_h, 400, water_h)
    set_color(ctx, "#4C8EC0")
    ctx.fill()
    for k in range(4):
        yy = base_y - water_h + 22 + k * 40 + math.sin(t * 2 + k) * 4
        line(ctx, [(x0 - 380, yy), (x0 - 40, yy)], f.lw(3), hx("#8CC3E8"))
    shaded_shape(ctx, lambda c: poly(c, [(x0, base_y - h), (x1 - W_ * 0.25, base_y - h), (x1, base_y), (x0, base_y)]),
                 "#B9B7B0", W_, f.lw(8), k=0.1)
    gx, gy = x0 + W_ * 0.42, base_y - h * 0.38
    rrect(ctx, gx - 60, gy - 40 - open_p * 60, 120, 120, 6)
    fill_stroke(ctx, "#6E6C66", f.lw(6))
    if open_p > 0:
        n = 3
        for i in range(n):
            ph = (t * 1.5 + i / n) % 1.0
            xx = gx + 60 + ph * 260
            yy = gy + 40 + ph ** 2 * (base_y - gy - 40)
            ellipse(ctx, xx, yy, 18 * open_p + 6, 12)
            fill_stroke(ctx, "#6FB3E3", f.lw(4))
    return (gx, gy)


def report_card(f, x, y, w, rows, grade=None, grade_k=0.0, title="REPORT CARD"):
    ctx = f.ctx
    h = w * 1.2
    rrect(ctx, x - w / 2, y - h / 2, w, h, 12)
    fill_stroke(ctx, "#FFFDF6", f.lw(8))
    rrect(ctx, x - w / 2, y - h / 2, w, h * 0.14, 12)
    fill_stroke(ctx, "#2F5D8A", f.lw(8))
    text(ctx, title, x, y - h / 2 + h * 0.1, h * 0.07, color=PAL["paper"], kind="marker", tracking=0.08)
    for i, (lab, val, col) in enumerate(rows):
        yy = y - h * 0.22 + i * h * 0.15
        text(ctx, lab, x - w * 0.42, yy, h * 0.06, color=PAL["ink"], kind="hand", align="left")
        text(ctx, val, x + w * 0.42, yy, h * 0.07, color=col, kind="marker", align="right")
        line(ctx, [(x - w * 0.42, yy + 18), (x + w * 0.42, yy + 18)], f.lw(2), hx("#D5CFC2"))
    if grade and grade_k > 0:
        stamp(f, x + w * 0.22, y + h * 0.36, w * 0.5, grade, grade_k, color=PAL["money_sh"] if "A" in grade else PAL["loss"])


def receipt(f, x, top_y, w, unroll, lines, total, highlight=None, max_h=900):
    """Receipt that unrolls downward (unroll 0..1). highlight = index of a line to mark."""
    ctx = f.ctx
    h = max(80, max_h * clamp(unroll))
    ctx.move_to(x - w / 2, top_y)
    ctx.line_to(x + w / 2, top_y)
    ctx.line_to(x + w / 2, top_y + h)
    for i in range(10, -1, -1):
        ctx.line_to(x - w / 2 + w * i / 10, top_y + h + (14 if i % 2 else 0))
    ctx.close_path()
    fill_stroke(ctx, "#FFFFFF", f.lw(6))
    for i, (lab, val) in enumerate(lines):
        yy = top_y + 70 + i * 74
        if yy > top_y + h - 30:
            break
        if highlight == i:
            rrect(ctx, x - w * 0.46, yy - 44, w * 0.92, 62, 8)
            set_color(ctx, "#FFE07A", 0.8)
            ctx.fill()
        text(ctx, lab, x - w * 0.42, yy, 44, color=PAL["ink"], kind="hand", align="left")
        text(ctx, val, x + w * 0.42, yy, 44, color=PAL["ink"], kind="hand", align="right")
    if top_y + h - 60 > top_y + 70 + len(lines) * 74:
        line(ctx, [(x - w * 0.42, top_y + h - 100), (x + w * 0.42, top_y + h - 100)], f.lw(3))
        text(ctx, total, x, top_y + h - 40, 60, color=PAL["loss_sh"], kind="marker")


def fuel_tank(f, x, base_y, w, h, label, fill_k=1.0):
    ctx = f.ctx
    _box(f, x - w / 2, base_y - h, w, h, "#DADFE8", r=w * 0.4, k=0.14)
    lvl = h * 0.9 * clamp(fill_k)
    ctx.save()
    rrect(ctx, x - w / 2 + 10, base_y - h + 10, w - 20, h - 20, w * 0.38)
    ctx.clip()
    ctx.rectangle(x - w / 2, base_y - 10 - lvl, w, lvl)
    set_color(ctx, "#F2B630")
    ctx.fill()
    ctx.restore()
    text(ctx, label, x, base_y - h / 2 + 20, w * 0.16, color=PAL["paper"], kind="marker", stroke=PAL["ink"],
         stroke_px=f.lw(6))


def planet(f, x, y, r, color="#D2693C", bands=True):
    ctx = f.ctx
    shaded_shape(ctx, lambda c: circle(c, x, y, r), color, r * 2, f.lw(8), k=0.22)
    if bands:
        for (dx, dy, rr) in ((-0.3, -0.25, 0.14), (0.25, 0.2, 0.18), (-0.1, 0.45, 0.1)):
            circle(ctx, x + dx * r, y + dy * r, rr * r)
            fill_stroke(ctx, shade(color, 0.85), f.lw(4))


def satellite(f, x, y, s=1.0, angle=0.3):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    for sx in (-1, 1):
        rrect(ctx, sx * 70 * s - 55 * s, -26 * s, 110 * s, 52 * s, 4)
        fill_stroke(ctx, "#3D6FB0", f.lw(5))
        for k in range(3):
            line(ctx, [(sx * 70 * s - 55 * s + (k + 1) * 27 * s, -26 * s), (sx * 70 * s - 55 * s + (k + 1) * 27 * s, 26 * s)],
                 f.lw(2), hx("#9CC3E8"))
    shaded_shape(ctx, lambda c: rrect(c, -26 * s, -34 * s, 52 * s, 68 * s, 8), "#D9DAE6", 60 * s, f.lw(6), k=0.2)
    ctx.restore()


def server_rack(f, x, base_y, w, h, t=0.0, seed=0):
    ctx = f.ctx
    _box(f, x - w / 2, base_y - h, w, h, "#2B3340", r=8, k=0.08)
    n = int(h / 46)
    for i in range(n):
        yy = base_y - h + 14 + i * 46
        rrect(ctx, x - w / 2 + 12, yy, w - 24, 34, 4)
        fill_stroke(ctx, "#1B222C", f.lw(3))
        for k in range(3):
            on = math.sin(t * (3 + k) + i * 1.7 + seed + k) > 0
            circle(ctx, x - w / 2 + 34 + k * 22, yy + 17, 6)
            set_color(ctx, "#5CE07A" if on else "#2F5D4A")
            ctx.fill()


def cheque(f, x, y, w, amount="$???", payee="SPACEX"):
    ctx = f.ctx
    h = w * 0.45
    rrect(ctx, x - w / 2, y - h / 2, w, h, 10)
    fill_stroke(ctx, "#E8F4E4", f.lw(7))
    text(ctx, "PAY TO: " + payee, x - w * 0.42, y - h * 0.18, h * 0.13, color=PAL["ink"], kind="hand", align="left")
    rrect(ctx, x + w * 0.08, y - h * 0.08, w * 0.36, h * 0.3, 6)
    fill_stroke(ctx, "#FFFFFF", f.lw(4))
    text(ctx, amount, x + w * 0.26, y + h * 0.14, h * 0.2, color=PAL["money_sh"], kind="marker")
    line(ctx, [(x - w * 0.42, y + h * 0.3), (x - w * 0.02, y + h * 0.3)], f.lw(3))


def big_arrow(f, x, y, length, angle, color=PAL["loss"], width=70):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    poly(ctx, [(0, -width * 0.3), (length - width, -width * 0.3), (length - width, -width * 0.7), (length, 0),
               (length - width, width * 0.7), (length - width, width * 0.3), (0, width * 0.3)])
    fill_stroke(ctx, color, f.lw(7))
    ctx.restore()


def balance_scale(f, x, base_y, w, tilt, left=None, right=None):
    """tilt > 0 = right pan lower. left/right = callables(f, px, py) drawing on each pan."""
    ctx = f.ctx
    h = w * 0.75
    poly(ctx, [(x - 90, base_y), (x + 90, base_y), (x + 20, base_y - 40), (x - 20, base_y - 40)])
    fill_stroke(ctx, PAL["gold_sh"], f.lw(7))
    rrect(ctx, x - 14, base_y - h, 28, h - 30, 8)
    fill_stroke(ctx, PAL["gold"], f.lw(6))
    ang = tilt * 0.22
    px = math.cos(ang) * w / 2
    py = math.sin(ang) * w / 2
    top = base_y - h
    line(ctx, [(x - px, top - py), (x + px, top + py)], f.lw(22))
    line(ctx, [(x - px, top - py), (x + px, top + py)], f.lw(10), hx(PAL["gold"]))
    circle(ctx, x, top, 20)
    fill_stroke(ctx, PAL["gold"], f.lw(6))
    for s, fn in ((-1, left), (1, right)):
        ax, ay = x + s * px, top + s * py
        line(ctx, [(ax, ay), (ax - 70, ay + 170)], f.lw(4))
        line(ctx, [(ax, ay), (ax + 70, ay + 170)], f.lw(4))
        ctx.new_path()
        ctx.arc(ax, ay + 170, 110, 0, math.pi)
        ctx.close_path()
        fill_stroke(ctx, PAL["gold"], f.lw(6))
        if fn:
            fn(f, ax, ay + 168)


def factory(f, x, base_y, w, h, built=1.0, t=0.0):
    ctx = f.ctx
    hh = h * clamp(built)
    _box(f, x - w / 2, base_y - hh, w, hh, "#8C95A3", r=6, k=0.1)
    for i in range(3):
        cx = x - w * 0.3 + i * w * 0.3
        rrect(ctx, cx - 26, base_y - hh - h * 0.35, 52, h * 0.35, 4)
        fill_stroke(ctx, "#6E7683", f.lw(6))
    for i in range(4):
        rrect(ctx, x - w * 0.4 + i * w * 0.21, base_y - hh * 0.6, w * 0.13, hh * 0.25, 4)
        fill_stroke(ctx, "#FFE07A" if math.sin(t * 2 + i) > -0.3 else "#C9B45A", f.lw(4))
    if built < 1:  # scaffold
        for i in range(6):
            line(ctx, [(x - w / 2 + i * w / 5, base_y), (x - w / 2 + i * w / 5, base_y - h)], f.lw(4), hx("#C98A12"))
        for j in range(4):
            line(ctx, [(x - w / 2, base_y - j * h / 3), (x + w / 2, base_y - j * h / 3)], f.lw(4), hx("#C98A12"))


def lemonade_stand(f, x, base_y, w):
    ctx = f.ctx
    h = w * 0.7
    _box(f, x - w / 2, base_y - h * 0.55, w, h * 0.55, "#F7D86A", r=8)
    text(ctx, "LEMONADE", x, base_y - h * 0.22, w * 0.15, color=PAL["ink"], kind="marker")
    for s in (-1, 1):
        line(ctx, [(x + s * w * 0.45, base_y - h * 0.55), (x + s * w * 0.45, base_y - h * 1.05)], f.lw(7))
    poly(ctx, [(x - w * 0.58, base_y - h), (x + w * 0.58, base_y - h), (x + w * 0.5, base_y - h * 1.2),
               (x - w * 0.5, base_y - h * 1.2)])
    fill_stroke(ctx, "#F07CC0", f.lw(7))


def exit_door(f, x, base_y, w, h, label="EXIT", locked=True):
    ctx = f.ctx
    rrect(ctx, x - w / 2 - 18, base_y - h - 18, w + 36, h + 18, 8)
    fill_stroke(ctx, "#3A3436", f.lw(7))
    _box(f, x - w / 2, base_y - h, w, h, "#7FA35A", r=4, k=0.06)
    rrect(ctx, x - w * 0.35, base_y - h - 90, w * 0.7, 64, 10)
    fill_stroke(ctx, "#2E9C4A", f.lw(6))
    text(ctx, label, x, base_y - h - 42, 44, color=PAL["paper"], kind="marker", tracking=0.1)
    if locked:
        for dy in (-0.15, 0.15):
            line(ctx, [(x - w * 0.6, base_y - h * (0.5 + dy) - 20), (x + w * 0.6, base_y - h * (0.5 - dy) + 20)], f.lw(16))
            line(ctx, [(x - w * 0.6, base_y - h * (0.5 + dy) - 20), (x + w * 0.6, base_y - h * (0.5 - dy) + 20)], f.lw(8),
                 hx("#9EA3AE"))
        padlock(f, x, base_y - h * 0.5, 0.8)


def glass_rocket(f, x, y, size, crack=0.0, angle=0.0):
    from .props import rocket
    ctx = f.ctx
    rocket(f, x, y, size, angle=angle, body="#CFEFFF", fin="#8FD3F0")
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(angle)
    # glints
    line(ctx, [(-size * 0.06, -size * 0.35), (-size * 0.1, -size * 0.05)], f.lw(6), hx("#FFFFFF"))
    if crack > 0:
        pts = [(size * 0.02, -size * 0.30), (-size * 0.04, -size * 0.16), (size * 0.06, -size * 0.04),
               (-size * 0.05, size * 0.10), (size * 0.04, size * 0.24), (-size * 0.02, size * 0.36)]
        n = max(2, int(len(pts) * clamp(crack)))
        line(ctx, pts[:n], f.lw(5))
        if crack > 0.6:
            line(ctx, [pts[2], (size * 0.13, size * 0.02)], f.lw(4))
            line(ctx, [pts[3], (-size * 0.12, size * 0.16)], f.lw(4))
    ctx.restore()


def whiteboard(f, x, y, w, h):
    ctx = f.ctx
    rrect(ctx, x - w / 2 - 16, y - h / 2 - 16, w + 32, h + 32, 12)
    fill_stroke(ctx, "#B9BEC8", f.lw(7))
    rrect(ctx, x - w / 2, y - h / 2, w, h, 6)
    fill_stroke(ctx, "#FFFFFF", f.lw(5))


def counter_number(f, x, y, size, value, color=PAL["gold"]):
    text(f.ctx, value, x, y, size, color=color, kind="marker", stroke=PAL["ink"], stroke_px=f.lw(7))
