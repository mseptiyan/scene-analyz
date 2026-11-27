"""Chapter 5 (The Next Rockets on the Pad, lines 94-111) + bookend + end card."""
from __future__ import annotations

import math

from common import (C, LE, LS, PAL, S, T, W, H, bg, cal, cam, ch, chapter_card, clamp, ease_in_out, ease_out, fx,
                    label, lerp, p2, pop, pop_label, popped, pr, scaled, text, wlabel, write_on_chars)
from crayon_engine.character import Look
from crayon_engine.core import FPS, Camera
from crayon_engine.draw import circle, fill_stroke, line
from looks import ELON, RETAIL

# generic company mascots (no logos, neutral colours, named only by handwritten labels)
AI_A = Look("AI company A", body="#5B8C7A", inner="#E9F2EE")
AI_B = Look("AI company B", body="#4A6FA5", glasses="round")


def _antenna(f, a):
    hx_, hy_ = a["head"]
    R = a["R"]
    line(f.ctx, [(hx_, hy_ - R), (hx_ + R * 0.1, hy_ - R * 1.55)], f.lw(7))
    circle(f.ctx, hx_ + R * 0.1, hy_ - R * 1.62, R * 0.14)
    fill_stroke(f.ctx, PAL["gold"], f.lw(5))


QUEUE = [(1610, "antenna", 330), (1728, "round", 300), (1846, "wide", 340)]


def _queue(f, reveal_a=None, reveal_b=None):
    for i, (x, kind, hh) in enumerate(QUEUE):
        if i == 0 and reveal_a is not None and f.T >= reveal_a:
            a = ch.draw(f, AI_A, x, 860, hh, expr="grin", pose="hold_r", seed=500)
            _antenna(f, a)
            pr.ticket(f, a["hand_r"][0] + 6, a["hand_r"][1] - 18, 88, "IPO", angle=-0.18)
        elif i == 1 and reveal_b is not None and f.T >= reveal_b:
            a = ch.draw(f, AI_B, x, 860, hh, expr="smug", pose="hold_r", seed=501)
            pr.ticket(f, a["hand_r"][0] + 6, a["hand_r"][1] - 18, 88, "IPO", angle=-0.18)
        else:
            ch.silhouette(f, x, 860, hh, kind=kind, seed=i + 5, ticket="IPO")


def sh940(f):  # Remember the queue at the launch pad? The next giants are taking off.
    bg.launch_pad_night(f, t=f.T)
    ch.draw(f, ELON, 960, 880, 440, expr="happy", pose="idle", seed=6)
    _queue(f)


def sh950(f):  # Nov 18: Anthropic priced its IPO at $83
    bg.launch_pad_night(f, t=f.T)
    ta = T(95, "Anthropic")
    _queue(f, reveal_a=ta)
    if f.T >= ta:
        fx.sparkle(f, 1560, 420, 30, f.T)
    wlabel(f, "Anthropic", 1610, 380, ta + 0.1, 60, color=PAL["paper"], arrow_to=(1610, 470))
    if f.T >= T(95, "eighty"):
        popped(f, T(95, "eighty"), 1250, 640, lambda: p2.price_tag(f, 1250, 640, 300, "$83", angle=0.12))
    if f.T >= T(95, "November"):
        cal(f, 1280, 300, 190, "NOV 18", "2026")


def sh960(f):  # raised $81.3B, more than SpaceX's original 75
    bg.white_void(f, disc_y=950, disc_rx=820)
    p2.money_tower(f, 640, 950, 280, 600, top_label="$75B", label="SpaceX (June)")
    t0 = T(96, "eighty")
    h = 650 * ease_out((f.T - t0) / 0.8) if f.T >= t0 else 0
    if h > 1:
        p2.money_tower(f, 1280, 950, 280, h, color="#8FB8A8", top_label="$81.3B" if f.T >= t0 + 0.8 else None,
                       label="Anthropic (Nov)")


