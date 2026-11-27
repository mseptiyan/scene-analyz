"""Effects animated straight-ahead *on ones* (every frame): confetti, money rain, sparkles,
speed lines. Deterministic: each particle's state is a closed-form function of time + seed,
so any frame can be rendered independently (parallel workers, QC stills)."""
from __future__ import annotations

import math
import random

from .core import PAL, W, H, hx
from .draw import INK, ellipse, fill_stroke, line, poly, rrect, set_color

CONFETTI = ["#F2B630", "#D9363E", "#4FAE5A", "#3FA9E0", "#F07CC0", "#FFFFFF", "#9B6CE0"]


def _parts(seed, n):
    rnd = random.Random(seed)
    return [(rnd.random(), rnd.random(), rnd.random(), rnd.random(), rnd.random(), rnd.random()) for _ in range(n)]


def confetti(f, t, n=150, seed=11, x0=-100, x1=W + 100, top=-120, fall=(170, 320), density=1.0, t_start=0.0):
    """Paper confetti falling with sway and 3D twirl (x-scale by cos)."""
    ctx = f.ctx
    tt = t - t_start
    if tt < 0:
        return
    for i, (a, b, c, d, e, g) in enumerate(_parts(seed, int(n * density))):
        vy = fall[0] + (fall[1] - fall[0]) * b
        delay = c * 2.4
        if tt < delay:
            continue
        y = top + (tt - delay) * vy
        if y > H + 60:
            # recycle so the shower stays continuous
            cyc = (H + 60 - top) / vy
            y = top + ((tt - delay) % cyc) * vy
        x = x0 + (x1 - x0) * a + math.sin(tt * (1.2 + 1.5 * d) + e * 6.28) * (18 + 40 * g)
        rot = tt * (2 + 4 * d) + e * 6.28
        flip = math.cos(tt * (5 + 6 * g) + a * 9)
        ctx.save()
        ctx.translate(x, y)
        ctx.rotate(rot)
        ctx.scale(max(abs(flip), 0.15), 1)
        rrect(ctx, -7, -11, 14, 22, 2)
        set_color(ctx, CONFETTI[i % len(CONFETTI)])
        ctx.fill_preserve()
        set_color(ctx, INK)
        ctx.set_line_width(f.lw(2))
        ctx.stroke()
        ctx.restore()


def money_rain(f, t, n=40, seed=5, x0=0, x1=W, top=-140, fall=(150, 260), t_start=0.0, w=86):
    from .props import bill
    tt = t - t_start
    if tt < 0:
        return
    for i, (a, b, c, d, e, g) in enumerate(_parts(seed, n)):
        vy = fall[0] + (fall[1] - fall[0]) * b
        delay = c * 1.6
        if tt < delay:
            continue
        y = top + (tt - delay) * vy
        cyc = (H + 120 - top) / vy
        y = top + ((tt - delay) % cyc) * vy
        x = x0 + (x1 - x0) * a + math.sin(tt * (0.9 + d) + e * 6.28) * (30 + 50 * g)
        ang = math.sin(tt * (1.4 + d) + e * 3) * 0.6
        flip = math.cos(tt * (2.5 + 3 * g) + a * 5)
        bill(f, x, y, w * (0.8 + 0.3 * g), angle=ang, flip=flip)


def sparkle(f, x, y, r, t, phase=0.0, color="#FFF6C8"):
    ctx = f.ctx
    k = 0.6 + 0.4 * math.sin(t * 6 + phase)
    rr = r * k
    poly(ctx, [(x, y - rr), (x + rr * 0.22, y - rr * 0.22), (x + rr, y), (x + rr * 0.22, y + rr * 0.22),
               (x, y + rr), (x - rr * 0.22, y + rr * 0.22), (x - rr, y), (x - rr * 0.22, y - rr * 0.22)])
    fill_stroke(ctx, color, f.lw(3))


def speed_lines(f, x, y, ang, n=5, length=120, spread=60, t=0.0, color=PAL["paper"]):
    ctx = f.ctx
    for i in range(n):
        off = (i - (n - 1) / 2) * spread / max(1, n - 1)
        jitter = (math.sin(t * 30 + i * 1.7) * 0.5 + 0.5) * 0.4
        L = length * (0.6 + jitter)
        nx, ny = -math.sin(ang), math.cos(ang)
        sx, sy = x + nx * off, y + ny * off
        ex, ey = sx - math.cos(ang) * L, sy - math.sin(ang) * L
        line(ctx, [(sx, sy), (ex, ey)], f.lw(5), hx(color), 0.85)


def exclaim(f, x, y, size=70, s="!!", color=PAL["loss"]):
    from .text import text
    text(f.ctx, s, x, y, size, color=color, kind="marker", stroke=PAL["ink"], stroke_px=f.lw(6))


def smoke_puffs(f, x, y, t, n=6, seed=3, color="#E6E6EE"):
    ctx = f.ctx
    for i, (a, b, c, d, e, g) in enumerate(_parts(seed, n)):
        life = (t * (0.5 + 0.4 * b) + c) % 1.0
        r = 30 + 70 * life
        xx = x + (a - 0.5) * 160 * life
        yy = y + 40 * life
        ellipse(ctx, xx, yy, r, r * 0.8)
        set_color(ctx, color, 0.85 * (1 - life))
        ctx.fill_preserve()
        set_color(ctx, INK, 0.5 * (1 - life))
        ctx.set_line_width(f.lw(4))
        ctx.stroke()
