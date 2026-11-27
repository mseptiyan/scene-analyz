"""PILOT (~60 s): hook + chapter 1 opening of "The SpaceX IPO Explained Like You're 5".

Every hard cut is derived from the VO word timestamps (`Words.cut`, lead 0.2 s before the
phrase), so re-recording the VO re-times the whole edit automatically.

    python pilot.py render   [audio_dir] [out.mp4]
    python pilot.py stills   [audio_dir] [qc_dir]      # A/M/Z frames per shot + contact sheet
    python pilot.py shotlist [audio_dir] [shotlist.md]
"""
from __future__ import annotations

import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
sys.path.insert(0, HERE)

from crayon_engine import backgrounds as bg  # noqa: E402
from crayon_engine import character as ch  # noqa: E402
from crayon_engine import fx  # noqa: E402
from crayon_engine import props as pr  # noqa: E402
from crayon_engine.core import FPS, PAL, H, W, clamp, drift, ease_in_out, ease_out, lerp, pop, shake  # noqa: E402
from crayon_engine.core import Camera  # noqa: E402
from crayon_engine.draw import INK, circle, fill_stroke, rrect, set_color  # noqa: E402
from crayon_engine.text import balloon, label, multiline, text, write_on_chars  # noqa: E402
from crayon_engine.timeline import Shot, Timeline, Words  # noqa: E402
from looks import BIG_FUND, BOUNCER, ELON, EMPLOYEE, FOUNDER_FRIEND, RETAIL  # noqa: E402

AUD = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("PILOT_AUDIO", "/home/user/work/spacex-ipo/audio")
WD = Words(os.path.join(AUD, "words.json"), os.path.join(AUD, "lines.json"))
T = WD.t          # T(line, token) -> global seconds of a word
VO_END = WD.line(17)["end"]
END_CARD = VO_END + 1.25
TOTAL = round(END_CARD + 3.0, 2)


def scaled(ctx, x, y, s):
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(max(s, 1e-3), max(s, 1e-3))
    ctx.translate(-x, -y)


def pop_label(f, s, x, y, t0, size=54, color=PAL["paper"], arrow_to=None, write=False):
    k = pop(f.T, t0)
    if k <= 0:
        return
    scaled(f.ctx, x, y, k)
    chars = write_on_chars(f.T, t0, 28) if write else None
    label(f.ctx, f, s, x, y, size, color=color, arrow_to=arrow_to, chars=chars)
    f.ctx.restore()


# ============================================================ HOOK
def sh010(f):  # "One company sold tiny slices of itself,"
    bg.white_void(f, disc_y=880)
    a = ch.draw(f, ELON, 960, 880, 600, expr="smug", pose="hold_r", anon=True, seed=3, hands=True)
    hx_, hy_ = a["hand_r"]
    pr.certificate(f, hx_ + 40, hy_ - 30, 120, angle=-0.12)


def sh020(f):  # "for $135 each."
    bg.white_void(f, floor=False)
    ctx = f.ctx
    # the certificate is already in frame on the cut (no pop on a hard cut = no near-empty frame)
    pr.certificate(f, 960, 540, 820, angle=-0.05, chars=write_on_chars(f.T, T(1, "one", 1), 10))
    if f.T >= T(1, "each"):
        fx.sparkle(f, 1360, 300, 34, f.T)
        fx.sparkle(f, 560, 760, 24, f.T, 1.3)


def sh030(f):  # "It raised seventy-five billion dollars."
    bg.white_void(f, disc_y=905, disc_rx=640)
    fx.money_rain(f, f.t, n=26, t_start=0.15, x0=200, x1=1720)  # behind the hero: FX never covers the face
    sx, sy = pr.money_mountain(f, 960, 905, 1040)
    ch.draw(f, ELON, sx, sy + 30, 300, expr="grin", pose="arms_up", anon=True, seed=4, shadow_floor=False)
    if f.T >= T(2, "seventy"):
        label(f.ctx, f, "$75,000,000,000", 960, 150, 112, color=PAL["gold"],
              chars=write_on_chars(f.T, T(2, "seventy"), 16))


