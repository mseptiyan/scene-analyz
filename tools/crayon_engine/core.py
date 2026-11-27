"""Core: canvas constants, colour tokens, easing, frame context and camera.

All drawing happens in *world* coordinates of a 1920x1080 stage. The camera maps world to screen.
Stroke widths are given in *screen* pixels through `f.lw(px)`, which divides by the current zoom.
That keeps outline thickness constant while the camera drifts (QC: "outline does not thicken
or thin on zoom").
"""
from __future__ import annotations

import colorsys
import math
from dataclasses import dataclass, field

W, H, FPS = 1920, 1080, 30

# ---- colour tokens (references/lighting_and_color.md §2, original Crayon Verse palette) ----
PAL = {
    "ink": "#1A1617",
    "paper": "#FDFDFB",
    "paper_shade": "#C9CAD0",
    "crowd": "#A9A9AD",
    "crowd_dark": "#8C8C90",
    "skin1": "#F2D3B0", "skin1_sh": "#D9AE8A",
    "skin2": "#C98F63", "skin2_sh": "#A8704A",
    "skin3": "#8C5B3E", "skin3_sh": "#6E432C",
    "money": "#4FAE5A", "money_sh": "#2F7C3B", "money_lt": "#8FD08A",
    "loss": "#D9363E", "loss_sh": "#A8232B",
    "gold": "#F2B630", "gold_sh": "#C98A12",
    "mouth": "#7A1E25", "tongue": "#C4505A",
    "sweat": "#9ED8F0",
    "anon": "#A6A6AB", "anon_sh": "#8A8A90", "anon_hair": "#6E6E74",
}


def hx(c):
    """'#RRGGBB' -> (r, g, b) floats. Tuples pass through."""
    if isinstance(c, tuple):
        return c
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) / 255 for i in (0, 2, 4))


def shade(c, k: float = 0.8, hue_shift: float = 0.035):
    """Cel shadow tone: value x0.75-0.85, hue nudged toward blue/violet (lighting §3/§4)."""
    r, g, b = hx(c)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    target = 0.66  # blue-violet
    dh = (target - h + 0.5) % 1.0 - 0.5
    h = (h + max(-hue_shift, min(hue_shift, dh))) % 1.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (r * k, g * k, b * k)


def tint(c, k: float = 1.15):
    r, g, b = hx(c)
    return tuple(min(1.0, v * k + (k - 1) * 0.15) for v in (r, g, b))


def mix(a, b, t):
    a, b = hx(a), hx(b)
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def desat(c, amount=0.7):
    r, g, b = hx(c)
    y = 0.299 * r + 0.587 * g + 0.114 * b
    return tuple(v + (y - v) * amount for v in (r, g, b))


# ---- easing ----
def clamp(x, a=0.0, b=1.0):
    return a if x < a else b if x > b else x


def lerp(a, b, t):
    return a + (b - a) * t


def ease_out(p):
    p = clamp(p)
    return 1 - (1 - p) ** 3


def ease_in(p):
    p = clamp(p)
    return p ** 3


def ease_in_out(p):
    p = clamp(p)
    return 4 * p ** 3 if p < 0.5 else 1 - (-2 * p + 2) ** 3 / 2


def pop(t: float, t0: float, dur: float = 7 / 30, peak: float = 1.08) -> float:
    """Pop-in scale with overshoot (motion standard: 6-8 f, 105-110%).
    0 -> peak at 60% of dur (ease-out), -> 0.985 at 82%, settle to 1.0."""
    p = (t - t0) / dur
    if p <= 0:
        return 0.0
    if p >= 1:
        return 1.0
    if p < 0.6:
        return peak * ease_out(p / 0.6)
    if p < 0.82:
        return lerp(peak, 0.985, ease_in_out((p - 0.6) / 0.22))
    return lerp(0.985, 1.0, ease_out((p - 0.82) / 0.18))


def shake(t: float, t0: float, amp: float = 10, frames: int = 6, seed: int = 1):
    """Impact shake: 4-8 frames with decay. Returns (dx, dy)."""
    n = (t - t0) * FPS
    if n < 0 or n > frames:
        return 0.0, 0.0
    d = (1 - n / frames) ** 2
    return amp * d * math.sin(n * 2.7 + seed), amp * d * math.cos(n * 3.1 + seed * 2)


# ---- camera ----
@dataclass
class Camera:
    """Constant-speed drift camera (reference: 94/158 shots drift 2-8 %/s, ~linear).

    z0 -> z1 linearly over the shot. focus0 -> focus1 is the world point at screen centre.
    Pull-out: z0 > z1 (reveal). Push-in: z0 < z1 (emphasis). Locked-off: z0 == z1.
    The focus is clamped so the visible window never leaves the 1920x1080 stage.
    """
    z0: float = 1.0
    z1: float = 1.0
    focus0: tuple = (W / 2, H / 2)
    focus1: tuple | None = None

    def at(self, t: float, dur: float):
        p = clamp(t / dur) if dur > 0 else 0
        z = lerp(self.z0, self.z1, p)
        f1 = self.focus1 or self.focus0
        fx, fy = lerp(self.focus0[0], f1[0], p), lerp(self.focus0[1], f1[1], p)
        z = max(z, 1.0)
        hw, hh = W / 2 / z, H / 2 / z
        fx = clamp(fx, hw, W - hw)
        fy = clamp(fy, hh, H - hh)
        return z, fx, fy

    def rate_per_s(self, dur: float) -> float:
        return 0.0 if dur <= 0 else (self.z1 - self.z0) / self.z0 / dur


def drift(rate: float, dur: float, focus=(W / 2, H / 2), focus_end=None, z_end: float = 1.0):
    """Camera that drifts at `rate` (e.g. +0.04 = push-in 4 %/s, -0.04 = pull-out 4 %/s)."""
    if rate >= 0:
        return Camera(1.0, 1.0 * (1 + rate * dur), focus, focus_end)
    z0 = z_end / (1 + rate * dur)
    return Camera(z0, z_end, focus, focus_end)


@dataclass
class Frame:
    ctx: object
    t: float          # shot-local seconds
    T: float          # global seconds
    dur: float        # shot duration
    zoom: float = 1.0
    shot_id: str = ""
    data: dict = field(default_factory=dict)

    def lw(self, px: float) -> float:
        """Line width in world units that renders as `px` screen pixels."""
        return px / self.zoom

    @property
    def n(self) -> int:  # frame index within shot
        return int(round(self.t * FPS))
