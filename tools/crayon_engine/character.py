"""Crayon Verse characters: perfectly round head, bean body (= clothing), single-line limbs.

Standard (references/character_design_standards.md):
  * total height ~3.2 x head diameter D; head 31%, bean body ~39% (width 1.0 D), legs ~33%
  * no neck: head overlaps the body by 0.1 D
  * outline #1A1617, 8 px at 1080p (constant under camera zoom), round caps
  * one hard crescent shadow on head, hair and body, away from the key light
  * colour hierarchy: hero = skin + hair colour; extras = white head; crowd = grey; silhouette = ink
  * expressions = swap of eyes + brows + mouth (instant swaps, no in-betweens)
  * moving hold: blink every 2-5 s (4 frames, de-synced by seed) + breathing 1.2 % / 2.6 s
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field, replace

from .core import FPS, PAL, hx, mix, shade, tint
from .draw import (INK, KEY_LIGHT, bean, circle, contact_shadow, crescent, ellipse, fill_stroke, line,
                   rrect, set_color, shaded_shape)


@dataclass
class Look:
    name: str
    cls: str = "extra"                 # hero | extra | crowd | silhouette
    skin: str = PAL["paper"]
    skin_sh: str | None = PAL["paper_shade"]
    hair: str | None = None            # elon | short | bob | bun | curly | None
    hair_c: str = "#3A2B24"
    body: str = "#2E9C9A"
    inner: str | None = None           # shirt visible in a jacket "V"
    tie: str | None = None
    hat: str | None = None             # tophat | hardhat | cap
    hat_c: str = "#1F1C1D"
    glasses: str | None = None         # sun | round | monocle
    earpiece: bool = False
    pin: str | None = None             # small accent badge
    hood: bool = False
    width: float = 1.0
    extra: dict = field(default_factory=dict)


# eyes, (brow angle deg, brow dy in D), mouth, sweat
EXPR = {
    "neutral":  ("open", (0, 0.0), "line", False),
    "happy":    ("open", (-4, -0.01), "smile", False),
    "proud":    ("closed", (6, 0.01), "smile", False),
    "grin":     ("open", (-8, -0.03), "grin", False),
    "sparkle":  ("sparkle", (-10, -0.04), "grin", False),
    "shock":    ("dots", (-14, -0.07), "O", False),
    "sad":      ("open", (-22, -0.02), "frown", False),
    "worried":  ("open", (-20, -0.03), "wave", True),
    "angry":    ("open", (24, 0.02), "frown", False),
    "thinking": ("up", (10, -0.02), "smirk", False),
    "smug":     ("half", (8, 0.015), "smirk", False),
    "shout":    ("open", (22, 0.0), "shout", False),
}

POSES = {
    # hand target (dx, dy) relative to shoulder in D units for side s (+1 = right), and elbow control
    "idle":    {"h": lambda s: (s * 0.24, 0.78), "c": lambda s: (s * 0.30, 0.36)},
    "sad":     {"h": lambda s: (s * 0.08, 0.82), "c": lambda s: (s * 0.12, 0.40)},
    "hips":    {"h": lambda s: (s * 0.02, 0.62), "c": lambda s: (s * 0.52, 0.30)},
    "arms_up": {"h": lambda s: (s * 0.58, -0.82), "c": lambda s: (s * 0.52, -0.22)},
    "shrug":   {"h": lambda s: (s * 0.62, -0.18), "c": lambda s: (s * 0.42, 0.30)},
    "hold":    {"h": lambda s: (-s * 0.30, 0.40), "c": lambda s: (s * 0.22, 0.52)},
}


def _pose_hand(pose, side):
    if pose == "wave":
        return POSES["arms_up"] if side > 0 else POSES["idle"]
    if pose == "point":
        return {"h": lambda s: (s * 0.95, -0.05), "c": lambda s: (s * 0.5, 0.02)} if side > 0 else POSES["idle"]
    if pose == "phone":
        return {"h": lambda s: (s * 0.05, -0.50), "c": lambda s: (s * 0.55, -0.05)} if side > 0 else POSES["idle"]
    if pose == "hold_r":
        return {"h": lambda s: (s * 0.55, 0.12), "c": lambda s: (s * 0.42, 0.42)} if side > 0 else POSES["idle"]
    return POSES.get(pose, POSES["idle"])


def _blinking(t, seed):
    """True during a 4-frame blink. Interval 2-5 s, de-synced per character by seed."""
    if t is None:
        return False
    rng = (seed * 0.6180339887) % 1.0
    period = 2.0 + 3.0 * rng
    phase = (t + rng * 7.3) % period
    return phase < 4 / FPS


def _hair_path(style, cx, cy, R):
    def p(ctx):
        if style == "elon":   # short, swept-back volume with a front quiff to screen-right
            ctx.move_to(cx - R * 1.00, cy - R * 0.02)
            ctx.curve_to(cx - R * 1.05, cy - R * 0.70, cx - R * 0.70, cy - R * 1.12, cx - R * 0.15, cy - R * 1.18)
            ctx.curve_to(cx + R * 0.35, cy - R * 1.30, cx + R * 0.82, cy - R * 1.20, cx + R * 0.96, cy - R * 0.86)
            ctx.curve_to(cx + R * 1.06, cy - R * 0.60, cx + R * 1.02, cy - R * 0.30, cx + R * 0.97, cy - R * 0.12)
            ctx.curve_to(cx + R * 0.86, cy - R * 0.42, cx + R * 0.66, cy - R * 0.52, cx + R * 0.40, cy - R * 0.60)
            ctx.curve_to(cx + R * 0.05, cy - R * 0.74, cx - R * 0.42, cy - R * 0.62, cx - R * 0.70, cy - R * 0.40)
            ctx.curve_to(cx - R * 0.84, cy - R * 0.26, cx - R * 0.92, cy - R * 0.12, cx - R * 1.00, cy - R * 0.02)
            ctx.close_path()
        elif style == "short":
            ctx.move_to(cx - R * 0.99, cy - R * 0.10)
            ctx.curve_to(cx - R * 1.02, cy - R * 0.85, cx - R * 0.45, cy - R * 1.10, cx, cy - R * 1.08)
            ctx.curve_to(cx + R * 0.45, cy - R * 1.10, cx + R * 1.02, cy - R * 0.85, cx + R * 0.99, cy - R * 0.10)
            ctx.curve_to(cx + R * 0.70, cy - R * 0.55, cx - R * 0.70, cy - R * 0.55, cx - R * 0.99, cy - R * 0.10)
            ctx.close_path()
        elif style == "bob":
            ctx.move_to(cx - R * 1.10, cy + R * 0.55)
            ctx.curve_to(cx - R * 1.25, cy - R * 0.60, cx - R * 0.55, cy - R * 1.18, cx, cy - R * 1.12)
            ctx.curve_to(cx + R * 0.55, cy - R * 1.18, cx + R * 1.25, cy - R * 0.60, cx + R * 1.10, cy + R * 0.55)
            ctx.curve_to(cx + R * 0.95, cy + R * 0.60, cx + R * 0.85, cy + R * 0.40, cx + R * 0.80, cy - R * 0.25)
            ctx.curve_to(cx + R * 0.40, cy - R * 0.55, cx - R * 0.40, cy - R * 0.55, cx - R * 0.80, cy - R * 0.25)
            ctx.curve_to(cx - R * 0.85, cy + R * 0.40, cx - R * 0.95, cy + R * 0.60, cx - R * 1.10, cy + R * 0.55)
            ctx.close_path()
        elif style == "bun":
            circle(ctx, cx + R * 0.10, cy - R * 1.22, R * 0.34)
            ctx.move_to(cx - R * 0.98, cy - R * 0.15)
            ctx.curve_to(cx - R * 1.0, cy - R * 0.9, cx - R * 0.4, cy - R * 1.08, cx, cy - R * 1.06)
            ctx.curve_to(cx + R * 0.4, cy - R * 1.08, cx + R * 1.0, cy - R * 0.9, cx + R * 0.98, cy - R * 0.15)
            ctx.curve_to(cx + R * 0.6, cy - R * 0.62, cx - R * 0.6, cy - R * 0.62, cx - R * 0.98, cy - R * 0.15)
            ctx.close_path()
        elif style == "curly":
            n = 9
            pts = []
            for i in range(n + 1):
                a = math.pi * (1.05 + 0.9 * i / n)
                pts.append((cx + math.cos(a) * R * 1.02, cy + math.sin(a) * R * 1.02))
            ctx.move_to(*pts[0])
            for i in range(n):
                (x0, y0), (x1, y1) = pts[i], pts[i + 1]
                mx, my = (x0 + x1) / 2, (y0 + y1) / 2
                ox, oy = (mx - cx) * 0.22, (my - cy) * 0.22
                ctx.curve_to(x0 + ox, y0 + oy, x1 + ox, y1 + oy, x1, y1)
            ctx.curve_to(cx + R * 0.6, cy - R * 0.5, cx - R * 0.6, cy - R * 0.5, *pts[0])
            ctx.close_path()
    return p


def draw(f, look: Look, x: float, y_feet: float, h: float, expr: str = "neutral", pose: str = "idle",
         facing: float = 0.0, seed: int = 0, anon: bool = False, breathe: bool = True, blink: bool = True,
         hands: bool = False, hand_r=None, hand_l=None, lw_px: float = 8.0, light=KEY_LIGHT, alpha: float = 1.0,
         shadow_floor: bool = True, wave_phase: float | None = None):
    """Draw one character with feet at (x, y_feet) and total height h. Returns anchor points."""
    ctx = f.ctx
    t = f.T
    D = h / 3.2
    R = D / 2
    lw = f.lw(lw_px)
    cls = look.cls
    sil = cls == "silhouette"
    crowd = cls == "crowd"
    ink = INK if not sil else hx("#0E0C0D")

    b = 1 + (0.012 * math.sin(2 * math.pi * t / 2.6 + seed * 1.7) if breathe else 0)
    legs = 1.05 * D
    body_h = 1.25 * D * b
    body_w = 1.0 * D * look.width
    body_bot = y_feet - legs + 0.10 * D
    body_top = body_bot - body_h
    hx_, hy_ = x, body_top - R + 0.10 * D

    skin = PAL["anon"] if anon else look.skin
    skin_sh = PAL["anon_sh"] if anon else (look.skin_sh or shade(look.skin))
    hair_c = PAL["anon_hair"] if anon else look.hair_c
    body_c = look.body
    if crowd:
        skin, skin_sh, body_c, hair_c = look.skin, shade(look.skin, 0.86), look.body, shade(look.body, 0.8)
    if sil:
        skin = skin_sh = body_c = hair_c = "#2A2526"

    if shadow_floor:
        contact_shadow(ctx, x, y_feet + 2, body_w * 0.62)

    # ---- legs (single lines) ----
    for s in (-1, 1):
        line(ctx, [(x + s * 0.20 * D, body_bot - 0.08 * D), (x + s * 0.22 * D, y_feet)], lw * 1.15, ink, alpha)
        line(ctx, [(x + s * 0.22 * D, y_feet), (x + s * 0.36 * D, y_feet)], lw * 1.15, ink, alpha)

    # ---- body (bean = clothing) ----
    def body_path(c):
        bean(c, x, body_top, body_w, body_h)
    shaded_shape(ctx, body_path, body_c, body_w, lw, shadow=shade(body_c, 0.78) if not sil else False,
                 k=0.22, light=light, ink=ink, alpha=alpha)
    if not sil and not crowd:
        _body_details(f, look, x, body_top, body_w, body_h, D, lw)

    # ---- arms (rubber-hose lines) ----
    anchors = {"head": (hx_, hy_), "R": R, "top": (hx_, hy_ - R), "mouth": (hx_ + facing * 0.12 * D, hy_ + 0.26 * D)}
    for s in ((-1, 1) if pose != "none" else ()):
        sx, sy = x + s * body_w * 0.46, body_top + 0.30 * body_h
        spec = _pose_hand(pose, s)
        hdx, hdy = spec["h"](s)
        cdx, cdy = spec["c"](s)
        if pose == "wave" and s > 0:
            ph = wave_phase if wave_phase is not None else t
            hdx += 0.12 * math.sin(ph * 2 * math.pi * 1.6)
        tgt = hand_r if (s > 0 and hand_r) else hand_l if (s < 0 and hand_l) else (sx + hdx * D, sy + hdy * D)
        ctrl = (sx + cdx * D, sy + cdy * D)
        line(ctx, [(sx, sy), ctrl, tgt], lw * 1.15, ink, alpha, curve=True)
        anchors["hand_r" if s > 0 else "hand_l"] = tgt
        if hands and not crowd:
            ellipse(ctx, tgt[0], tgt[1], 0.085 * D, 0.075 * D)
            fill_stroke(ctx, PAL["paper"] if not sil else skin, f.lw(lw_px * 0.75), ink, alpha)

    # ---- head ----
    if look.hair == "bob" and not crowd:   # back part of a bob sits behind the head
        pass

    def head_path(c):
        circle(c, hx_, hy_, R)
    shaded_shape(ctx, head_path, skin, D, lw, shadow=skin_sh if not sil else False, k=0.2, light=light,
                 ink=ink, alpha=alpha)

    if look.hair and not crowd:
        hp = _hair_path(look.hair, hx_, hy_, R)
        hp(ctx)
        set_color(ctx, hair_c, alpha)
        ctx.fill()
        if not sil:
            crescent(ctx, hp, D, shade(hair_c, 0.7), 0.16, light, alpha)
            # one highlight band on the lit side
            ctx.save()
            hp(ctx)
            ctx.clip()
            ctx.new_path()
            ctx.arc(hx_ - R * 0.15, hy_ - R * 0.15, R * 0.95, math.radians(200), math.radians(250))
            set_color(ctx, tint(hair_c, 1.45) if not anon else "#8C8C92", alpha)
            ctx.set_line_width(R * 0.10)
            ctx.set_line_cap(1)
            ctx.stroke()
            ctx.restore()
        hp(ctx)
        fill_stroke(ctx, None, lw, ink, alpha)

    if look.hat and not crowd:
        _hat(f, look, hx_, hy_, R, lw, sil)

    # ---- face (swap set) ----
    if not sil and not crowd:
        _face(f, look, hx_ + facing * 0.12 * D, hy_, D, expr, blink and _blinking(t, seed), lw_px)
        if look.glasses:
            _glasses(f, look.glasses, hx_ + facing * 0.12 * D, hy_, D, lw)
        if look.earpiece:
            line(ctx, [(hx_ - R * 0.98, hy_ + R * 0.05), (hx_ - R * 1.10, hy_ + R * 0.60)], f.lw(3), ink)
            circle(ctx, hx_ - R * 0.98, hy_ + R * 0.02, R * 0.08)
            fill_stroke(ctx, "#2B2B30", f.lw(3))
    return anchors


def _body_details(f, look, x, top, w, h, D, lw):
    ctx = f.ctx
    if look.inner:     # jacket open: V of the shirt
        ctx.move_to(x - w * 0.20, top + h * 0.03)
        ctx.line_to(x, top + h * 0.48)
        ctx.line_to(x + w * 0.20, top + h * 0.03)
        ctx.close_path()
        fill_stroke(ctx, look.inner, lw * 0.75)
        # lapel lines
        for s in (-1, 1):
            line(ctx, [(x + s * w * 0.20, top + h * 0.03), (x + s * w * 0.08, top + h * 0.52)], lw * 0.6)
    if look.tie:
        ctx.move_to(x - w * 0.05, top + h * 0.06)
        ctx.line_to(x + w * 0.05, top + h * 0.06)
        ctx.line_to(x + w * 0.07, top + h * 0.36)
        ctx.line_to(x, top + h * 0.45)
        ctx.line_to(x - w * 0.07, top + h * 0.36)
        ctx.close_path()
        fill_stroke(ctx, look.tie, lw * 0.6)
    if look.hood:
        for s in (-1, 1):
            line(ctx, [(x + s * w * 0.10, top + h * 0.10), (x + s * w * 0.12, top + h * 0.34)], lw * 0.5)
        line(ctx, [(x - w * 0.22, top + h * 0.70), (x + w * 0.22, top + h * 0.70)], lw * 0.55)
    if look.pin:
        circle(ctx, x - w * 0.27, top + h * 0.28, D * 0.05)
        fill_stroke(ctx, look.pin, lw * 0.5)


def _hat(f, look, cx, cy, R, lw, sil):
    ctx = f.ctx
    c = look.hat_c if not sil else "#2A2526"
    if look.hat == "tophat":
        rrect(ctx, cx - R * 0.62, cy - R * 1.95, R * 1.24, R * 1.10, R * 0.10)
        fill_stroke(ctx, c, lw)
        rrect(ctx, cx - R * 0.62, cy - R * 1.08, R * 1.24, R * 0.18, 2)
        fill_stroke(ctx, "#8C2A27" if not sil else c, lw * 0.6)
        ellipse(ctx, cx, cy - R * 0.86, R * 1.05, R * 0.16)
        fill_stroke(ctx, c, lw)
    elif look.hat == "hardhat":
        ctx.new_sub_path()
        ctx.arc(cx, cy - R * 0.45, R * 0.92, math.pi, 2 * math.pi)
        ctx.close_path()
        fill_stroke(ctx, c, lw)
        rrect(ctx, cx - R * 1.12, cy - R * 0.55, R * 2.24, R * 0.2, R * 0.1)
        fill_stroke(ctx, c, lw)
    elif look.hat == "cap":
        ctx.new_sub_path()
        ctx.arc(cx, cy - R * 0.40, R * 0.95, math.pi, 2 * math.pi)
        ctx.close_path()
        fill_stroke(ctx, c, lw)
        ellipse(ctx, cx + R * 0.65, cy - R * 0.42, R * 0.55, R * 0.12)
        fill_stroke(ctx, c, lw)


def _glasses(f, kind, cx, cy, D, lw):
    ctx = f.ctx
    ey = cy + 0.02 * D
    if kind == "sun":
        for s in (-1, 1):
            rrect(ctx, cx + s * 0.15 * D - 0.11 * D, ey - 0.06 * D, 0.22 * D, 0.13 * D, 0.04 * D)
            fill_stroke(ctx, "#141214", lw * 0.6)
        line(ctx, [(cx - 0.04 * D, ey - 0.02 * D), (cx + 0.04 * D, ey - 0.02 * D)], lw * 0.6)
    elif kind == "round":
        for s in (-1, 1):
            circle(ctx, cx + s * 0.15 * D, ey, 0.09 * D)
            fill_stroke(ctx, None, lw * 0.55)
        line(ctx, [(cx - 0.06 * D, ey), (cx + 0.06 * D, ey)], lw * 0.55)
    elif kind == "monocle":
        circle(ctx, cx + 0.15 * D, ey, 0.10 * D)
        fill_stroke(ctx, None, lw * 0.6, ink=hx(PAL["gold_sh"]))
        line(ctx, [(cx + 0.24 * D, ey + 0.05 * D), (cx + 0.30 * D, ey + 0.45 * D)], f.lw(2.5), hx(PAL["gold_sh"]))


def _face(f, look, fx, cy, D, expr, blinking, lw_px):
    ctx = f.ctx
    eyes, (bang, bdy), mouth, sweat = EXPR.get(expr, EXPR["neutral"])
    ey = cy + 0.02 * D
    ex = 0.15 * D
    lwf = f.lw(lw_px * 0.75)
    # eyes
    for s in (-1, 1):
        x = fx + s * ex
        e = "closed_flat" if blinking and eyes in ("open", "sparkle", "up", "half") else eyes
        if e in ("open", "sparkle", "up"):
            oy = -0.03 * D if e == "up" else 0
            ellipse(ctx, x, ey + oy, 0.034 * D, 0.058 * D)
            set_color(ctx, INK)
            ctx.fill()
            circle(ctx, x + 0.012 * D, ey + oy - 0.022 * D, 0.011 * D)
            set_color(ctx, PAL["paper"])
            ctx.fill()
            if e == "sparkle":
                circle(ctx, x - 0.012 * D, ey + 0.02 * D, 0.007 * D)
                set_color(ctx, PAL["paper"])
                ctx.fill()
        elif e == "half":
            ctx.save()
            ctx.rectangle(x - 0.05 * D, ey - 0.005 * D, 0.1 * D, 0.08 * D)
            ctx.clip()
            ellipse(ctx, x, ey, 0.034 * D, 0.058 * D)
            set_color(ctx, INK)
            ctx.fill()
            ctx.restore()
            line(ctx, [(x - 0.05 * D, ey - 0.005 * D), (x + 0.05 * D, ey - 0.005 * D)], lwf)
        elif e == "closed":      # happy/proud closed eyes (arc up)
            ctx.new_path()
            ctx.arc(x, ey + 0.03 * D, 0.05 * D, math.radians(200), math.radians(340))
            set_color(ctx, INK)
            ctx.set_line_width(lwf)
            ctx.set_line_cap(1)
            ctx.stroke()
        elif e == "closed_flat":
            line(ctx, [(x - 0.045 * D, ey + 0.01 * D), (x + 0.045 * D, ey + 0.01 * D)], lwf)
        elif e == "dots":
            circle(ctx, x, ey, 0.024 * D)
            set_color(ctx, INK)
            ctx.fill()
    # brows (lead actor of the expression)
    by = ey - 0.17 * D + bdy * D
    for s in (-1, 1):
        x = fx + s * ex
        a = math.radians(bang) * s * -1  # positive angle = inner ends down (angry)
        if expr == "thinking" and s < 0:
            a, byy = math.radians(-12), by - 0.03 * D
        else:
            byy = by
        L = 0.10 * D
        x0, y0 = x - L * math.cos(a), byy - L * math.sin(a)
        x1, y1 = x + L * math.cos(a), byy + L * math.sin(a)
        line(ctx, [(x0, y0), ((x0 + x1) / 2, (y0 + y1) / 2 - 0.025 * D), (x1, y1)], f.lw(lw_px * 0.8), curve=True)
    # mouth
    my = cy + 0.26 * D
    mw = 0.07 * D
    if mouth == "line":
        line(ctx, [(fx - mw, my), (fx + mw, my)], lwf)
    elif mouth == "smile":
        line(ctx, [(fx - mw * 1.2, my - 0.01 * D), (fx, my + 0.06 * D), (fx + mw * 1.2, my - 0.01 * D)], lwf, curve=True)
    elif mouth == "frown":
        line(ctx, [(fx - mw, my + 0.035 * D), (fx, my - 0.03 * D), (fx + mw, my + 0.035 * D)], lwf, curve=True)
    elif mouth == "smirk":
        line(ctx, [(fx - mw, my + 0.01 * D), (fx + mw * 0.4, my + 0.03 * D), (fx + mw * 1.2, my - 0.03 * D)], lwf, curve=True)
    elif mouth == "wave":
        pts = [(fx - mw * 1.1 + i * mw * 2.2 / 6, my + (0.015 * D if i % 2 else -0.015 * D)) for i in range(7)]
        line(ctx, pts, lwf)
    elif mouth in ("grin", "O", "shout"):
        ctx.new_path()
        if mouth == "grin":
            ctx.move_to(fx - mw * 1.5, my - 0.03 * D)
            ctx.curve_to(fx - mw * 1.3, my + 0.12 * D, fx + mw * 1.3, my + 0.12 * D, fx + mw * 1.5, my - 0.03 * D)
            ctx.close_path()
        elif mouth == "O":
            ellipse(ctx, fx, my + 0.02 * D, 0.06 * D, 0.08 * D)
        else:
            rrect(ctx, fx - mw * 1.3, my - 0.04 * D, mw * 2.6, 0.13 * D, 0.02 * D)
        path = ctx.copy_path()
        set_color(ctx, PAL["mouth"])
        ctx.fill()
        # top teeth row
        ctx.save()
        ctx.append_path(path)
        ctx.clip()
        ctx.rectangle(fx - 0.2 * D, my - 0.06 * D, 0.4 * D, 0.065 * D if mouth != "O" else 0.0)
        set_color(ctx, PAL["paper"])
        ctx.fill()
        ctx.restore()
        ctx.append_path(path)
        fill_stroke(ctx, None, lwf)
    if sweat:
        sx, sy = fx + 0.47 * D, cy - 0.18 * D
        ctx.move_to(sx, sy - 0.10 * D)
        ctx.curve_to(sx + 0.07 * D, sy, sx + 0.05 * D, sy + 0.07 * D, sx, sy + 0.07 * D)
        ctx.curve_to(sx - 0.05 * D, sy + 0.07 * D, sx - 0.07 * D, sy, sx, sy - 0.10 * D)
        ctx.close_path()
        fill_stroke(ctx, PAL["sweat"], f.lw(4))


# ---------------------------------------------------------------- crowd & silhouettes
def crowd(f, members, lw_px=4.5, cheer=False, base_alpha=1.0, arms=True):
    """Grey desaturated crowd (no faces). members = list of (x, y_feet, h, seed).
    arms=False for big foreground crowds cut by the frame edge: raised rubber-hose arms would
    cross the neighbours' heads (QC finding SH060), so they cheer by bobbing only."""
    look = Look("crowd", cls="crowd", skin="#BDBDBF", body=PAL["crowd"])
    out = []
    for (x, y, h, sd) in members:
        tone = 0.86 + 0.14 * ((sd * 0.37) % 1)
        lk = replace(look, skin=mix("#8C8C90", "#C2C2C4", tone), body=mix("#7E7E83", "#B3B3B6", (tone * 1.7) % 1))
        bob = 0.0
        pose = "idle"
        if cheer:
            on = int((f.T * FPS + sd * 5) // 9) % 2
            bob = -h * 0.03 * on
            pose = "arms_up" if on else "shrug"
        if not arms:
            pose = "none"
        draw(f, lk, x, y + bob, h, pose=pose, seed=sd, lw_px=lw_px, breathe=False, shadow_floor=False)
        out.append((x, y))
    return out


def silhouette(f, x, y, h, kind="round", seed=0, ticket=None):
    """Mystery class: ink silhouette with a subtle rim; optional white ticket in hand."""
    look = Look("sil", cls="silhouette", hair={"round": None, "tall": "short", "bun": "bun", "curly": "curly"}.get(kind),
                width={"wide": 1.25}.get(kind, 1.0))
    if kind == "antenna":
        look = replace(look, hair=None)
    a = draw(f, look, x, y, h, pose="hold_r" if ticket else "idle", seed=seed, lw_px=6, shadow_floor=True)
    ctx = f.ctx
    hx_, hy_ = a["head"]
    R = a["R"]
    if kind == "antenna":
        line(ctx, [(hx_, hy_ - R), (hx_ + R * 0.1, hy_ - R * 1.55)], f.lw(6), hx("#0E0C0D"))
        circle(ctx, hx_ + R * 0.1, hy_ - R * 1.62, R * 0.14)
        fill_stroke(ctx, "#2A2526", f.lw(5), hx("#0E0C0D"))
    # rim light on the head (lit from the stage behind)
    ctx.new_path()
    ctx.arc(hx_, hy_, R - f.lw(5), math.radians(200), math.radians(290))
    set_color(ctx, "#6B6280", 0.9)
    ctx.set_line_width(f.lw(4))
    ctx.stroke()
    if ticket:
        from .props import ticket as _ticket
        hxr, hyr = a["hand_r"]
        _ticket(f, hxr + 6, hyr - 18, 88, ticket, angle=-0.18)
    return a