PTS_UP = [(0.0, 0.10), (0.10, 0.16), (0.18, 0.13), (0.30, 0.30), (0.40, 0.26), (0.52, 0.48), (0.62, 0.44),
          (0.74, 0.70), (0.84, 0.66), (0.97, 0.93)]


def sh040(f):  # "In three days, the stock jumped two-thirds."
    bg.night_grid(f)
    ctx = f.ctx
    x, y, w, h = 300, 210, 1300, 620
    p = max(0.004, ease_in_out((f.t - 0.15) / 1.35))
    tip, ang = pr.chart(f, x, y, w, h, PTS_UP, progress=p, rocket_tip=True, flame=0.6 + 0.4 * math.sin(f.t * 20))
    for i, u in enumerate((0.17, 0.5, 0.83)):
        text(ctx, f"Day {i + 1}", x + u * w, y + h + 70, 46, color="#9CC3DA", kind="hand")
    label(ctx, f, "$135", x - 10, y + h * 0.95 + 70, 58, color=PAL["paper"])
    if p > 0.88:
        pop_label(f, "$225", tip[0] - 40, tip[1] + 150, f.T - f.t + 0.15 + 1.35 * 0.88, size=64)
        pop_label(f, "+67%", tip[0] - 330, tip[1] + 40, f.T - f.t + 0.15 + 1.35 * 0.88 + 0.12, size=96,
                  color=PAL["money_lt"])


def sh050(f):  # "Then, it lost over half its value."
    bg.crisis_desk(f)
    t0 = 0.0
    p = ease_out((f.t - t0) / 0.5)
    x = lerp(2400, 960, p)
    ang = lerp(0.45, -0.06, p)
    pr.newspaper(f, x, 520, 1080, "THE DAILY ORBIT", "SPACE STOCK CUT IN HALF", angle=ang)
    if f.T >= T(4, "half"):
        k = pop(f.T, T(4, "half"))
        scaled(f.ctx, 1510, 230, k)
        fx.exclaim(f, 1510, 260, 140, "!!")
        f.ctx.restore()


# reveal: the face turns colour exactly on the word "SpaceX"
REVEAL = None


def sh060(f):  # "This is the story of the SpaceX IPO..." + "And the wildest part? The next giants..."
    bg.launch_pad_night(f, t=f.T)
    rv = T(5, "SpaceX")
    revealed = f.T >= rv
    if revealed:
        fx.confetti(f, f.T, n=120, t_start=rv, x0=150, x1=1770)
    # queue of next giants (right), hidden by the initial framing, revealed by the pull-out
    for i, (k, hh) in enumerate([("antenna", 330), ("round", 300), ("wide", 340)]):
        ch.silhouette(f, 1610 + i * 118, 860, hh, kind=k, seed=i + 5, ticket="IPO")
    if revealed:
        n = int((f.T - rv) * FPS) // 21  # instant pose swap every ~0.7 s, no in-betweens
        expr, pose = (("proud", "hips"), ("grin", "wave"))[n % 2]
        ch.draw(f, ELON, 960, 880, 440, expr=expr, pose=pose, seed=6, wave_phase=f.T)
        if f.T >= rv + 0.25:
            label(f.ctx, f, "Elon Musk", 1290, 330, 56, arrow_to=(1050, 430), chars=write_on_chars(f.T, rv + 0.25, 24))
    else:
        ch.draw(f, ELON, 960, 880, 440, expr="neutral", pose="idle", anon=True, seed=6)
    # cheering grey crowd in the foreground (revealed by the pull-out)
    members = [(x, 1335 + (i % 2) * 30, 430 + (i * 37 % 60), i + 1) for i, x in enumerate(range(-40, 2000, 150))]
    ch.crowd(f, members, cheer=revealed, lw_px=5, arms=False)