def sh965(f):  # its shares jumped on day one, then slid back... Sound familiar?
    bg.night_grid(f)
    x, y, w, h = 300, 220, 1100, 560
    pts = [(0, 0.25), (0.15, 0.85), (0.35, 0.7), (0.6, 0.45), (0.8, 0.3), (1.0, 0.27)]
    p = ease_in_out((f.T - LS("96b")) / 2.4)
    pr.chart(f, x, y, w, h, pts, progress=max(0.003, p), color=PAL["money"] if p < 0.4 else PAL["loss"])
    iy = y + (1 - 0.25) * h
    f.ctx.save()
    f.ctx.set_dash([16, 14])
    line(f.ctx, [(x, iy), (x + w, iy)], f.lw(4), (0.85, 0.85, 0.9))
    f.ctx.restore()
    text(f.ctx, "IPO price", x + w - 140, iy - 18, 40, color="#DDE3EA", kind="hand")
    text(f.ctx, "Anthropic, first days (simplified)", x, y + h + 64, 38, color="#9CC3DA", kind="hand", align="left")
    tf = T("96b", "Sound")
    ch.draw(f, ELON, 1650, 960, 380, expr="smug" if f.T >= tf else "neutral", pose="hips", seed=505, facing=-0.3)
    if f.T >= tf:
        fx.exclaim(f, 1740, 520, 90, "?", color=PAL["gold"])


def _tower_fn(val, color="#7DBF73"):
    def fn(f, x, y):
        top = p2.money_tower(f, x, y - 8, 120, 40 + val * 1.3, color=color)
        text(f.ctx, f"${val}B", x, top - 22, 52, color=PAL["paper"], kind="marker", stroke=PAL["ink"],
             stroke_px=f.lw(5))
    return fn


def scale_shot(line_id, left_val, right_val, tilt_to, left_name, right_name):
    def draw(f):
        bg.office(f, "#5B6B7D")
        t0 = LS(line_id)
        tilt = tilt_to * ease_out((f.T - t0 - 0.3) / 0.8) if tilt_to else 0.12 * math.sin(f.T * 3)
        p2.balance_scale(f, 960, 960, 860, tilt, left=_tower_fn(left_val), right=_tower_fn(right_val, "#8FB8A8"))
        text(f.ctx, left_name, 430, 860, 52, color=PAL["paper"], kind="hand", stroke=PAL["ink"], stroke_px=f.lw(4))
        text(f.ctx, right_name, 1490, 860, 52, color=PAL["paper"], kind="hand", stroke=PAL["ink"], stroke_px=f.lw(4))
        if not tilt_to:
            fx.exclaim(f, 960, 170, 120, "??", color=PAL["gold"])
    return draw


def sh1000(f):  # Next in line: OpenAI, the maker of ChatGPT.
    bg.launch_pad_night(f, t=f.T)
    tb = T(100, "Open")
    _queue(f, reveal_a=-1, reveal_b=tb)
    wlabel(f, "OpenAI", 1728, 380, tb + 0.1, 60, color=PAL["paper"], arrow_to=(1728, 500))
    wlabel(f, "next in line?", 1200, 260, T(100, "Next"), 56, color=PAL["gold"])


def sh1010(f):  # filed in secret, aiming for 2027, reported valuations above $1T
    bg.office(f, "#4D6E8C")
    p2.envelope(f, 640, 520, 520, angle=-0.08)
    if f.T >= T(101, "twenty"):
        cal(f, 1300, 470, 320, "2027?", "TARGET")
    wlabel(f, "> $1 trillion (reported)", 1300, 900, T(101, "valuations"), 64, color=PAL["gold"])
    wlabel(f, "filed in secret", 640, 860, T(101, "secret"), 56)


def sh1015(f):  # Databricks and Stripe often named, no dates set
    bg.launch_pad_night(f, t=f.T)
    for i, x in enumerate((760, 1160)):
        ch.silhouette(f, x, 880, 360 + i * 20, kind=("bun", "wide")[i], seed=520 + i, ticket="IPO?")
    wlabel(f, "Databricks?", 760, 380, T("101b", "Databricks"), 58)
    wlabel(f, "Stripe?", 1160, 360, T("101b", "Stripe"), 58)
    wlabel(f, "no dates set", 960, 1020, T("101b", "dates"), 60, color=PAL["gold"])


def sh1020(f):  # So what can the SpaceX story teach us?
    bg.office(f, "#6A5B8C")
    p2.whiteboard(f, 900, 460, 1000, 560)
    wlabel(f, "5 LESSONS", 900, 380, T(102, "teach"), 110, color=PAL["loss"])
    ch.draw(f, ELON, 1600, 960, 440, expr="happy", pose="point", seed=530, facing=-0.6)


def _icon(kind):
    def fn(f, x, y, s):
        if kind == "popcorn":
            p2.popcorn(f, x, y, s / 220, popped=1.0)
        elif kind == "calendar":
            pr.calendar(f, x, y + 10, s * 0.7, ["DEC 8"], f.T, f.T + 99, sub="UNLOCK")
        elif kind == "pizza":
            pr.pizza(f, x, y, s * 0.42, slices=12)
        elif kind == "diary":
            p2.diary(f, x, y, s * 0.95, [("RISKS", PAL["loss"], 0.8)], cover="S-1")
        elif kind == "tag":
            p2.price_tag(f, x, y, s * 0.9, "$$$", angle=-0.1)
    return fn


