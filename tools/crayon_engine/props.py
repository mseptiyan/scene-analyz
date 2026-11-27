"""Props (6-8 px outline, flat fill + one crescent shadow). All logos are generic, never real."""
from __future__ import annotations

import math

from .core import PAL, clamp, ease_in_out, ease_out, hx, lerp, shade, tint
from .draw import (INK, bean, circle, crescent, ellipse, fill_stroke, line, outlined_stroke, poly, rrect,
                   set_color, shaded_shape)
from .text import font, label, text


def _xf(ctx, x, y, s=1.0, angle=0.0):
    ctx.save()
    ctx.translate(x, y)
    if angle:
        ctx.rotate(angle)
    if s != 1.0:
        ctx.scale(s, s)


def certificate(f, x, y, w, value="$135", sub="1 SHARE", s=1.0, angle=0.0, chars=None):
    ctx = f.ctx
    h = w * 0.66
    _xf(ctx, x, y, s, angle)
    rrect(ctx, -w / 2, -h / 2, w, h, 8)
    fill_stroke(ctx, "#F6EFD9", f.lw(6) / s)
    rrect(ctx, -w / 2 + w * 0.06, -h / 2 + w * 0.06, w * 0.88, h - w * 0.12, 6)
    fill_stroke(ctx, None, f.lw(4) / s, ink=hx(PAL["money_sh"]))
    for sx in (-1, 1):
        circle(ctx, sx * w * 0.34, -h * 0.26, w * 0.05)
        fill_stroke(ctx, PAL["gold"], f.lw(3) / s)
    text(ctx, value, 0, h * 0.10, w * 0.30, color=PAL["money_sh"], kind="marker", chars=chars)
    text(ctx, sub, 0, h * 0.34, w * 0.11, color=PAL["ink"], kind="hand")
    ctx.restore()


def bill(f, x, y, w=90, angle=0.0, flip=1.0, alpha=1.0):
    """Paper money (generic). `flip` (-1..1) squashes x for a tumbling look."""
    ctx = f.ctx
    h = w * 0.46
    _xf(ctx, x, y, 1.0, angle)
    ctx.scale(max(abs(flip), 0.08), 1)
    rrect(ctx, -w / 2, -h / 2, w, h, 4)
    fill_stroke(ctx, "#8FCF86", f.lw(4), alpha=alpha)
    rrect(ctx, -w / 2 + 6, -h / 2 + 5, w - 12, h - 10, 3)
    fill_stroke(ctx, None, f.lw(2.5), ink=hx(PAL["money_sh"]), alpha=alpha)
    circle(ctx, 0, 0, h * 0.3)
    fill_stroke(ctx, "#B9E3B0", f.lw(2.5), ink=hx(PAL["money_sh"]), alpha=alpha)
    text(ctx, "$", 0, h * 0.2, h * 0.55, color=PAL["money_sh"], kind="marker", alpha=alpha)
    ctx.restore()


def sack(f, x, y, size=150, color="#D3B07A", angle=0.0, s=1.0):
    """Money sack with a $ sign; (x, y) = bottom centre."""
    ctx = f.ctx
    _xf(ctx, x, y, s, angle)
    w, h = size, size * 0.95

    def body(c):
        c.move_to(-w * 0.18, -h * 0.80)
        c.curve_to(-w * 0.62, -h * 0.62, -w * 0.62, 0, 0, 0)
        c.curve_to(w * 0.62, 0, w * 0.62, -h * 0.62, w * 0.18, -h * 0.80)
        c.close_path()
    shaded_shape(ctx, body, color, w, f.lw(7), k=0.22)
    # neck + tie
    poly(ctx, [(-w * 0.18, -h * 0.80), (-w * 0.26, -h * 1.0), (w * 0.26, -h * 1.0), (w * 0.18, -h * 0.80)])
    fill_stroke(ctx, color, f.lw(7))
    rrect(ctx, -w * 0.22, -h * 0.86, w * 0.44, h * 0.08, 4)
    fill_stroke(ctx, "#9C6B3A", f.lw(5))
    text(ctx, "$", 0, -h * 0.20, h * 0.48, color=PAL["money_sh"], kind="marker")
    ctx.restore()