def sh070(f):  # chapter card (black, handwritten write-on)
    bg.card(f)
    c = write_on_chars(f.T, f.T - f.t + 0.12, 26)
    text(f.ctx, "Chapter 1", 960, 440, 70, color="#BDBDBD", kind="script", chars=c)
    text(f.ctx, "What Even Is an IPO?", 960, 610, 140, color=PAL["paper"], kind="script",
         chars=max(0, c - len("Chapter 1")))


# ============================================================ CHAPTER 1
def sh080(f):  # "Imagine a company is a giant pizza."
    bg.gold_radial(f)
    ctx = f.ctx
    tp = T(7, "pizza")
    if f.T < tp:
        k = pop(f.T, f.T - f.t - 2 / 30)  # pre-rolled pop: already ~45% on the cut frame (no empty frame)
        if k > 0:
            scaled(ctx, 960, 800, k)
            from crayon_engine.draw import contact_shadow
            contact_shadow(ctx, 960, 800, 220)
            pr.building(f, 960, 800, 320, 420)
            ctx.restore()
    else:
        k = pop(f.T, tp)
        scaled(ctx, 960, 540, k)
        from crayon_engine.draw import contact_shadow
        contact_shadow(ctx, 960, 860, 300)
        pr.pizza(f, 960, 540, 300)
        ctx.restore()


def sh090(f):  # "Every share is one tiny slice."
    bg.gold_radial(f)
    lift = 0.55 * ease_out((f.T - T(8, "share")) / 0.5)
    pr.pizza(f, 900, 580, 360, missing=1, lift=lift)
    if f.T >= T(8, "slice"):
        label(f.ctx, f, "1 share", 1520, 260, 76, arrow_to=(1330, 330), chars=write_on_chars(f.T, T(8, "slice"), 18))


YEARS = [str(y) for y in range(2002, 2027, 2)]


def sh100(f):  # "For twenty-four years,"
    bg.white_void(f, disc_y=860, disc_rx=420)
    t0 = T("9-11", "For") + 0.2
    pr.calendar(f, 960, 500, 440, YEARS, f.T, t0, flip_dur=2 / 30, interval=0.075, sub="YEAR")
    if f.T >= T("9-11", "years"):
        pop_label(f, "24 years", 960, 940, T("9-11", "years"), size=74, color=PAL["gold"])


CLUB = [(EMPLOYEE, "happy"), (ELON, "proud"), (BIG_FUND, "smug"), (FOUNDER_FRIEND, "smug")]


def sh110(f):  # "SpaceX only sold its slices to a private club:"
    bg.club_red(f)
    for i, (lk, ex) in enumerate(CLUB):
        x = 640 + i * 215
        a = ch.draw(f, lk, x, 760, 330, expr=ex, pose="hold_r", seed=10 + i)
        pr.pizza_slice(f, (a["hand_r"][0] - 10, a["hand_r"][1] - 6), 52, 1)
    pr.rope_line(f, 380, 1540, 930, post_h=210, n_posts=3, sag=46)
    pr.plaque(f, 960, 830, "MEMBERS ONLY", w=380)
    ch.draw(f, BOUNCER, 250, 980, 470, expr="angry", seed=19)


def sh120(f):  # "founders, employees, and big investors."
    bg.club_red(f, spot=(960, 520))
    xs = [520, 860, 1200, 1500]
    for (lk, ex), x in zip(CLUB, xs):
        a = ch.draw(f, lk, x, 930, 470, expr=ex, pose="hold_r", seed=30 + int(x))
        pr.pizza_slice(f, (a["hand_r"][0] - 10, a["hand_r"][1] - 8), 70, 1)
    pop_label(f, "FOUNDER", 860, 300, T("9-11", "founders"), size=60)
    pop_label(f, "EMPLOYEE", 520, 300, T("9-11", "employees"), size=60)
    pop_label(f, "BIG INVESTORS", 1350, 250, T("9-11", "big"), size=60)


