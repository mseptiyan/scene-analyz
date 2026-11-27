"""Chapter 3 (Liftoff, lines 51-64) and Chapter 4 (Gravity Always Wins, lines 65-93)."""
from __future__ import annotations

import math

from common import (C, LE, LS, PAL, S, T, W, H, bg, cal, cam, ch, chapter_card, clamp, ease_in_out, ease_out, fx,
                    label, lerp, p2, pop, pop_label, popped, pr, punch_card, scaled, shake, text, wlabel, write_on_chars)
from crayon_engine.draw import INK, line, rrect, set_color
from looks import BIG_FUND, ELON, EMPLOYEE, FOUNDER_FRIEND, RETAIL

# --- SPCX price path (simplified). Labelled points are real (sources.md B1, B4, C3-C7, C9, C11);
#     the line between them is illustrative and the chart says so on screen.
PATH = [(0, 135), (0.25, 150), (0.5, 176.52), (1, 160.95), (2, 192), (3, 225.64), (4, 196), (5, 172), (12, 160),
        (20, 135), (31, 108.66), (34, 118), (36, 104.83), (38, 108.27), (39, 114.92), (44, 155.1), (55, 150),
        (70, 138), (90, 147.79), (91, 165), (100, 150), (110, 122), (116, 127.44)]


def _xy(box, lo, hi, d0, d1, day, price):
    x, y, w, h = box
    return x + (day - d0) / (d1 - d0) * w, y + (1 - (price - lo) / (hi - lo)) * h


def price_chart(f, d0, d1, progress, lo=90, hi=240, box=(300, 200, 1340, 620), rocket=False, flags=(), ipo=True,
                color=None, caption="SPCX (simplified)", flame=0.8):
    """Draw PATH between days d0..d1, revealed up to `progress`. flags = [(day, text, colour, dy)]."""
    x, y, w, h = box
    pts = [(d, p) for d, p in PATH if d0 <= d <= d1]
    norm = [((d - d0) / (d1 - d0), (p - lo) / (hi - lo)) for d, p in pts]
    if ipo:
        iy = _xy(box, lo, hi, d0, d1, d0, 135)[1]
        f.ctx.save()
        f.ctx.set_dash([16, 14])
        line(f.ctx, [(x, iy), (x + w, iy)], f.lw(4), (0.85, 0.85, 0.9))
        f.ctx.restore()
        text(f.ctx, "IPO $135", x + w + 20, iy + 14, 40, color="#DDE3EA", kind="hand", align="left")
    last = pts[-1][1] if progress >= 1 else None
    col = color or (PAL["money"] if (pts[-1][1] >= pts[0][1]) else PAL["loss"])
    tip, ang = pr.chart(f, x, y, w, h, norm, progress=max(0.003, progress), color=col, rocket_tip=rocket, flame=flame)
    text(f.ctx, caption, x, y + h + 64, 38, color="#9CC3DA", kind="hand", align="left")
    # reveal flags once the line has passed them
    seg = [math.dist(_xy(box, lo, hi, d0, d1, *pts[i]), _xy(box, lo, hi, d0, d1, *pts[i + 1])) for i in range(len(pts) - 1)]
    total = sum(seg)
    acc = 0.0
    passed = {pts[0][0]: 0.0}
    for i, s_ in enumerate(seg):
        acc += s_
        passed[pts[i + 1][0]] = acc / total
    for (day, s, c, dy) in flags:
        if progress + 1e-6 >= passed.get(day, 2):
            px, py = _xy(box, lo, hi, d0, d1, day, dict(PATH)[day])
            from crayon_engine.draw import circle, fill_stroke
            circle(f.ctx, px, py, 12)
            fill_stroke(f.ctx, c, f.lw(5))
            label(f.ctx, f, s, px, py + dy, 52, color=c)
    return tip, ang


# ------------------------------------------------------------------ CHAPTER 3
def sh510(f):  # June twelfth, 2026. The opening bell.
    bg.white_void(f, disc_y=900)
    cal(f, 640, 520, 400, "JUN 12", "2026")
    tb = T(51, "bell")
    sw = 0.35 * math.sin((f.T - tb) * 18) * math.exp(-(f.T - tb) * 2.5) if f.T >= tb else 0
    p2.bell(f, 1330, 520, 1.6, sw)
    if f.T >= tb:
        fx.exclaim(f, 1600, 300, 90, "DING!", color=PAL["gold"])


def sh520(f):  # SPCX opened at $150, above the IPO price.
    bg.night_grid(f)
    rrect(f.ctx, 460, 300, 1000, 360, 20)
    from crayon_engine.draw import fill_stroke
    fill_stroke(f.ctx, "#0A1520", f.lw(8))
    to = T(52, "opened")
    v = "$135" if f.T < to + 0.3 else "$150"
    text(f.ctx, "SPCX", 960, 420, 90, color="#9CC3DA", kind="marker", tracking=0.1)
    text(f.ctx, v, 960, 590, 170, color=PAL["money_lt"] if v == "$150" else PAL["paper"], kind="marker")
    if v == "$150":
        from crayon_engine.draw import poly
        poly(f.ctx, [(1210, 580), (1290, 580), (1250, 500)])
        fill_stroke(f.ctx, PAL["money_lt"], f.lw(5))
    wlabel(f, "above the IPO price", 960, 850, T(52, "above"), 64, color=PAL["gold"])