def money_mountain(f, cx, base_y, width=900, seed=3):
    """A heap of sacks and bills. Returns the summit point."""
    ctx = f.ctx
    # heap silhouette of loose bills
    ctx.move_to(cx - width / 2, base_y)
    ctx.curve_to(cx - width * 0.32, base_y - width * 0.26, cx - width * 0.12, base_y - width * 0.36, cx, base_y - width * 0.37)
    ctx.curve_to(cx + width * 0.12, base_y - width * 0.36, cx + width * 0.32, base_y - width * 0.26, cx + width / 2, base_y)
    ctx.close_path()
    path = ctx.copy_path()
    set_color(ctx, "#7DBF73")
    ctx.fill()
    crescent(ctx, lambda c: c.append_path(path), width * 0.5, shade("#7DBF73", 0.8), 0.18)
    ctx.append_path(path)
    fill_stroke(ctx, None, f.lw(7))
    import random
    rnd = random.Random(seed)
    for i in range(26):
        u = rnd.uniform(-0.42, 0.42)
        v = rnd.uniform(0.05, 0.9) * (1 - abs(u) * 2.0)
        bill(f, cx + u * width, base_y - v * width * 0.34 - 10, 70, angle=rnd.uniform(-0.6, 0.6))
    for (u, v, sz, c) in ((-0.30, 0.02, 170, "#D3B07A"), (0.27, 0.0, 180, "#C9A66B"), (-0.12, 0.13, 160, "#D8B985"),
                          (0.10, 0.14, 165, "#CFAE76"), (0.0, 0.26, 150, "#D3B07A")):
        sack(f, cx + u * width, base_y - v * width, sz, c)
    return cx, base_y - width * 0.37


def rocket(f, x, y, size=120, angle=0.0, flame=0.0, body="#F4F4F2", fin=PAL["loss"], s=1.0):
    """Generic rocket (no real branding). (x, y) = centre; angle 0 = pointing up."""
    ctx = f.ctx
    _xf(ctx, x, y, s, angle)
    L, Wd = size, size * 0.34
    if flame > 0:
        fl = L * (0.35 + 0.25 * flame)
        for c, k in (("#F2B630", 1.0), ("#FFF3C4", 0.55)):
            ctx.move_to(-Wd * 0.32 * k, L * 0.42)
            ctx.curve_to(-Wd * 0.3 * k, L * 0.42 + fl * 0.6 * k, 0, L * 0.42 + fl * k, 0, L * 0.42 + fl * k)
            ctx.curve_to(0, L * 0.42 + fl * k, Wd * 0.3 * k, L * 0.42 + fl * 0.6 * k, Wd * 0.32 * k, L * 0.42)
            ctx.close_path()
            fill_stroke(ctx, c, f.lw(4) if k == 1.0 else 0)
    for sx in (-1, 1):
        poly(ctx, [(sx * Wd * 0.45, L * 0.10), (sx * Wd * 0.95, L * 0.45), (sx * Wd * 0.45, L * 0.38)])
        fill_stroke(ctx, fin, f.lw(5))

    def bodyp(c):
        c.move_to(0, -L * 0.5)
        c.curve_to(Wd * 0.62, -L * 0.30, Wd * 0.55, L * 0.25, Wd * 0.40, L * 0.42)
        c.line_to(-Wd * 0.40, L * 0.42)
        c.curve_to(-Wd * 0.55, L * 0.25, -Wd * 0.62, -L * 0.30, 0, -L * 0.5)
        c.close_path()
    shaded_shape(ctx, bodyp, body, Wd, f.lw(6), k=0.25)
    circle(ctx, 0, -L * 0.08, Wd * 0.18)
    fill_stroke(ctx, "#7EC8E3", f.lw(5))
    ctx.restore()