def sh130(f):  # "Everyone else was stuck behind the rope."
    bg.club_red(f, spot=(1100, 430))
    rnd = [(x, 700 + (i % 3) * 22, 300 + (i * 53 % 80), 40 + i) for i, x in enumerate(range(60, 1500, 120))]
    ch.crowd(f, rnd)
    ch.draw(f, RETAIL[0], 960, 800, 420, expr="worried", pose="sad", seed=41)
    # reverse angle of SH110: the bouncer (screen-left, outside the rope there) is now screen-right,
    # on the crowd side of the rope (180-degree rule)
    a = ch.draw(f, BOUNCER, 1600, 1000, 560, expr="angry", seed=42, pose="hips")
    pr.rope_line(f, 80, 1400, 900, post_h=200, n_posts=3, sag=40)
    ts = T(12, "stuck")
    if f.T >= ts:
        k = pop(f.T, ts)
        balloon(f.ctx, f, "Members only.", 1330, 250, a["mouth"], size=58, scale=k)


def sh140(f):  # "An IPO, or initial public offering, is the day the doors swing open."
    bg.blue_wall(f)
    op = ease_out((f.T - T(13, "swing")) / 0.45) if f.T >= T(13, "swing") else 0.0
    pr.doors(f, 960, 930, 560, 600, open_p=op, sign="IPO")
    happy = op > 0.3
    ch.draw(f, RETAIL[1], 470, 960, 380, expr="sparkle" if happy else "neutral", facing=0.6, seed=51)
    ch.draw(f, RETAIL[2], 1450, 960, 400, expr="sparkle" if happy else "thinking", facing=-0.6, seed=52)
    ti = T(13, "initial")
    if f.T >= ti:
        label(f.ctx, f, "Initial Public Offering", 1440, 170, 50, arrow_to=(1140, 210),
              chars=write_on_chars(f.T, ti, 28))
    if op > 0:
        fx.sparkle(f, 800, 380, 30 * op, f.T)
        fx.sparkle(f, 1110, 520, 22 * op, f.T, 2.0)


INVESTORS = [(RETAIL[0], 330), (RETAIL[1], 600), (RETAIL[3], 1320), (RETAIL[4], 1590)]


def sh150(f):  # "The company sells slices to anyone, on a public stock market, like the Nasdaq."
    bg.market_hall(f)
    pr.ticker_strip(f, 70, 84, f.T, [("SPCX", True), ("ABC", False), ("XYZ", True), ("PIZZA", True), ("QRS", False)])
    ts = T(14, "sells")
    # company (Elon) at the counter with the pizza
    ch.draw(f, ELON, 960, 760, 380, expr="grin", pose="hold", seed=61, shadow_floor=False)
    rrect(f.ctx, 700, 700, 520, 230, 14)
    fill_stroke(f.ctx, "#2A6F8F", f.lw(8))
    pr.pizza(f, 960, 690, 120, missing=None)
    for i, (lk, x) in enumerate(INVESTORS):
        t_go = ts + 0.15 + i * 0.32
        got = f.T >= t_go + 0.45
        a = ch.draw(f, lk, x, 960, 390, expr="grin" if got else "happy", pose="hold_r", seed=70 + i,
                    facing=0.5 if x < 960 else -0.5)
        hxp, hyp = a["hand_r"]
        pr.phone(f, hxp + 8, hyp - 6, 62, angle=0.15)
        if f.T >= t_go:  # slice flies along an arc from the pizza to the investor
            p = ease_in_out((f.T - t_go) / 0.45)
            sx, sy, ex_, ey_ = 960, 640, hxp - 4, hyp - 80
            px = lerp(sx, ex_, p)
            py = lerp(sy, ey_, p) - math.sin(math.pi * p) * 240
            pr.pizza_slice(f, (px, py), 58, 1)
    tn = T(14, "Nasdaq")
    if f.T >= tn:
        label(f.ctx, f, "the Nasdaq", 960, 250, 88, color=PAL["gold"], arrow_to=(1180, 150),
              chars=write_on_chars(f.T, tn, 20))