DAY1 = [(0, 135), (0.12, 150), (0.45, 168), (0.6, 176.52), (0.8, 158), (1.0, 160.95)]


def sh530(f):  # high $176 that day, closed $160.95, +19%
    bg.night_grid(f)
    x, y, w, h = 320, 220, 1280, 580
    lo, hi = 125, 185
    p = ease_in_out((f.T - LS(53)) / max(1.0, LE(53) - LS(53) - 1.2))
    norm = [(u, (v - lo) / (hi - lo)) for u, v in DAY1]
    pr.chart(f, x, y, w, h, norm, progress=max(0.003, p), color=PAL["money"])
    pts = {k: (x + u * w, y + (1 - (v - lo) / (hi - lo)) * h) for k, (u, v) in zip(("ipo", "open", "m", "high", "d", "close"), DAY1)}
    if f.T >= T(53, "seventy"):
        label(f.ctx, f, "high $176.52", pts["high"][0], pts["high"][1] - 50, 54, color=PAL["paper"])
    if f.T >= T(53, "sixty"):
        label(f.ctx, f, "close $160.95", pts["close"][0] - 60, pts["close"][1] + 90, 54, color=PAL["paper"])
    pop_label(f, "+19%", 1500, 300, T(53, "nineteen"), 120, color=PAL["money_lt"])
    text(f.ctx, "Day 1 (June 12)", x, y + h + 64, 40, color="#9CC3DA", kind="hand", align="left")


def sh540(f):  # worth over two trillion dollars
    bg.gold_radial(f)
    fx.confetti(f, f.T, n=90, t_start=T(54, "two"))
    ch.draw(f, ELON, 960, 960, 420, expr="sparkle", pose="arms_up", seed=300)
    wlabel(f, "$2,000,000,000,000+", 960, 300, T(54, "worth"), 120, color=PAL["gold"], cps=22)


def sh550(f):  # Headlines called Musk the world's first trillionaire.
    bg.gold_radial(f)
    p = ease_out(f.t / 0.5)
    pr.newspaper(f, lerp(-600, 960, p), 520, 1080, "THE DAILY ORBIT", "FIRST TRILLIONAIRE?", angle=lerp(-0.4, 0.05, p),
                 chart=False)
    if p > 0.95:
        ch.draw(f, ELON, 1250, 880, 220, expr="sparkle", seed=301, shadow_floor=False, lw_px=6)


def sh560(f):  # A first-day jump like this is called an IPO pop.
    bg.white_void(f, disc_y=860)
    tp = T(56, "pop")
    p2.popcorn(f, 960, 520, 2.0, popped=clamp((f.T - tp) / 0.25))
    pop_label(f, "IPO POP", 960, 900, tp, 120, color=PAL["gold"])
    if f.T >= tp:
        fx.exclaim(f, 1300, 330, 90, "POP!", color=PAL["loss"])


def sh570(f):  # The IPO price is set before trading starts.
    bg.blue_wall(f)
    pr.doors(f, 960, 930, 560, 600, open_p=0.0)
    p2.price_tag(f, 960, 640, 300, "$135", angle=0.12)
    wlabel(f, "set BEFORE trading starts", 960, 1010, T(57, "set"), 58, color=PAL["gold"])


def sh580(f):  # more people want it than there are shares: buyers bid the price up
    bg.market_hall(f)
    tb = T(58, "bid")
    price = "$135" if f.T < tb else ("$150" if f.T < tb + 0.5 else "$176")
    rrect(f.ctx, 700, 150, 520, 170, 16)
    from crayon_engine.draw import fill_stroke
    fill_stroke(f.ctx, "#0A1520", f.lw(7))
    text(f.ctx, price, 960, 280, 120, color=PAL["money_lt"], kind="marker")
    for i in range(7):
        x = 240 + i * 240
        up = f.T >= tb + i * 0.08
        a = ch.draw(f, RETAIL[i % 5], x, 980, 360, expr="grin" if up else "happy", pose="hold_r" if up else "idle",
                    seed=310 + i, facing=0.3 if x < 960 else -0.3)
        if up:
            p2.paddle(f, a["hand_r"][0], a["hand_r"][1] - 70, 1.0, 10 + i * 7)


def sh590(f):  # left money on the table
    bg.office(f, "#7A6A5A")
    p2.table_front(f, 900, 720, 900, 220)
    for i in range(5):
        p2.money_tower(f, 640 + i * 130, 722, 100, 26 * (1 + i % 3), color="#7DBF73")
    ch.draw(f, ELON, 1560, 940, 440, expr="thinking", seed=320, facing=-0.7)
    wlabel(f, "money left on the table?", 900, 300, LS(59) + 0.3, 70, color=PAL["gold"])


def sh595(f):  # maybe it sold its slices too cheaply
    bg.gold_radial(f)
    pr.pizza_slice(f, (700, 560), 260, 1)
    p2.price_tag(f, 1240, 540, 520, "$135", angle=-0.12)
    pop_label(f, "too cheap?", 1240, 860, T("59b", "cheaply"), 90, color=PAL["paper"])