def newspaper(f, x, y, w, masthead, headline, angle=0.0, s=1.0, chart=True):
    ctx = f.ctx
    h = w * 0.72
    _xf(ctx, x, y, s, angle)
    rrect(ctx, -w / 2 + 10, -h / 2 + 12, w, h, 6)
    set_color(ctx, INK, 0.25)
    ctx.fill()
    rrect(ctx, -w / 2, -h / 2, w, h, 6)
    fill_stroke(ctx, "#F3EFE6", f.lw(6))
    text(ctx, masthead, 0, -h * 0.34, w * 0.07, color=PAL["ink"], kind="marker", tracking=0.05)
    line(ctx, [(-w * 0.45, -h * 0.29), (w * 0.45, -h * 0.29)], f.lw(3))
    line(ctx, [(-w * 0.45, -h * 0.27), (w * 0.45, -h * 0.27)], f.lw(1.5))
    words = headline.split()
    mid = len(words) // 2 + (len(words) % 2)
    text(ctx, " ".join(words[:mid]), 0, -h * 0.12, w * 0.105, color=PAL["ink"], kind="marker")
    text(ctx, " ".join(words[mid:]), 0, h * 0.03, w * 0.105, color=PAL["loss_sh"], kind="marker")
    # columns + chart box
    for i in range(6):
        yy = h * 0.12 + i * h * 0.055
        line(ctx, [(-w * 0.44, yy), (-w * 0.05, yy)], f.lw(3), hx("#B7B1A6"))
    if chart:
        rrect(ctx, w * 0.02, h * 0.09, w * 0.42, h * 0.32, 4)
        fill_stroke(ctx, "#FFFFFF", f.lw(3))
        pts = [(w * 0.06, h * 0.30), (w * 0.14, h * 0.20), (w * 0.20, h * 0.13), (w * 0.27, h * 0.24),
               (w * 0.33, h * 0.33), (w * 0.40, h * 0.37)]
        line(ctx, pts, f.lw(5), hx(PAL["loss"]))
    ctx.restore()


def pizza(f, x, y, r, slices=8, missing=None, lift=0.0, lift_dir=None, s=1.0):
    """Pizza = company; a slice = one share. `missing` slice index is drawn lifted by `lift` * r."""
    ctx = f.ctx
    _xf(ctx, x, y, s)
    crust, cheese, pep = "#E3A247", "#F7D56A", "#C8423B"

    def wedge(c, i, off=(0, 0)):
        a0 = -math.pi / 2 + i * 2 * math.pi / slices
        a1 = a0 + 2 * math.pi / slices
        c.move_to(off[0], off[1])
        c.arc(off[0], off[1], r, a0, a1)
        c.close_path()

    for i in range(slices):
        if i == missing:
            continue
        wedge(ctx, i)
        set_color(ctx, crust)
        ctx.fill()
    circle(ctx, 0, 0, r * 0.86)
    ctx.save()
    ctx.clip()
    for i in range(slices):
        if i == missing:
            ctx.save()
            wedge(ctx, i)
            set_color(ctx, "#FFFFFF", 0.0)
            ctx.restore()
            continue
    ctx.restore()
    # cheese per wedge (so the missing one is really missing)
    for i in range(slices):
        if i == missing:
            continue
        ctx.save()
        wedge(ctx, i)
        ctx.clip()
        circle(ctx, 0, 0, r * 0.86)
        set_color(ctx, cheese)
        ctx.fill()
        crescent(ctx, lambda c: circle(c, 0, 0, r * 0.86), r * 2, shade(cheese, 0.86), 0.10)
        ctx.restore()
    peps = [(0.45, 0.2), (0.55, 1.1), (0.30, 2.0), (0.60, 2.7), (0.42, 3.6), (0.62, 4.4), (0.33, 5.2), (0.58, 5.9)]
    for (d, a) in peps:
        px, py = math.cos(a) * r * d, math.sin(a) * r * d
        ang = (math.atan2(py, px) + math.pi / 2) % (2 * math.pi)
        idx = int(ang / (2 * math.pi / slices))
        if idx == missing:
            continue
        circle(ctx, px, py, r * 0.11)
        fill_stroke(ctx, pep, f.lw(4))
    for i in range(slices):
        if i == missing or (missing is not None and i == (missing + 1) % slices):
            pass
        a = -math.pi / 2 + i * 2 * math.pi / slices
        line(ctx, [(0, 0), (math.cos(a) * r, math.sin(a) * r)], f.lw(4))
    # outline of the remaining pie
    ctx.new_path()
    if missing is None:
        circle(ctx, 0, 0, r)
    else:
        a0 = -math.pi / 2 + (missing + 1) * 2 * math.pi / slices
        a1 = a0 + (slices - 1) * 2 * math.pi / slices
        ctx.move_to(0, 0)
        ctx.arc(0, 0, r, a0, a1)
        ctx.close_path()
    fill_stroke(ctx, None, f.lw(7))
    if missing is not None:
        a_mid = -math.pi / 2 + (missing + 0.5) * 2 * math.pi / slices
        d = lift_dir if lift_dir is not None else (math.cos(a_mid), math.sin(a_mid))
        off = (d[0] * lift * r, d[1] * lift * r)
        pizza_slice(f, off, r, missing, slices, crust, cheese, pep)
    ctx.restore()