def _icon_first(f, x, y, s):
    ctx = f.ctx
    circle(ctx, x, y, s * 0.42)
    fill_stroke(ctx, PAL["paper"], f.lw(6))
    text(ctx, "1st", x, y + s * 0.16, s * 0.42, color=PAL["ink"], kind="marker")


def _icon_people(f, x, y, s):
    for i, dx in enumerate((-0.33, 0.33, 0.0)):
        ch.draw(f, RETAIL[i], x + dx * s, y + s * (0.55 if i < 2 else 0.62), s * (0.85 if i < 2 else 0.95),
                expr="happy", seed=80 + i, lw_px=6, shadow_floor=False)


def _icon_tag(f, x, y, s):
    ctx = f.ctx
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(-0.3)
    ctx.move_to(-s * 0.45, -s * 0.22)
    ctx.line_to(s * 0.25, -s * 0.22)
    ctx.line_to(s * 0.48, 0)
    ctx.line_to(s * 0.25, s * 0.22)
    ctx.line_to(-s * 0.45, s * 0.22)
    ctx.close_path()
    fill_stroke(ctx, PAL["paper"], f.lw(6))
    circle(ctx, s * 0.24, 0, s * 0.05)
    fill_stroke(ctx, PAL["gold"], f.lw(4))
    text(ctx, "$", -s * 0.1, s * 0.12, s * 0.34, color=PAL["money_sh"], kind="marker")
    ctx.restore()


CARDS = [("INITIAL", "first time", 15, "Initial", "#E0A020", _icon_first),
         ("PUBLIC", "anyone can buy", 16, "Public", "#2E9C9A", _icon_people),
         ("OFFERING", "the company sells", 17, "Offering", "#3F9E4D", _icon_tag)]


def sh160(f):  # "Initial: it's the first time. Public: anyone can buy. Offering: the company is selling."
    bg.white_void(f, floor=False)
    for i, (word, sub, ln, tok, col, icon) in enumerate(CARDS):
        t0 = max(T(ln, tok) - 0.2, f.T - f.t - 2 / 30)
        k = pop(f.T, t0)
        if k <= 0:
            continue
        x = 480 + i * 480
        pr.word_card(f, x, 500, 400, word, col, icon=icon, s=k)
        if f.T >= t0 + 0.25:
            text(f.ctx, sub, x, 860, 56, color=PAL["ink"], kind="hand", chars=write_on_chars(f.T, t0 + 0.25, 22))


def sh170(f):  # end slate
    bg.card(f)
    c = write_on_chars(f.T, f.T - f.t + 0.25, 22)
    text(f.ctx, "To be continued...", 960, 560, 120, color=PAL["paper"], kind="script", chars=c)
    if f.t > 1.2:
        text(f.ctx, "PILOT  ·  The SpaceX IPO Explained Like You're 5", 960, 690, 40, color="#8C8C90", kind="hand")


# ============================================================ timeline
def cam(rate, focus=(W / 2, H / 2), focus_end=None):
    return lambda d: drift(rate, d, focus, focus_end)


