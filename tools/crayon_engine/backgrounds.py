"""Backgrounds: one dominant hue per location, 3 value bands, radial elliptical spotlight,
atmospheric shafts. Flat vector bands (no smooth gradients), like the reference."""
from __future__ import annotations

import math
import random

from .core import PAL, W, H, hx, mix
from .draw import INK, ellipse, fill_stroke, line, poly, rrect, set_color

M = 260  # margin drawn beyond the stage so camera shake never shows an edge


def fill_all(ctx, c):
    ctx.rectangle(-M, -M, W + 2 * M, H + 2 * M)
    set_color(ctx, c)
    ctx.fill()


def radial_spot(ctx, cx, cy, rx, ry, outer, inner, n=6):
    """Concentric flat ellipses from `outer` to `inner` (subject sits in the brightest one)."""
    for i in range(n):
        k = i / (n - 1)
        s = 1.0 - 0.78 * k
        ellipse(ctx, cx, cy, rx * s, ry * s)
        set_color(ctx, mix(outer, inner, k))
        ctx.fill()


def white_void(f, floor=True, disc_y=860, disc_rx=520):
    ctx = f.ctx
    fill_all(ctx, PAL["paper"])
    if floor:
        ellipse(ctx, W / 2, disc_y, disc_rx, disc_rx * 0.16)
        set_color(ctx, "#E9E9EC")
        ctx.fill()


def black(f):
    fill_all(f.ctx, "#000000")


def gold_radial(f, cx=W / 2, cy=H * 0.48):
    ctx = f.ctx
    fill_all(ctx, "#B8860B")
    radial_spot(ctx, cx, cy, 1250, 820, "#C99419", "#F8DA86", n=7)


def night_grid(f):
    ctx = f.ctx
    fill_all(ctx, "#0F2233")
    radial_spot(ctx, W * 0.55, H * 0.45, 1300, 760, "#0F2233", "#1A3D57", n=5)


def crisis_desk(f, seed=2):
    ctx = f.ctx
    fill_all(ctx, "#3E3E40")
    # diagonal stripe pattern (crisis grey)
    ctx.save()
    set_color(ctx, "#454547")
    for i in range(-20, 40):
        x0 = i * 90
        poly(ctx, [(x0, -M), (x0 + 40, -M), (x0 + 40 - H - 2 * M, H + M), (x0 - H - 2 * M, H + M)])
        ctx.fill()
    ctx.restore()
    radial_spot(ctx, W / 2, H * 0.46, 1050, 640, "#3E3E40", "#6A6A6E", n=6)
    # desk top
    ctx.rectangle(-M, H * 0.80, W + 2 * M, H * 0.2 + M)
    set_color(ctx, "#2A2A2C")
    ctx.fill()
    line(ctx, [(-M, H * 0.80), (W + M, H * 0.80)], f.lw(6))


def club_red(f, spot=(W / 2, H * 0.50)):
    ctx = f.ctx
    fill_all(ctx, "#5E1E20")
    radial_spot(ctx, spot[0], spot[1], 1150, 700, "#5E1E20", "#BC5A4E", n=7)
    # curtains at the sides
    for side in (-1, 1):
        for k in range(5):
            x = (0 if side < 0 else W) - side * (k * 46)
            poly(ctx, [(x, -M), (x - side * 60, -M), (x - side * (40 + k * 8), H + M), (x + side * 12, H + M)])
            set_color(ctx, "#7C2426" if k % 2 else "#681C1E")
            ctx.fill()
    # floor
    ctx.rectangle(-M, H * 0.83, W + 2 * M, H)
    set_color(ctx, "#4A1517")
    ctx.fill()
    line(ctx, [(-M, H * 0.83), (W + M, H * 0.83)], f.lw(6))


def market_hall(f):
    ctx = f.ctx
    fill_all(ctx, "#3F8FB5")
    radial_spot(ctx, W / 2, H * 0.55, 1250, 700, "#3F8FB5", "#9FD2E2", n=6)
    # columns
    for i, x in enumerate((140, 470, 1450, 1780)):
        rrect(ctx, x - 60, 150, 120, 720, 6)
        fill_stroke(ctx, "#D6EAF1", f.lw(6))
        rrect(ctx, x - 80, 130, 160, 40, 6)
        fill_stroke(ctx, "#BFDCE8", f.lw(6))
        line(ctx, [(x - 25, 190), (x - 25, 850)], f.lw(3), hx("#A9CCDA"))
        line(ctx, [(x + 25, 190), (x + 25, 850)], f.lw(3), hx("#A9CCDA"))
    ctx.rectangle(-M, H * 0.80, W + 2 * M, H)
    set_color(ctx, "#2F6E8C")
    ctx.fill()
    line(ctx, [(-M, H * 0.80), (W + M, H * 0.80)], f.lw(6))