def pizza_slice(f, off, r, i, slices=8, crust="#E3A247", cheese="#F7D56A", pep="#C8423B"):
    ctx = f.ctx
    a0 = -math.pi / 2 + i * 2 * math.pi / slices
    a1 = a0 + 2 * math.pi / slices

    def wedge(c):
        c.move_to(*off)
        c.arc(off[0], off[1], r, a0, a1)
        c.close_path()
    wedge(ctx)
    set_color(ctx, crust)
    ctx.fill()
    ctx.save()
    wedge(ctx)
    ctx.clip()
    circle(ctx, off[0], off[1], r * 0.86)
    set_color(ctx, cheese)
    ctx.fill()
    am = (a0 + a1) / 2
    circle(ctx, off[0] + math.cos(am) * r * 0.55, off[1] + math.sin(am) * r * 0.55, r * 0.11)
    fill_stroke(ctx, pep, f.lw(4))
    ctx.restore()
    wedge(ctx)
    fill_stroke(ctx, None, f.lw(7))


def rope_line(f, x0, x1, y, post_h=170, n_posts=3, sag=40):
    """Gold posts + red velvet rope (club = private market)."""
    ctx = f.ctx
    xs = [lerp(x0, x1, i / (n_posts - 1)) for i in range(n_posts)]
    top = y - post_h
    for i in range(n_posts - 1):
        a, b = xs[i], xs[i + 1]

        def rp(c, a=a, b=b):
            c.move_to(a, top + 20)
            c.curve_to(a + (b - a) * 0.3, top + 20 + sag, a + (b - a) * 0.7, top + 20 + sag, b, top + 20)
        outlined_stroke(ctx, rp, hx("#B0283A"), f.lw(14), f.lw(5))
    for xx in xs:
        rrect(ctx, xx - 10, top + 10, 20, post_h - 10, 6)
        fill_stroke(ctx, PAL["gold"], f.lw(6))
        circle(ctx, xx, top + 6, 18)
        fill_stroke(ctx, PAL["gold"], f.lw(6))
        ellipse(ctx, xx, y, 46, 12)
        fill_stroke(ctx, PAL["gold_sh"], f.lw(6))


def plaque(f, x, y, s, w=360, color="#1E1A1B", fg=PAL["gold"]):
    ctx = f.ctx
    fs = w * 0.13
    h = fs * 2.0
    rrect(ctx, x - w / 2, y - h / 2, w, h, 12)
    fill_stroke(ctx, color, f.lw(6))
    rrect(ctx, x - w / 2 + 8, y - h / 2 + 8, w - 16, h - 16, 8)
    fill_stroke(ctx, None, f.lw(3), ink=hx(fg))
    text(ctx, s, x, y + fs * 0.36, fs, color=fg, kind="marker", tracking=0.06)