def build():
    c = WD.cut
    S = [
        Shot("SH010", sh010, 0.0, cam(0.03, (960, 560)),
             dict(size="MS", angle="eye-level frontal", cam="push-in 3%/s", action="Anonymous grey-faced man holds a tiny share certificate", expr="smug (grey face)", txt="—", sfx="bed in", trans="hard cut")),
        Shot("SH020", sh020, c(1, "for"), cam(0.04),
             dict(size="ECU insert", angle="frontal", cam="push-in 4%/s", action="Certificate fills frame; '$135' writes on with the VO", expr="—", txt="$135 / 1 SHARE", sfx="pop, tick", trans="hard cut")),
        Shot("SH030", sh030, c(2), cam(0.02, (960, 520)),
             dict(size="WS", angle="frontal", cam="push-in 2%/s", action="Same man on a mountain of money sacks; bills rain on ones", expr="grin (grey face)", txt="$75,000,000,000", sfx="cash", trans="hard cut")),
        Shot("SH040", sh040, c(3), cam(-0.045, (1000, 520)),
             dict(size="Infographic", angle="frontal", cam="pull-out 4.5%/s", action="Green line draws on with rocket tip, Day 1-3", expr="—", txt="$135, $225, +67%", sfx="riser", trans="hard cut")),
        Shot("SH050", sh050, c(4), cam(0.03, (960, 520)),
             dict(size="Insert", angle="top-ish frontal", cam="push-in 3%/s", action="Generic newspaper slides in and stops; '!!' pops on 'half'", expr="—", txt="THE DAILY ORBIT: SPACE STOCK CUT IN HALF", sfx="whoosh, thud", trans="hard cut")),
        Shot("SH060", sh060, c(5), lambda d: Camera(1.32, 1.0, (820, 470), (960, 540)),
             dict(size="MS -> WS (reveal)", angle="eye-level", cam="pull-out ~2.8%/s", action="Face turns colour on 'SpaceX'; pose swap every 21 f; confetti; pull-out reveals cheering grey crowd + queue of silhouettes with IPO tickets", expr="proud <-> grin (swap)", txt="Elon Musk (label)", sfx="sparkle, pop", trans="hard cut to card")),
        Shot("SH070", sh070, WD.line("card_ch01")["start"], None,
             dict(size="Card", angle="—", cam="locked-off", action="Black card, handwritten write-on", expr="—", txt="Chapter 1 / What Even Is an IPO?", sfx="pencil ticks", trans="hard cut")),
        Shot("SH080", sh080, c(7), cam(0.02, (960, 540)),
             dict(size="MS", angle="frontal", cam="push-in 2%/s", action="Office in frame on the cut (pre-rolled pop), instantly swaps to a pizza on 'pizza'", expr="—", txt="—", sfx="pop x2", trans="hard cut")),
        Shot("SH090", sh090, c(8), cam(0.05, (900, 560), (1050, 470)),
             dict(size="CU", angle="frontal", cam="push-in 5%/s", action="One slice lifts out of the pizza", expr="—", txt="1 share", sfx="whoosh (small), tick", trans="hard cut")),
        Shot("SH100", sh100, c("9-11"), cam(0.025, (960, 560)),
             dict(size="Insert", angle="frontal", cam="push-in 2.5%/s", action="Desk calendar flips 2002 -> 2026", expr="—", txt="YEAR 2002..2026, 24 years", sfx="page flips", trans="hard cut")),
        Shot("SH110", sh110, c("9-11", "SpaceX"), cam(0.03, (960, 600)),
             dict(size="WS", angle="frontal", cam="push-in 3%/s", action="Velvet-rope club: 4 members with slices behind the rope, bouncer in front", expr="proud / smug / angry", txt="MEMBERS ONLY", sfx="—", trans="hard cut")),
        Shot("SH120", sh120, c("9-11", "founders"), cam(-0.03, (960, 560)),
             dict(size="MS lineup", angle="frontal", cam="pull-out 3%/s", action="Lineup of 4 holding slices; labels pop on each word", expr="happy / proud / smug", txt="FOUNDER, EMPLOYEE, BIG INVESTORS", sfx="pop x3", trans="hard cut")),
        Shot("SH130", sh130, c(12), cam(0.025, (1000, 560)),
             dict(size="MS (reverse angle)", angle="eye-level", cam="push-in 2.5%/s", action="Reverse angle: grey crowd behind the rope, worried retail investor, bouncer now screen-right (180° rule) with balloon", expr="worried (+sweat) / angry", txt="Members only.", sfx="boing", trans="hard cut")),
        Shot("SH140", sh140, c(13), cam(0.03, (960, 500)),
             dict(size="WS", angle="frontal", cam="push-in 3%/s", action="Doors with IPO sign swing open on 'swing'; light floods; onlookers swap to sparkle eyes", expr="neutral/thinking -> sparkle", txt="IPO, Initial Public Offering", sfx="door shimmer", trans="hard cut")),
        Shot("SH150", sh150, c(14), cam(-0.03, (960, 560)),
             dict(size="WS", angle="frontal", cam="pull-out 3%/s", action="Elon at the counter; slices fly on arcs to retail investors with phones; ticker scrolls", expr="happy -> grin", txt="ticker, the Nasdaq", sfx="cash, pops", trans="hard cut")),
        Shot("SH160", sh160, c(15), cam(0.02, (960, 560)),
             dict(size="Infographic", angle="frontal", cam="push-in 2%/s", action="Three word cards pop in on each word", expr="—", txt="INITIAL / PUBLIC / OFFERING + captions", sfx="pop x3", trans="hard cut")),
        Shot("SH170", sh170, END_CARD, None,
             dict(size="Card", angle="—", cam="locked-off", action="End slate write-on", expr="—", txt="To be continued...", sfx="ticks, bed out", trans="end")),
    ]
    return Timeline(S, TOTAL)