def sh600(f):  # But the rocket kept climbing. + June 16, third day, touched $225.64
    bg.night_grid(f)
    t0, t1 = LS(60), T(61, "two")
    p = ease_in_out((f.T - t0) / max(1.0, t1 - t0))
    price_chart(f, 0, 3, p, lo=120, hi=240, rocket=True, flags=[(3, "$225.64", PAL["paper"], 110)],
                caption="SPCX, days 1-3 (simplified)", flame=0.6 + 0.4 * math.sin(f.T * 20))
    if f.T >= T(61, "June"):
        cal(f, 1720, 860, 220, "JUN 16", "2026")


def sh620(f):  # two-thirds above the IPO price in three trading days
    bg.white_void(f, floor=False)
    t0, t1 = T(62), LE(62)
    lines = ["($225.64 - $135) / $135", "=+67%  (about two-thirds)"]
    c = write_on_chars(f.T, t0, sum(len(s) for s in lines) / max(0.5, (t1 - t0) * 0.8))
    p2.chalkboard(f, 960, 520, 1400, 600, lines, chars=c, size=88)


def sh630(f):  # Early buyers felt like geniuses.
    bg.gold_radial(f)
    fx.confetti(f, f.T, n=110, t_start=f.T - f.t)
    for i, x in enumerate((420, 760, 1160, 1500)):
        n = int((f.T * 30 + i * 7) // 18) % 2
        ch.draw(f, RETAIL[i], x, 960, 400, expr="sparkle", pose="arms_up" if n else "hips", seed=330 + i)


def sh640(f):  # And then, gravity showed up.
    bg.night_grid(f)
    tip, ang = price_chart(f, 0, 3, 1.0, lo=120, hi=240, rocket=False, caption="SPCX, days 1-3 (simplified)")
    tilt = 0.25 * math.sin(f.t * 9) * ease_out(f.t / 0.6)
    pr.rocket(f, tip[0], tip[1] - 40, 140, angle=ang + math.pi / 2 + tilt + 0.4, flame=0.15 if int(f.t * 10) % 3 else 0.0)
    pop_label(f, "uh-oh", tip[0] - 120, tip[1] - 170, T(64, "gravity"), 80, color=PAL["loss"])


# ------------------------------------------------------------------ CHAPTER 4
def _weights(f, t_start, n=4, labels=("1", "2", "3", "4"), focus=None):
    pr.rocket(f, 960, 260, 300, flame=0.5 + 0.3 * math.sin(f.T * 18))
    xs = [480, 800, 1120, 1440]
    for i in range(n):
        tt = t_start + i * 0.22
        if f.T < tt:
            continue
        k = pop(f.T, tt)
        p2.chain(f, 960, 380, xs[i], 770)
        scaled(f.ctx, xs[i], 820, k)
        p2.weight(f, xs[i], 860, 1.0 if focus in (None, i + 1) else 0.8, labels[i],
                  color="#3A3D45" if focus in (None, i + 1) else "#6B6F78")
        f.ctx.restore()


def sh650(f):  # SPCX was pulled down by four weights
    bg.space(f, t=f.T)
    _weights(f, T(65, "four"))
    wlabel(f, "4 weights", 960, 1000, T(65, "four"), 64, color=PAL["gold"])


def weight_shot(num, title, line_id):
    def draw(f):
        bg.space(f, t=f.T)
        k = pop(f.T, f.T - f.t - 2 / 30)
        scaled(f.ctx, 960, 560, k)
        p2.weight(f, 960, 560, 2.2, str(num))
        f.ctx.restore()
        wlabel(f, title, 960, 960, T(line_id) + 0.15, 96, color=PAL["gold"])
    return draw


def sh670(f):  # agreed to buy Cursor for $60B, paid in stock
    bg.office(f, "#5A6E8C")
    cal(f, 240, 300, 220, "JUN 16", "2026")
    ta = T(67, "agreed")
    signed = clamp((f.T - ta) / 1.4) if f.T >= ta else 0
    pen_at = p2.contract(f, 1000, 560, 420, title="AGREEMENT", sub="BUY CURSOR", signed=signed)
    p2.pen(f, pen_at[0] + 10, pen_at[1] - 6, 1.0)
    ch.draw(f, ELON, 1520, 940, 440, expr="grin", pose="point", seed=400, facing=-0.6)
    pop_label(f, "$60B, paid in stock", 1000, 210, T(67, "sixty"), 70, color=PAL["gold"])


def sh680(f):  # cutting new slices from the same pizza
    bg.gold_radial(f)
    tc = T(68, "cutting")
    n = 8 if f.T < tc + 0.5 else 12
    pr.pizza(f, 960, 560, 330, slices=n)
    if tc <= f.T < tc + 0.9:
        p = (f.T - tc) / 0.9
        p2.knife(f, lerp(400, 1100, p), lerp(320, 700, p), 1.2, angle=0.6)
    wlabel(f, "8 slices -> 12 slices", 960, 1000, tc + 0.5, 64, color=PAL["paper"])


def sh690(f):  # every slice gets smaller: dilution
    bg.gold_radial(f)
    ts = T(69, "smaller")
    k = 1 - 0.3 * ease_out((f.T - ts) / 0.5) if f.T >= ts else 1
    f.ctx.save()
    f.ctx.set_dash([18, 14])
    from crayon_engine.draw import fill_stroke
    import cairo
    f.ctx.move_to(760, 760)
    f.ctx.arc(760, 760, 420, -math.pi / 2, -math.pi / 2 + 2 * math.pi / 8)
    f.ctx.close_path()
    set_color(f.ctx, INK)
    f.ctx.set_line_width(f.lw(5))
    f.ctx.stroke()
    f.ctx.restore()
    pr.pizza_slice(f, (760, 760 - (1 - k) * 0), 420 * k, 0)
    pop_label(f, "DILUTION", 1380, 420, T(69, "dilution"), 120, color=PAL["loss"])


def sh700(f):  # lost more than $600B in two trading days
    bg.white_void(f, disc_y=950, disc_rx=700)
    tl = T(70, "lost")
    h = 760 if f.T < tl else 760 - 300 * ease_in_out((f.T - tl) / 0.6)
    dx, dy = shake(f.T, tl + 0.5, 14)
    p2.money_tower(f, 960 + dx, 950 + dy, 320, h)
    if f.T >= tl:
        fx.money_rain(f, f.T - tl, n=18, x0=600, x1=1320, top=300, fall=(250, 380), w=80)
    pop_label(f, "-$600 billion", 960, 200, T(70, "six"), 110, color=PAL["loss"])
    wlabel(f, "in 2 trading days", 960, 1035, T(70, "two"), 52)


def sh720(f):  # insiders usually can't sell for months
    bg.club_red(f)
    for i, x in enumerate((520, 760, 1000, 1240, 1480)):
        p2.suitcase(f, x, 930, 200, color=("#8C5B3E", "#4A6FA5", "#6B2234", "#3F9E4D", "#8C5B3E")[i])
    for i, (lk, x) in enumerate(((EMPLOYEE, 640), (FOUNDER_FRIEND, 1120), (BIG_FUND, 1360))):
        ch.draw(f, lk, x, 760, 330, expr="sad", seed=410 + i, shadow_floor=False)
    wlabel(f, "LOCKED for months", 960, 230, T(72, "months"), 84, color=PAL["gold"])


def sh725(f):  # a promise that stops everyone rushing for the exit on day one
    bg.blue_wall(f)
    p2.exit_door(f, 960, 930, 420, 560, locked=True)
    for i, (lk, x) in enumerate(((RETAIL[0], 420), (EMPLOYEE, 1460), (FOUNDER_FRIEND, 1680))):
        ch.draw(f, lk, x, 960, 360, expr="worried", seed=420 + i, facing=0.6 if x < 960 else -0.6)
    wlabel(f, "a promise: no selling (yet)", 960, 200, T("72b", "promise"), 60, color=PAL["gold"])


def sh730(f):  # first unlock Aug 6: about 911 million shares
    bg.day_pad(f)
    cal(f, 300, 300, 240, "AUG 6", "2026")
    gx, gy = p2.dam(f, 700, 1500, 900, 520, t=f.T)
    p2.padlock(f, gx, gy + 30, 1.0, 1.0)
    pop_label(f, "~911 million shares", 1100, 260, T(73, "nine"), 76, color=PAL["paper"])


def sh735(f):  # almost 7% of all shares
    bg.gold_radial(f)
    p2.pie(f, 960, 540, 330, 0.069, slice_c=PAL["loss"])
    pop_label(f, "~7% of all shares", 960, 980, T("73b", "seven"), 80, color=PAL["paper"])


def sh740(f):  # worried about a flood, investors pushed the price down ahead of time
    bg.day_pad(f)
    p2.dam(f, 1300, 2000, 900, 520, t=f.T)
    t0 = f.T - f.t
    for i, lk in enumerate((RETAIL[0], RETAIL[1], RETAIL[3])):
        x = 900 - i * 260 - 260 * ease_in_out(f.t / max(1.0, f.dur))
        ch.draw(f, lk, x, 960, 360, expr="shock", pose="arms_up", seed=430 + i, facing=-0.6)
        fx.speed_lines(f, x + 160, 800, math.pi, n=4, length=90, spread=110, t=f.T, color=PAL["ink"])
    p2.big_arrow(f, 1120, 140, 300, math.pi / 2, color=PAL["loss"], width=90)
    wlabel(f, "price", 1250, 260, T(74, "price"), 60, color=PAL["loss"])
    wlabel(f, "sell first!", 520, 300, T(74, "pushed"), 70, color=PAL["loss"])


def sh750(f):  # July 27 record low under $109
    bg.night_grid(f)
    t0 = LS(75)
    p = ease_in_out((f.T - t0) / max(1.0, T(75, "under") - t0))
    price_chart(f, 3, 31, p, flags=[(31, "Jul 27: $108.66", PAL["loss"], 90)], caption="SPCX, Jun 16 - Jul 27 (simplified)")


def sh760(f):  # on unlock day the stock actually rose 6%
    bg.day_pad(f)
    gx, gy = p2.dam(f, 500, 1300, 900, 520, open_p=1.0 if f.T >= T(76, "unlock") else 0.0, t=f.T)
    ch.draw(f, ELON, 1560, 940, 420, expr="smug", pose="shrug", seed=440, facing=-0.4)
    pop_label(f, "+6%", 1560, 330, T(76, "six"), 140, color=PAL["money_lt"])
    wlabel(f, "Aug 6: unlock day", 700, 220, T(76, "unlock"), 60)


def sh765(f):  # next five trading days, +35%
    bg.night_grid(f)
    p = ease_in_out((f.T - LS("76b")) / 1.6)
    price_chart(f, 36, 44, p, lo=90, hi=170, flags=[(39, "$114.92", PAL["paper"], 90), (44, "+35% in 5 days", PAL["money_lt"], -60)],
                caption="SPCX, Aug 3 - Aug 13 (simplified)", color=PAL["money"])


def sh790(f):  # first report card as a public company
    bg.office(f, "#5A6E8C")
    cal(f, 260, 300, 220, "AUG 4", "2026")
    p2.report_card(f, 960, 560, 520, [("Revenue", "?", PAL["ink"]), ("Growth", "?", PAL["ink"]), ("Spending", "?", PAL["ink"])])
    ch.draw(f, ELON, 1520, 940, 430, expr="worried", seed=450, facing=-0.6)


def sh800(f):  # revenue +92% to $7.8B. Great!
    bg.gold_radial(f)
    tr = T(80, "Revenue")
    rows = [("Revenue (Q2)", "$7.8B" if f.T >= T(80, "seven") else "?", PAL["money_sh"]),
            ("vs last year", "+92%" if f.T >= T(80, "ninety") else "?", PAL["money_sh"]),
            ("Spending", "?", PAL["ink"])]
    p2.report_card(f, 960, 560, 620, rows, grade="A+", grade_k=pop(f.T, T(80, "Great"), peak=1.15))


def sh810(f):  # spent $18.4B in a quarter, most on AI
    bg.white_void(f, disc_y=950)
    t0 = LS(81)
    p2.receipt(f, 960, 90, 640, ease_out((f.T - t0) / 2.0),
               [("Rockets", "$"), ("Starlink", "$$"), ("AI (approx.)", "$15.8B"), ("Other", "$")], "TOTAL $18.4B / quarter",
               highlight=2 if f.T >= T(81, "most") else None, max_h=880)
    ch.draw(f, ELON, 1520, 950, 430, expr="worried", seed=455, facing=-0.6)


def sh815(f):  # chips and data centres
    bg.night_grid(f)
    for i in range(5):
        p2.server_rack(f, 360 + i * 300, 940, 220, 640, f.T, i)
    wlabel(f, "AI chips + data centers", 960, 200, T("81b", "chips"), 78, color=PAL["gold"])


def sh820(f):  # investors hate surprise bills; next day fell >10%
    bg.white_void(f, disc_y=920)
    tf = T(82, "fell")
    for i, x in enumerate((520, 820, 1120)):
        ch.draw(f, RETAIL[i], x, 920, 380, expr="shock" if f.T >= tf else "worried", seed=460 + i)
    if f.T >= tf:
        k = ease_out((f.T - tf) / 0.4)
        p2.big_arrow(f, 1450, 260, 520 * k + 1, 1.25, color=PAL["loss"], width=100)
    pop_label(f, "-10%+", 1580, 860, tf + 0.2, 120, color=PAL["loss"])
    wlabel(f, "surprise bill!", 820, 230, T(82, "surprise"), 70, color=PAL["loss"])


def sh830(f):  # Aug 3 all-time low $104.83
    bg.night_grid(f)
    t0 = LS(83)
    p = ease_in_out((f.T - t0) / max(1.0, T(83, "one") - t0))
    price_chart(f, 0, 36, p, flags=[(3, "peak $225.64", PAL["paper"], -60), (36, "Aug 3: $104.83", PAL["loss"], 90)],
                caption="SPCX, Jun 12 - Aug 3 (simplified)")


def sh840(f):  # a fall of about 53%
    bg.white_void(f, floor=False)
    t0, t1 = T(84), LE(84)
    lines = ["$225.64  ->  $104.83", "=about -53.5%"]
    c = write_on_chars(f.T, t0, sum(len(s) for s in lines) / max(0.5, (t1 - t0) * 0.8))
    p2.chalkboard(f, 960, 520, 1300, 600, lines, chars=c, size=96)


def sh860(f):  # paying for a future of Mars trips and space data centres
    bg.space(f, t=f.T)
    p2.planet(f, 1480, 420, 230)
    p2.fuel_tank(f, 700, 960, 420, 760, "EXPECTATIONS", fill_k=0.95)
    p2.satellite(f, 1250, 820, 1.2, 0.2 + 0.1 * math.sin(f.T))
    wlabel(f, "$2 trillion+ price tag", 1480, 760, T(86, "two"), 60, color=PAL["gold"])
    wlabel(f, "Mars", 1480, 160, T(86, "Mars"), 64)


def sh870(f):  # When a price assumes everything goes right...
    bg.white_void(f, disc_y=920)
    p2.glass_rocket(f, 960, 520, 620)
    for i in range(3):
        fx.sparkle(f, 760 + i * 200, 260 + (i % 2) * 300, 30, f.T, i)
    wlabel(f, "priced for perfection", 960, 1000, T(87, "everything"), 66, color=PAL["gold"])


def sh875(f):  # rocket made of glass: one pebble can crack it
    bg.white_void(f, disc_y=920)
    tp = T("87b", "pebble")
    hit = tp + 0.5
    crack = clamp((f.T - hit) / 0.5) if f.T >= hit else 0
    dx, dy = shake(f.T, hit, 12)
    p2.glass_rocket(f, 960 + dx, 520 + dy, 620, crack=crack)
    if tp <= f.T < hit:
        p = (f.T - tp) / 0.5
        from crayon_engine.draw import circle, fill_stroke
        circle(f.ctx, lerp(200, 960, p), lerp(900, 560, p), 26)
        fill_stroke(f.ctx, "#8C8C90", f.lw(6))
    if f.T >= tp:
        label(f.ctx, f, "bad news", 420, 820, 72, color=PAL["loss"])


def sh880(f):  # one AI customer = more than a third of revenue
    bg.gold_radial(f)
    p2.pie(f, 820, 540, 340, 0.345 * ease_out((f.T - T(88, "one")) / 0.6) if f.T >= T(88, "one") else 0.0,
           slice_c=PAL["loss"], label="34.5%" if f.T >= T(88, "third") else None)
    wlabel(f, "ONE AI customer (Q3)", 1440, 360, T(88, "customer"), 60, color=PAL["paper"])
    wlabel(f, "SpaceX filing: \"Customer B\"", 1440, 860, T(88, "third"), 46, color=PAL["paper"])


def sh890(f):  # Bloomberg: that customer is Anthropic; cancel with 90 days' notice from early 2027
    bg.office(f, "#5B6B7D")
    p2.contract(f, 820, 560, 420, title="COMPUTE DEAL", sub="CUSTOMER B")
    p2.exit_door(f, 1400, 900, 220, 300, label="EXIT", locked=False)
    wlabel(f, "Anthropic (per Bloomberg)", 820, 180, T(89, "Anthropic"), 62, color=PAL["gold"])
    wlabel(f, "90 days' notice", 1400, 470, T(89, "ninety"), 52)
    if f.T >= T(89, "early"):
        cal(f, 1720, 300, 200, "2027", "FROM")


def sh900(f):  # the business kept growing
    bg.day_pad(f)
    p2.factory(f, 520, 840, 620, 360, built=1.0, t=f.T)
    t0 = f.T - f.t
    lift = 220 * ease_in(clamp((f.T - t0 - 0.3) / 1.8)) if True else 0
    pr.rocket(f, 1400, 520 - lift, 380, flame=1.0)
    fx.smoke_puffs(f, 1400, 760, f.T)


def ease_in(p):
    p = clamp(p)
    return p * p


def sh910(f):  # Oct: revenue +161%, profit $4.4B
    bg.gold_radial(f)
    rows = [("Revenue (Q3)", "+161%" if f.T >= T(91, "hundred") else "?", PAL["money_sh"]),
            ("Profit", "$4.4B" if f.T >= T(91, "four") else "?", PAL["money_sh"]),
            ("Month", "October", PAL["ink"])]
    p2.report_card(f, 960, 560, 620, rows, grade="A+", grade_k=pop(f.T, T(91, "profit")))


def sh920(f):  # bounced, but by late November back below $135
    bg.night_grid(f)
    t0 = LS(92)
    p = ease_in_out((f.T - t0) / max(1.0, T(92, "below") - t0))
    price_chart(f, 36, 116, p, lo=90, hi=190,
                flags=[(91, "Oct: bounce", PAL["money_lt"], -60), (116, "Nov 25: $127.44", PAL["loss"], 90)],
                caption="SPCX, Aug 3 - Nov 25 (simplified)")


def shots():
    return [
        S("SH505", chapter_card(3, "Liftoff"), LS("card_ch03"), None, "Card", camtxt="locked-off", action="Chapter card write-on", txt="Chapter 3", sfx="ticks"),
        S("SH510", sh510, C(51), cam(0.025), "MS", camtxt="push-in 2.5%/s", action="Calendar JUN 12; bell swings on 'bell'", txt="JUN 12, DING!", sfx="bell(pop), shake"),
        S("SH520", sh520, C(52), cam(0.03), "Insert", camtxt="push-in 3%/s", action="Ticker board flips $135 -> $150", txt="SPCX $150, above the IPO price", sfx="flip"),
        S("SH530", sh530, C(53), cam(-0.03, (960, 520)), "Infographic", camtxt="pull-out 3%/s", action="Day-1 chart draws on: high, close", txt="high $176.52, close $160.95, +19%", sfx="riser, pop"),
        S("SH540", sh540, C(54), cam(-0.03), "MS", camtxt="pull-out 3%/s", action="Elon cheers, confetti, $2T writes on", expr="sparkle", txt="$2,000,000,000,000+", sfx="sparkle"),
        S("SH550", sh550, C(55), cam(0.02), "Insert", camtxt="push-in 2%/s", action="Generic newspaper slides in", txt="FIRST TRILLIONAIRE?", sfx="whoosh, thud"),
        S("SH560", sh560, C(56), cam(0.05, (960, 560)), "Insert", camtxt="push-in 5%/s", action="Kernel pops into popcorn (gag)", txt="IPO POP, POP!", sfx="pop"),
        S("SH570", sh570, C(57), cam(0.025), "WS", camtxt="push-in 2.5%/s", action="Price tag $135 hangs on the closed doors", txt="set BEFORE trading starts"),
        S("SH580", sh580, C(58), cam(-0.03), "WS", camtxt="pull-out 3%/s", action="Bidders raise paddles; price board climbs", expr="happy -> grin", txt="$135 -> $150 -> $176", sfx="pop"),
        S("SH590", sh590, C(59), cam(0.025), "WS", camtxt="push-in 2.5%/s", action="Cash left on a table; Elon looks back", expr="thinking", txt="money left on the table?"),
        S("SH595", sh595, C("59b"), cam(0.03), "Insert", camtxt="push-in 3%/s", action="Slice next to a $135 price tag", txt="too cheap?", sfx="pop"),
        S("SH600", sh600, C(60), cam(-0.025, (1000, 520)), "Infographic", camtxt="pull-out 2.5%/s", action="Rocket rides the line to the day-3 peak; calendar JUN 16", txt="$225.64, JUN 16", sfx="riser"),
        S("SH620", sh620, C(62), cam(0.02), "Insert", camtxt="push-in 2%/s", action="Chalkboard maths write-on", txt="(225.64-135)/135 = +67%"),
        S("SH630", sh630, C(63), cam(-0.03), "WS", camtxt="pull-out 3%/s", action="Retail investors celebrate, pose swaps, confetti", expr="sparkle", sfx="sparkle"),
        S("SH640", sh640, C(64), cam(0.04, (1400, 300)), "Insert", camtxt="push-in 4%/s", action="Rocket sputters and tilts at the peak", txt="uh-oh", sfx="boing", trans="hard cut to card"),
        S("SH645", chapter_card(4, "Gravity Always Wins"), LS("card_ch04"), None, "Card", camtxt="locked-off", action="Chapter card write-on", txt="Chapter 4", sfx="ticks"),
        S("SH650", sh650, C(65), cam(-0.025), "WS", camtxt="pull-out 2.5%/s", action="Rocket with 4 chained weights popping in", txt="1 2 3 4, 4 weights", sfx="thud x4"),
        S("SH660", weight_shot(1, "THE CURSOR DEAL", 66), C(66), cam(0.04), "CU", camtxt="push-in 4%/s", action="Weight #1", txt="THE CURSOR DEAL", sfx="thud"),
        S("SH670", sh670, C(67), cam(0.02), "MS", camtxt="push-in 2%/s", action="Contract signed with pen; calendar JUN 16", expr="grin", txt="BUY CURSOR, $60B, paid in stock", sfx="pop"),
        S("SH680", sh680, C(68), cam(0.025), "Insert", camtxt="push-in 2.5%/s", action="Knife adds cuts: 8 -> 12 slices", txt="8 slices -> 12 slices", sfx="whoosh"),
        S("SH690", sh690, C(69), cam(0.03), "CU", camtxt="push-in 3%/s", action="Slice shrinks inside its dashed old outline", txt="DILUTION", sfx="pop"),
        S("SH700", sh700, C(70), cam(-0.02), "Infographic", camtxt="pull-out 2%/s", action="Money tower collapses with shake", txt="-$600 billion, in 2 trading days", sfx="thud"),
        S("SH710", weight_shot(2, "THE LOCK-UP", 71), C(71), cam(0.04), "CU", camtxt="push-in 4%/s", action="Weight #2", txt="THE LOCK-UP", sfx="thud"),
        S("SH720", sh720, C(72), cam(-0.025), "WS", camtxt="pull-out 2.5%/s", action="Insiders sit by locked suitcases", expr="sad", txt="LOCKED for months"),
        S("SH725", sh725, C("72b"), cam(0.025), "WS", camtxt="push-in 2.5%/s", action="Chained EXIT door; worried figures", expr="worried", txt="a promise: no selling (yet)"),
        S("SH730", sh730, C(73), cam(0.02), "WS", camtxt="push-in 2%/s", action="Dam with a padlocked gate; calendar AUG 6", txt="AUG 6, ~911 million shares", sfx="pop"),
        S("SH735", sh735, C("73b"), cam(0.025), "Infographic", camtxt="push-in 2.5%/s", action="Pie 6.9% slice", txt="~7% of all shares", sfx="pop"),
        S("SH740", sh740, C(74), None, "WS", camtxt="locked-off (subjects move)", action="Investors flee the dam; red arrow down", expr="shock", txt="sell first!", sfx="whoosh"),
        S("SH750", sh750, C(75), cam(-0.025), "Infographic", camtxt="pull-out 2.5%/s", action="Line falls to the July 27 low", txt="Jul 27: $108.66", sfx="whoosh_down"),
        S("SH760", sh760, C(76), cam(0.03), "WS", camtxt="push-in 3%/s", action="Dam opens: only a trickle; Elon shrugs", expr="smug", txt="Aug 6: unlock day, +6%", sfx="pop"),
        S("SH765", sh765, C("76b"), cam(-0.02), "Infographic", camtxt="pull-out 2%/s", action="Line jumps up after the unlock", txt="$114.92, +35% in 5 days", sfx="riser"),
        S("SH770", punch_card(["The fear did more damage", "than the flood."], 77), C(77), None, "Card", camtxt="locked-off", action="Punchline card write-on", txt="The fear did more damage than the flood."),
        S("SH780", weight_shot(3, "SPENDING", 78), C(78), cam(0.04), "CU", camtxt="push-in 4%/s", action="Weight #3", txt="SPENDING", sfx="thud"),
        S("SH790", sh790, C(79), cam(0.025), "MS", camtxt="push-in 2.5%/s", action="Blank report card; calendar AUG 4", expr="worried", txt="AUG 4, REPORT CARD"),
        S("SH800", sh800, C(80), cam(0.02), "Insert", camtxt="push-in 2%/s", action="Report card fills; A+ stamp", txt="$7.8B, +92%, A+", sfx="thud"),
        S("SH810", sh810, C(81), cam(-0.02, (960, 400)), "Insert", camtxt="pull-out 2%/s", action="Receipt unrolls; AI line highlighted", txt="AI ~$15.8B, TOTAL $18.4B / quarter", sfx="whoosh"),
        S("SH815", sh815, C("81b"), cam(-0.03), "WS", camtxt="pull-out 3%/s", action="Rows of blinking server racks", txt="AI chips + data centers"),
        S("SH820", sh820, C(82), cam(0.03), "MS", camtxt="push-in 3%/s", action="Investors shocked; big red arrow down", expr="worried -> shock", txt="surprise bill!, -10%+", sfx="thud"),
        S("SH830", sh830, C(83), cam(-0.02), "Infographic", camtxt="pull-out 2%/s", action="Full line from the peak to the all-time low", txt="peak $225.64, Aug 3: $104.83", sfx="whoosh_down"),
        S("SH840", sh840, C(84), cam(0.02), "Insert", camtxt="push-in 2%/s", action="Chalkboard maths", txt="$225.64 -> $104.83 = about -53.5%"),
        S("SH850", weight_shot(4, "THE PRICE TAG", 85), C(85), cam(0.04), "CU", camtxt="push-in 4%/s", action="Weight #4", txt="THE PRICE TAG", sfx="thud"),
        S("SH860", sh860, C(86), cam(-0.025), "WS", camtxt="pull-out 2.5%/s", action="Mars-sized expectations tank, planet, satellite", txt="EXPECTATIONS, $2 trillion+, Mars"),
        S("SH870", sh870, C(87), cam(0.025), "MS", camtxt="push-in 2.5%/s", action="Glass rocket sparkles", txt="priced for perfection"),
        S("SH875", sh875, C("87b"), cam(0.03), "MS", camtxt="push-in 3%/s", action="Pebble hits, crack spreads, shake", txt="bad news", sfx="thud"),
        S("SH880", sh880, C(88), cam(0.02), "Infographic", camtxt="push-in 2%/s", action="Pie: one customer 34.5%", txt="ONE AI customer (Q3), 34.5%, Customer B"),
        S("SH890", sh890, C(89), cam(-0.02), "MS", camtxt="pull-out 2%/s", action="Compute contract with a small exit door", txt="Anthropic (per Bloomberg), 90 days' notice, 2027"),
        S("SH900", sh900, C(90), cam(-0.03), "WS", camtxt="pull-out 3%/s", action="Factory lights on; rocket lifts off", sfx="riser"),
        S("SH910", sh910, C(91), cam(0.02), "Insert", camtxt="push-in 2%/s", action="Q3 report card, A+", txt="+161%, $4.4B, A+", sfx="thud"),
        S("SH920", sh920, C(92), cam(-0.02), "Infographic", camtxt="pull-out 2%/s", action="Bounce, then the line slips under $135", txt="Oct: bounce, Nov 25: $127.44"),
        S("SH930", punch_card(["A great company and a great stock", "are not always the same thing."], 93, size=96), C(93), None, "Card", camtxt="locked-off", action="Punchline card write-on", txt="A great company and a great stock are not always the same thing.", trans="hard cut to card"),
    ]


def cues():
    c = [(LS("card_ch03") + 0.15, "tick", 0), (LS("card_ch03") + 0.6, "tick", -2),
         (T(51, "bell"), "sparkle", 0), (T(51, "bell"), "pop", 0), (T(52, "opened"), "flip", 0), (LS(53), "riser", -5),
         (T(53, "nineteen"), "pop", -2), (T(54, "two"), "sparkle", -2), (C(55), "whoosh", -3), (C(55) + 0.48, "thud", -4),
         (T(56, "pop"), "pop", 3), (T(58, "bid"), "pop", -3), (T("59b", "cheaply"), "pop", -3), (LS(60), "riser", -4),
         (T(63, "felt"), "sparkle", -3), (T(64, "gravity"), "boing", -2),
         (LS("card_ch04") + 0.15, "tick", 0), (LS("card_ch04") + 0.6, "tick", -2)]
    c += [(T(65, "four") + i * 0.22, "thud", -6) for i in range(4)]
    c += [(C(66) + 0.05, "thud", -2), (T(67, "sixty"), "pop", -3), (T(68, "cutting"), "whoosh", -4),
          (T(69, "dilution"), "pop", -2), (T(70, "lost") + 0.5, "thud", 0), (C(71) + 0.05, "thud", -2),
          (T(73, "nine"), "pop", -3), (T("73b", "seven"), "pop", -3), (C(74), "whoosh", -4), (LS(75), "whoosh_down", -4),
          (T(76, "six"), "pop", -1), (LS("76b"), "riser", -5), (C(78) + 0.05, "thud", -2),
          (T(80, "Great"), "thud", -2), (LS(81), "whoosh", -6), (T(82, "fell"), "thud", -1), (LS(83), "whoosh_down", -5),
          (C(85) + 0.05, "thud", -2), (T("87b", "pebble") + 0.5, "thud", 0), (C(90), "riser", -5), (T(91, "profit"), "thud", -2)]
    return c