def doors(f, cx, floor_y, w=560, h=640, open_p=0.0, sign="IPO", wall="#2E5E78"):
    """Double doors. open_p 0..1 swings both leaves (perspective squash) and floods light."""
    ctx = f.ctx
    x0, y0 = cx - w / 2, floor_y - h
    # frame
    rrect(ctx, x0 - 30, y0 - 30, w + 60, h + 30, 10)
    fill_stroke(ctx, "#1F3442", f.lw(8))
    # opening: warm light
    rrect(ctx, x0, y0, w, h, 4)
    fill_stroke(ctx, "#FFF4D6" if open_p > 0 else "#14222C", f.lw(6))
    if open_p > 0:
        # light spilling onto the floor
        a = 0.35 * clamp(open_p * 1.4)
        poly(ctx, [(x0, floor_y), (x0 + w, floor_y), (x0 + w + 420, floor_y + 380), (x0 - 420, floor_y + 380)])
        set_color(ctx, "#FFF1C2", a)
        ctx.fill()
        for k in range(3):  # shafts
            sx = x0 + w * (0.2 + 0.3 * k)
            poly(ctx, [(sx, y0 + 40), (sx + 70, y0 + 40), (sx + 330, floor_y + 380), (sx + 120, floor_y + 380)])
            set_color(ctx, "#FFFFFF", 0.10 * clamp(open_p * 1.5))
            ctx.fill()
    for s in (-1, 1):
        leaf_w = w / 2 * (1 - 0.82 * ease_out(open_p))
        hinge = x0 if s < 0 else x0 + w
        lx = hinge if s < 0 else hinge - leaf_w
        skew = 40 * ease_out(open_p)
        pts = [(lx, y0), (lx + leaf_w, y0), (lx + leaf_w, floor_y), (lx, floor_y)]
        if s < 0:
            pts = [(lx, y0), (lx + leaf_w, y0 - skew), (lx + leaf_w, floor_y + skew), (lx, floor_y)]
        else:
            pts = [(lx, y0 - skew), (lx + leaf_w, y0), (lx + leaf_w, floor_y), (lx, floor_y + skew)]
        poly(ctx, pts)
        fill_stroke(ctx, "#20374A" if open_p < 0.5 else "#1B2F3E", f.lw(7))
        if leaf_w > 40:
            hxp = lx + leaf_w - 28 if s < 0 else lx + 28
            circle(ctx, hxp, (y0 + floor_y) / 2, 12)
            fill_stroke(ctx, PAL["gold"], f.lw(5))
    # sign
    rrect(ctx, cx - 150, y0 - 140, 300, 90, 14)
    fill_stroke(ctx, "#1E1A1B", f.lw(7))
    text(ctx, sign, cx, y0 - 70, 72, color=PAL["gold"], kind="marker", tracking=0.12)


def phone(f, x, y, h=70, angle=0.0, screen="#9ED8F0"):
    ctx = f.ctx
    _xf(ctx, x, y, 1.0, angle)
    w = h * 0.55
    rrect(ctx, -w / 2, -h / 2, w, h, 8)
    fill_stroke(ctx, "#2B2B30", f.lw(5))
    rrect(ctx, -w / 2 + 5, -h / 2 + 7, w - 10, h - 16, 4)
    set_color(ctx, screen)
    ctx.fill()
    ctx.restore()


def ticket(f, x, y, w, s="IPO", angle=0.0):
    ctx = f.ctx
    h = w * 0.5
    _xf(ctx, x, y, 1.0, angle)
    ctx.move_to(-w / 2, -h / 2)
    ctx.line_to(w / 2, -h / 2)
    ctx.arc_negative(w / 2, 0, h * 0.18, -math.pi / 2, math.pi / 2)
    ctx.line_to(w / 2, h / 2)
    ctx.line_to(-w / 2, h / 2)
    ctx.arc_negative(-w / 2, 0, h * 0.18, math.pi / 2, -math.pi / 2)
    ctx.close_path()
    fill_stroke(ctx, "#FDF3D0", f.lw(5))
    text(ctx, s, 0, h * 0.2, h * 0.55, color=PAL["loss_sh"], kind="marker", tracking=0.05)
    ctx.restore()