def sfx_cues():
    return [
        (T(1, "one", 1), "tick", 0), (T(1, "one", 1) + 0.12, "tick", -2),
        (T(2, "raised"), "cash", 0),
        (WD.cut(3) + 0.05, "riser", -2),
        (WD.cut(4), "whoosh", 0), (WD.cut(4) + 0.48, "thud", 0), (T(4, "half"), "pop", -4),
        (T(5, "SpaceX"), "sparkle", 2), (T(5, "SpaceX"), "pop", -2),
        (WD.line("card_ch01")["start"] + 0.15, "tick", 0), (WD.line("card_ch01")["start"] + 0.55, "tick", -2),
        (WD.line("card_ch01")["start"] + 0.95, "tick", -1),
        (WD.cut(7) + 0.03, "pop", 0), (T(7, "pizza"), "pop", 2),
        (T(8, "share"), "whoosh", -8), (T(8, "slice"), "tick", 0),
    ] + [(T("9-11", "For") + 0.2 + i * 0.075, "flip", -3) for i in range(len(YEARS) - 1)] + [
        (T("9-11", "founders"), "pop", -2), (T("9-11", "employees"), "pop", -2), (T("9-11", "big"), "pop", -2),
        (T(12, "stuck"), "boing", -2),
        (T(13, "swing"), "door", 0),
        (T(14, "sells"), "cash", -3),
    ] + [(T(14, "sells") + 0.15 + i * 0.32 + 0.45, "pop", -6) for i in range(4)] + [
        (T(14, "Nasdaq"), "tick", 0),
        (T(15, "Initial") - 0.17, "pop", 0), (T(16, "Public") - 0.17, "pop", 0), (T(17, "Offering") - 0.17, "pop", 0),
        (END_CARD + 0.3, "tick", -2), (END_CARD + 0.8, "tick", -3),
    ]


def tc(sec):
    m, s = divmod(sec, 60)
    return f"{int(m):02d}:{s:05.2f}"