LESSONS = [(103, "1", "A pop is not a promise", "popcorn", "#E0A020"),
           (104, "2", "Check the lock-up calendar", "calendar", "#2E9C9A"),
           (105, "3", "Watch for dilution", "pizza", "#3F9E4D"),
           (106, "4", "Read the S-1 (the risks!)", "diary", "#D9363E"),
           (107, "5", "Famous is not the same as cheap", "tag", "#7A5CC2")]


def lesson_shot(line_id, num, caption, icon, color):
    def draw(f):
        bg.white_void(f, floor=False)
        k = pop(f.T, f.T - f.t - 2 / 30)
        scaled(f.ctx, 640, 520, k)
        p2.counter_number(f, 380, 640, 360, num, color=color)
        f.ctx.restore()
        popped(f, LS(line_id) + 0.25, 1120, 470, lambda: _icon(icon)(f, 1120, 470, 520))
        wlabel(f, caption, 960, 960, LS(line_id) + 0.35, 78, color=color, cps=30)
    return draw


def sh1080(f):  # SpaceX is still building rockets, satellites and AI computers.
    bg.day_pad(f)
    pr.rocket(f, 520, 520, 520)
    p2.satellite(f, 1020, 300, 1.4, 0.25 + 0.05 * math.sin(f.T))
    for i in range(3):
        p2.server_rack(f, 1260 + i * 170, 840, 140, 460, f.T, i)


def sh1090(f):  # Whether its stock reaches Mars is a different story.
    bg.space(f, t=f.T)
    p2.planet(f, 1600, 300, 190)
    pts = [(0, 0.2), (0.15, 0.6), (0.3, 0.35), (0.45, 0.7), (0.6, 0.4), (0.75, 0.55), (0.9, 0.45)]
    pr.chart(f, 200, 380, 1100, 520, pts, progress=1.0, color=PAL["gold"], grid=False, glow="#F2B630", lw_px=8)
    pr.rocket(f, 1180 + 30 * f.t, 560 - 20 * f.t, 240, angle=0.9, flame=0.8 + 0.2 * math.sin(f.T * 20))
    wlabel(f, "Mars?", 1600, 560, T(109, "Mars"), 70, color=PAL["paper"])


def sh1100(f):  # BOOKEND: what goes up has to fight gravity (callback of hook SH060)
    bg.launch_pad_night(f, t=f.T)
    t0 = f.T - f.t
    fx.confetti(f, f.T, n=120, t_start=t0 - 1.5, x0=150, x1=1770)
    _queue(f, reveal_a=-1, reveal_b=-1)
    n = int((f.T - t0) * FPS) // 21
    expr, pose = (("proud", "hips"), ("grin", "wave"))[n % 2]
    ch.draw(f, ELON, 960, 880, 440, expr=expr, pose=pose, seed=6, wave_phase=f.T)
    members = [(x, 1335 + (i % 2) * 30, 430 + (i * 37 % 60), i + 1) for i, x in enumerate(range(-40, 2000, 150))]
    ch.crowd(f, members, cheer=True, lw_px=5, arms=False)
    wlabel(f, "gravity", 960, 300, T(110, "gravity"), 96, color=PAL["gold"])


def sh1110(f):  # end card
    bg.card(f)
    c = write_on_chars(f.T, f.T - f.t + 0.1, 26)
    text(f.ctx, "Education, not financial advice.", 960, 470, 92, color=PAL["paper"], kind="script", chars=c)
    if f.t > 1.2:
        text(f.ctx, "Sources for every number: see the description.", 960, 600, 46, color="#BDBDBD", kind="hand")
    if f.t > 1.8:
        text(f.ctx, "The SpaceX IPO Explained Like You're 5", 960, 720, 40, color="#8C8C90", kind="hand")