def calendar(f, x, y, w, pages, t, t0, flip_dur=5 / 30, interval=None, header_c="#D9363E", sub=None):
    """Desk calendar (time marker). Flips through `pages` starting at t0; each flip = flip_dur.
    `interval` = time per page (default flip_dur). Returns the index of the page shown."""
    ctx = f.ctx
    interval = interval or flip_dur
    h = w * 0.95
    k = 0 if t < t0 else min(len(pages) - 1, int((t - t0) / interval))
    phase = 0 if t < t0 or k >= len(pages) - 1 else ((t - t0) - k * interval) / flip_dur
    # stand (tent)
    poly(ctx, [(x - w * 0.55, y + h * 0.55), (x + w * 0.55, y + h * 0.55), (x + w * 0.45, y - h * 0.40),
               (x - w * 0.45, y - h * 0.40)])
    fill_stroke(ctx, "#3A3436", f.lw(7))

    def page(txt, scale_y=1.0, dark=0.0):
        ph = h * 0.86 * scale_y
        rrect(ctx, x - w / 2, y - h * 0.43, w, ph, 10)
        fill_stroke(ctx, "#FFFDF7", f.lw(6))
        if scale_y > 0.25:
            rrect(ctx, x - w / 2, y - h * 0.43, w, min(ph, h * 0.22), 10)
            fill_stroke(ctx, header_c, f.lw(6))
            if sub and scale_y > 0.9:
                text(ctx, sub, x, y - h * 0.43 + h * 0.155, h * 0.13, color=PAL["paper"], kind="marker", tracking=0.08)
            if scale_y > 0.6:
                ctx.save()
                ctx.translate(x, y - h * 0.43 + ph * 0.62)
                ctx.scale(1, scale_y)
                text(ctx, txt, 0, h * 0.12, h * 0.34 if len(txt) <= 4 else h * 0.25, color=PAL["ink"], kind="marker")
                ctx.restore()
        if dark > 0:
            rrect(ctx, x - w / 2, y - h * 0.43, w, ph, 10)
            set_color(ctx, INK, dark)
            ctx.fill()
    nxt = pages[min(k + 1, len(pages) - 1)]
    if phase > 0:
        page(nxt)
        page(pages[k], scale_y=max(0.02, 1 - ease_in_out(phase)), dark=0.25 * phase)
    else:
        page(pages[k])
    # rings
    for s in (-0.25, 0.25):
        rrect(ctx, x + s * w - 8, y - h * 0.50, 16, h * 0.14, 6)
        fill_stroke(ctx, "#9A9AA0", f.lw(4))
    return k


def chart(f, x, y, w, h, pts, progress=1.0, color=PAL["money"], grid=True, glow="#3FD0E0", lw_px=10,
          rocket_tip=False, labels=None, flame=1.0):
    """Stock chart drawn on along its path. pts = [(u, v)] in 0..1 (v up). Returns the tip."""
    ctx = f.ctx
    if grid:
        for i in range(7):
            gx = x + w * i / 6
            line(ctx, [(gx, y), (gx, y + h)], f.lw(2), hx("#4A7598"))
        for j in range(5):
            gy = y + h * j / 4
            line(ctx, [(x, gy), (x + w, gy)], f.lw(2), hx("#4A7598"))
    P = [(x + u * w, y + (1 - v) * h) for u, v in pts]
    seg = [math.dist(P[i], P[i + 1]) for i in range(len(P) - 1)]
    total = sum(seg)
    target = total * clamp(progress)
    draw_pts = [P[0]]
    acc = 0.0
    tip_ang = 0.0
    for i, d in enumerate(seg):
        if acc + d >= target:
            k = (target - acc) / d if d else 0
            draw_pts.append((lerp(P[i][0], P[i + 1][0], k), lerp(P[i][1], P[i + 1][1], k)))
            tip_ang = math.atan2(P[i + 1][1] - P[i][1], P[i + 1][0] - P[i][0])
            break
        draw_pts.append(P[i + 1])
        acc += d
        tip_ang = math.atan2(P[i + 1][1] - P[i][1], P[i + 1][0] - P[i][0])
    if len(draw_pts) >= 2:
        for c, wpx, a in ((glow, lw_px * 3.2, 0.18), (glow, lw_px * 1.9, 0.25)):
            line(ctx, draw_pts, f.lw(wpx), hx(c), a)
        line(ctx, draw_pts, f.lw(lw_px + 8), INK)
        line(ctx, draw_pts, f.lw(lw_px), hx(color))
    tip = draw_pts[-1]
    if rocket_tip and progress > 0.01:
        rocket(f, tip[0], tip[1], 120, angle=tip_ang + math.pi / 2, flame=flame)
    return tip, tip_ang