def blue_wall(f):
    ctx = f.ctx
    fill_all(ctx, "#2E5E78")
    radial_spot(ctx, W / 2, H * 0.48, 1100, 680, "#2E5E78", "#4B88A6", n=5)
    ctx.rectangle(-M, H * 0.86, W + 2 * M, H)
    set_color(ctx, "#1E3F52")
    ctx.fill()
    line(ctx, [(-M, H * 0.86), (W + M, H * 0.86)], f.lw(6))


def launch_pad_night(f, seed=7, searchlights=1.0, t=0.0):
    """Launch pad at night: blue-violet sky bands, stars, tower, rocket, two searchlights in a 'V'."""
    ctx = f.ctx
    bands = ["#1E2448", "#2A3060", "#383E78", "#4A4E8C"]
    fill_all(ctx, bands[0])
    for i, c in enumerate(bands[1:], 1):
        ctx.rectangle(-M, H * (0.18 * i) - 20, W + 2 * M, H)
        set_color(ctx, c)
        ctx.fill()
    rnd = random.Random(seed)
    for _ in range(70):
        x, y = rnd.uniform(-M, W + M), rnd.uniform(-M, H * 0.55)
        tw = 0.55 + 0.45 * math.sin(t * 2.0 + x)
        ellipse(ctx, x, y, 2.2, 2.2)
        set_color(ctx, "#E8E6FF", 0.35 + 0.4 * tw)
        ctx.fill()
    # searchlights crossing in a V behind the stage
    for side, ph in ((-1, 0.0), (1, 1.3)):
        sway = math.sin(t * 0.6 + ph) * 0.05
        ox = W / 2 + side * 520
        ang = -math.pi / 2 - side * (0.32 + sway)
        L = 1500
        tipx, tipy = ox + math.cos(ang) * L, H * 0.80 + math.sin(ang) * L
        nx, ny = -math.sin(ang), math.cos(ang)
        poly(ctx, [(ox - 18 * nx, H * 0.80 - 18 * ny), (ox + 18 * nx, H * 0.80 + 18 * ny),
                   (tipx + 160 * nx, tipy + 160 * ny), (tipx - 160 * nx, tipy - 160 * ny)])
        set_color(ctx, "#FFF3C9", 0.13 * searchlights)
        ctx.fill()
    # launch tower (left) + rocket on pad (background, desaturated)
    tx = W * 0.30
    for xx in (tx - 45, tx + 45):
        line(ctx, [(xx, H * 0.78), (xx, H * 0.16)], f.lw(5), hx("#5A5D7E"))
    for k in range(13):
        y0 = H * 0.78 - k * 48
        line(ctx, [(tx - 45, y0), (tx + 45, y0 - 48)], f.lw(3), hx("#5A5D7E"))
        line(ctx, [(tx + 45, y0), (tx - 45, y0 - 48)], f.lw(3), hx("#5A5D7E"))
    from .props import rocket
    rocket(f, W * 0.36, H * 0.47, 520, body="#D9DAE6", fin="#9A4A63")
    # ground + stage
    ctx.rectangle(-M, H * 0.78, W + 2 * M, H)
    set_color(ctx, "#2E3060")
    ctx.fill()
    line(ctx, [(-M, H * 0.78), (W + M, H * 0.78)], f.lw(5))
    radial_spot(ctx, W / 2, H * 0.86, 560, 120, "#3A3C70", "#F0D37A", n=6)


def card(f, color="#000000"):
    fill_all(f.ctx, color)


def vignette(f, strength=0.22):
    """Flat vignette: dark frame bands at the edges (cheap, no gradients)."""
    ctx = f.ctx
    for i, a in enumerate((strength * 0.35, strength * 0.6, strength)):
        pad = 70 - i * 25
        ctx.rectangle(-M, -M, W + 2 * M, H + 2 * M)
        ctx.new_sub_path()
        ellipse(ctx, W / 2, H / 2, W * (0.75 - i * 0.04) + pad, H * (0.80 - i * 0.04) + pad)
        ctx.set_fill_rule(1)
        set_color(ctx, INK, a * 0.5)
        ctx.fill()
        ctx.set_fill_rule(0)


def light_shaft(f, x0, x1, top, bottom, spread=260, alpha=0.14, color="#FFFFFF"):
    ctx = f.ctx
    poly(ctx, [(x0, top), (x1, top), (x1 + spread, bottom), (x0 + spread * 0.4, bottom)])
    set_color(ctx, color, alpha)
    ctx.fill()