def shots():
    return [
        S("SH935", chapter_card(5, "The Next Rockets on the Pad"), LS("card_ch05"), None, "Card", camtxt="locked-off", action="Chapter card write-on", txt="Chapter 5", sfx="ticks"),
        S("SH940", sh940, C(94), lambda d: Camera(1.0, 1.25, (960, 560), (1500, 600)), "WS -> MS", camtxt="push-in toward the queue ~5%/s",
          action="Callback to the hook: launch pad and queue of silhouettes", expr="happy"),
        S("SH950", sh950, C(95), cam(0.02, (1400, 560)), "MS", camtxt="push-in 2%/s", action="Silhouette 1 turns into a generic AI character; $83 tag; NOV 18",
          expr="grin", txt="Anthropic, $83, NOV 18", sfx="sparkle, pop"),
        S("SH960", sh960, C(96), cam(-0.025), "Infographic", camtxt="pull-out 2.5%/s", action="Two towers: $75B vs $81.3B", txt="$75B SpaceX, $81.3B Anthropic", sfx="cash"),
        S("SH965", sh965, C("96b"), cam(0.02), "Infographic", camtxt="push-in 2%/s", action="Up-then-down line; Elon side-eyes the camera", expr="smug", txt="IPO price, ?", sfx="whoosh_down"),
        S("SH970", scale_shot(97, 75, 81.3, 0, "SpaceX", "Anthropic"), C(97), cam(0.02), "WS", camtxt="push-in 2%/s", action="Balance scale wobbles", txt="??"),
        S("SH980", scale_shot(98, 85.7, 81.3, -1, "SpaceX (with greenshoe)", "Anthropic"), C(98), cam(0.02), "WS", camtxt="push-in 2%/s", action="Scale tips to SpaceX", txt="$85.7B vs $81.3B", sfx="thud"),
        S("SH990", scale_shot(99, 75, 81.3, 1, "SpaceX (starting deal)", "Anthropic"), C(99), cam(-0.02), "WS", camtxt="pull-out 2%/s", action="Scale tips to Anthropic", txt="$75B vs $81.3B", sfx="thud"),
        S("SH1000", sh1000, C(100), cam(0.03, (1600, 560)), "MS", camtxt="push-in 3%/s", action="Silhouette 2 turns into a generic AI character", txt="OpenAI, next in line?", sfx="sparkle"),
        S("SH1010", sh1010, C(101), cam(0.02), "MS", camtxt="push-in 2%/s", action="Confidential envelope; calendar 2027?", txt="filed in secret, 2027?, > $1 trillion (reported)"),
        S("SH1015", sh1015, C("101b"), cam(-0.02), "WS", camtxt="pull-out 2%/s", action="More silhouettes with 'IPO?' tickets", txt="Databricks?, Stripe?, no dates set"),
        S("SH1020", sh1020, C(102), cam(0.025), "WS", camtxt="push-in 2.5%/s", action="Elon points at a whiteboard", expr="happy", txt="5 LESSONS"),
    ] + [S(f"SH10{3 + i}0", lesson_shot(*ls), C(ls[0]), cam(0.02), "Infographic", camtxt="push-in 2%/s",
           action=f"Lesson {ls[1]}: number + icon pop", txt=ls[2], sfx="pop") for i, ls in enumerate(LESSONS)] + [
        S("SH1080", sh1080, C(108), cam(-0.025), "WS", camtxt="pull-out 2.5%/s", action="Day pad: rocket, satellite, server racks"),
        S("SH1090", sh1090, C(109), None, "WS", camtxt="locked-off (rocket moves)", action="Rocket heads for Mars over a wobbly stock line", txt="Mars?"),
        S("SH1100", sh1100, C(110), lambda d: Camera(1.32, 1.0, (820, 470), (960, 540)), "MS -> WS (bookend)", camtxt="pull-out ~2.8%/s",
          action="BOOKEND of SH060: same launch pad, confetti, pose swap, crowd + queue (now revealed)", expr="proud <-> grin", txt="gravity", sfx="sparkle"),
        S("SH1110", sh1110, C(111), None, "Card", camtxt="locked-off", action="End card write-on", txt="Education, not financial advice.", trans="end"),
    ]


def cues():
    c = [(LS("card_ch05") + 0.15, "tick", 0), (LS("card_ch05") + 0.6, "tick", -2),
         (T(95, "Anthropic"), "sparkle", -2), (T(95, "eighty"), "pop", -2), (T(96, "eighty"), "cash", -4),
         (LS("96b"), "whoosh_down", -6), (LS(98) + 0.3, "thud", -4), (LS(99) + 0.3, "thud", -4),
         (T(100, "Open"), "sparkle", -2), (T(102, "teach"), "tick", 0)]
    c += [(C(ls[0]) + 0.02, "pop", -1) for ls in LESSONS]
    c += [(LS(ls[0]) + 0.25, "pop", -4) for ls in LESSONS]
    c += [(C(110), "sparkle", 0), (C(111) + 0.2, "tick", -2)]
    return c