def write_shotlist(tl, path):
    from crayon_engine.core import Camera as _C
    rows = []
    lines = {str(l["id"]): l for l in WD.lines.values()}
    for i, s in enumerate(tl.shots, 1):
        m = s.meta
        camr = s.camera().rate_per_s(s.dur) * 100
        # which VO phrase starts in this shot, and how far before it the cut lands
        first = next((w for w in WD.words if s.start <= w["start"] < s.end), None)
        lead = f"{first['start'] - s.start:.2f}" if first else "—"
        vo = " ".join(w["word"] for w in WD.words if s.start <= w["start"] < s.end) or "— (no VO)"
        rows.append(f"| {i} | {s.id} | {tc(s.start)} | {s.dur:.2f}s | {m['size']} / {m['angle']} | {m['cam']} "
                    f"(measured {camr:+.1f}%/s) | {m['action']} | {m['expr']} | {m['txt']} | {m['sfx']} | {m['trans']} "
                    f"| {lead} | {vo} |")
    hdr = ("# Shot list: PILOT (hook + chapter 1 opening)\n\n"
           "Format: `workflows/pre_production.md` §7.3, plus two sync columns. **Generated from the locked timeline** "
           "(`pilot.py shotlist`), so the timecodes are the real cut points of the rendered pilot. Every cut is computed from the "
           "VO word timestamps: `cut = start of the phrase's first word − 0.20 s` (rule: 1 phrase = 1 shot, cut 0.1–0.3 s before the phrase).\n\n"
           f"Total: {tl.total:.2f} s · {len(tl.shots)} shots · median shot "
           f"{sorted(s.dur for s in tl.shots)[len(tl.shots)//2]:.2f} s · 30 fps · 1920×1080\n\n"
           "| # | Shot ID | TC in | Dur | Size/Angle | Camera | Characters & action | Expression | On-screen text | SFX/Music | Transition out | Cut→VO lead (s) | VO in shot |\n"
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    open(path, "w").write(hdr + "\n".join(rows) + "\n")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "render"
    tl = build()
    if mode == "render":
        from crayon_engine import audio, render
        out = sys.argv[3] if len(sys.argv) > 3 else "/home/user/work/spacex-ipo/render/spacex_ipo_pilot.mp4"
        os.makedirs(os.path.dirname(out), exist_ok=True)
        import numpy as np
        import soundfile as sf
        vo, sr = sf.read(os.path.join(AUD, "vo_master.wav"), dtype="float64")
        pad = np.zeros(int(TOTAL * sr) - vo.size + int(0.05 * sr))
        sf.write(os.path.join(AUD, "_vo_padded.wav"), np.concatenate([vo, pad]), sr, subtype="PCM_24")
        mixwav = os.path.join(AUD, "mix_pilot.wav")
        stats = audio.mix(os.path.join(AUD, "_vo_padded.wav"), sfx_cues(), mixwav)
        print("mix", stats)
        render.render(tl, out, mixwav, os.path.join(os.path.dirname(out), "_work"))
        print("rendered", out)
    elif mode == "stills":
        from crayon_engine import render
        qc = sys.argv[3] if len(sys.argv) > 3 else "/home/user/work/spacex-ipo/qc"
        os.makedirs(qc, exist_ok=True)
        for s in tl.shots:
            for tag, tt in (("A", s.start + 1 / FPS), ("M", (s.start + s.end) / 2), ("Z", s.end - 2 / FPS)):
                render.still(tl, tt, os.path.join(qc, f"{s.id}_{tag}.png"))
        print("stills ok")
    elif mode == "srt":
        out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, "pilot.srt")

        def ts(x):
            h, r = divmod(x, 3600)
            m, sec = divmod(r, 60)
            return f"{int(h):02d}:{int(m):02d}:{int(sec):02d},{int(round((sec % 1) * 1000)):03d}"
        rows = [l for l in WD.lines.values() if l["say"]]
        with open(out, "w") as fh:
            for k, l in enumerate(rows, 1):
                txt = l["say"].replace("I.P.O.", "IPO").replace("one hundred and thirty-five dollars", "$135")
                txt = txt.replace("seventy-five billion dollars", "$75 billion").replace("twenty-four", "24")
                fh.write(f"{k}\n{ts(l['start'])} --> {ts(l['end'] + 0.15)}\n{txt}\n\n")
        print("srt ->", out)
    elif mode == "shotlist":
        out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, "shotlist.md")
        write_shotlist(tl, out)
        print("shotlist ->", out)