def word_card(f, x, y, w, word, color, icon=None, s=1.0, sub=None):
    ctx = f.ctx
    h = w * 1.05
    _xf(ctx, x, y, s)
    rrect(ctx, -w / 2 + 10, -h / 2 + 14, w, h, 26)
    set_color(ctx, INK, 0.18)
    ctx.fill()

    def cp(c):
        rrect(c, -w / 2, -h / 2, w, h, 26)
    shaded_shape(ctx, cp, color, w, f.lw(8), k=0.07)
    if icon:
        icon(f, 0, -h * 0.12, w * 0.5)
    text(ctx, word, 0, h * 0.36, w * 0.17, color=PAL["paper"], kind="marker", stroke=PAL["ink"], stroke_px=f.lw(6),
         tracking=0.04)
    ctx.restore()


def building(f, x, base_y, w=300, h=360, color="#7FA7C9"):
    """Generic company office (no logo)."""
    ctx = f.ctx

    def bp(c):
        rrect(c, x - w / 2, base_y - h, w, h, 8)
    shaded_shape(ctx, bp, color, w, f.lw(7), k=0.12)
    for i in range(3):
        for j in range(4):
            rrect(ctx, x - w * 0.36 + i * w * 0.27, base_y - h * 0.88 + j * h * 0.2, w * 0.18, h * 0.12, 4)
            fill_stroke(ctx, "#FFF1C2" if (i + j) % 3 else "#CFE6F5", f.lw(4))
    rrect(ctx, x - w * 0.11, base_y - h * 0.18, w * 0.22, h * 0.18, 4)
    fill_stroke(ctx, "#3E4A5A", f.lw(5))


def ticker_strip(f, y, h, t, items, speed=140, bg="#0F1B26"):
    """Scrolling ticker tape (generic). items = [(text, up_bool)]."""
    ctx = f.ctx
    from .core import W
    ctx.rectangle(-20, y, W + 40, h)
    fill_stroke(ctx, bg, f.lw(6))
    fnt = font("marker")
    size = h * 0.55
    seq = "   ".join(f"{s} {'▲' if up else '▼'}" for s, up in items)
    seq_w = fnt.width(seq + "   ", size)
    off = -(t * speed) % seq_w
    xx = off - seq_w
    while xx < W:
        cx = xx
        for s, up in items:
            col = PAL["money_lt"] if up else "#FF7A7F"
            wtxt = fnt.width(s + " ", size)
            text(ctx, s + " ", cx, y + h * 0.7, size, color=col, kind="marker", align="left")
            cx += wtxt
            # triangle arrow
            ax = cx + size * 0.15
            if up:
                poly(ctx, [(ax, y + h * 0.66), (ax + size * 0.5, y + h * 0.66), (ax + size * 0.25, y + h * 0.30)])
            else:
                poly(ctx, [(ax, y + h * 0.34), (ax + size * 0.5, y + h * 0.34), (ax + size * 0.25, y + h * 0.70)])
            set_color(ctx, col)
            ctx.fill()
            cx += size * 0.5 + fnt.width("   ", size)
        xx += seq_w
