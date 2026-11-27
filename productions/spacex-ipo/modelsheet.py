"""Render the pilot model sheet (characters.md): lineup, expression bank, anon vs revealed hero."""
import os
import sys

import cairo

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
from crayon_engine import backgrounds as bg  # noqa: E402
from crayon_engine import character as ch  # noqa: E402
from crayon_engine.core import H, W, Frame  # noqa: E402
from crayon_engine.text import label, text  # noqa: E402
from looks import BIG_FUND, BOUNCER, ELON, EMPLOYEE, FOUNDER_FRIEND, RETAIL  # noqa: E402


def sheet(path):
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(s)
    f = Frame(ctx=ctx, t=0.5, T=0.5, dur=1)
    bg.white_void(f, floor=False)
    text(ctx, "The SpaceX IPO: model sheet v1 (pilot)", 40, 64, 52, color="#1A1617", align="left", kind="marker")
    # row 1: anon -> revealed hero, extras, crowd, silhouettes
    y = 520
    ch.draw(f, ELON, 150, y, 400, expr="neutral", anon=True, seed=1)
    text(ctx, "hook: anonymous", 150, y + 60, 34, color="#1A1617")
    ch.draw(f, ELON, 400, y, 400, expr="proud", seed=2, pose="hips")
    text(ctx, "Elon (hero)", 400, y + 60, 34, color="#1A1617")
    xs = [620, 790, 960, 1130, 1300]
    for x, lk, ex in zip(xs, [RETAIL[0], RETAIL[1], RETAIL[2], FOUNDER_FRIEND, BIG_FUND],
                         ["happy", "worried", "grin", "smug", "neutral"]):
        ch.draw(f, lk, x, y, 330, expr=ex, seed=x, pose="idle")
    text(ctx, "extras: white heads", 960, y + 60, 34, color="#1A1617")
    ch.draw(f, BOUNCER, 1480, y, 360, expr="angry", seed=9)
    ch.crowd(f, [(1640, y, 260, 1), (1720, y, 300, 2), (1800, y, 250, 3)])
    text(ctx, "crowd: grey", 1720, y + 60, 34, color="#1A1617")
    # row 2: expression bank on the hero
    exprs = ["neutral", "happy", "proud", "grin", "sparkle", "shock", "sad", "worried", "angry", "thinking", "smug", "shout"]
    for i, e in enumerate(exprs):
        x = 110 + i * 150
        ch.draw(f, ELON, x, 980, 260, expr=e, seed=i + 20, blink=False, breathe=False, shadow_floor=False)
        text(ctx, e, x, 1040, 28, color="#1A1617", kind="hand")
    s.write_to_png(path)


def sil(path):
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, W // 2, H // 2)
    ctx = cairo.Context(s)
    ctx.scale(0.5, 0.5)
    f = Frame(ctx=ctx, t=0.5, T=0.5, dur=1)
    bg.launch_pad_night(f)
    for i, (k, h) in enumerate([("antenna", 420), ("round", 380), ("bun", 360), ("wide", 400)]):
        ch.silhouette(f, 1100 + i * 190, 930, h, kind=k, seed=i, ticket="IPO")
    s.write_to_png(path)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "assets")
    os.makedirs(out, exist_ok=True)
    sheet(os.path.join(out, "modelsheet_pilot.png"))
    sil(os.path.join(out, "modelsheet_silhouettes.png"))
    print("ok")
