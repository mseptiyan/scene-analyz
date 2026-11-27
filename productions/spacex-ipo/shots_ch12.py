"""Chapter 1 (after the pilot section, lines 18-24) and Chapter 2 (lines 25-50)."""
from __future__ import annotations

import math

from common import (C, LE, LS, PAL, S, T, W, H, bg, cal, cam, ch, chapter_card, clamp, ease_in_out, ease_out, fx,
                    label, lerp, p2, pop, pop_label, popped, pr, scaled, text, wlabel, write_on_chars)
from crayon_engine.character import Look
from crayon_engine.draw import contact_shadow
from looks import BIG_FUND, ELON, EMPLOYEE, FOUNDER_FRIEND, RETAIL

BANKER_A = Look("Banker A", body="#22324A", inner="#F3F3F3", tie="#4FAE5A", hat="tophat")
BANKER_B = Look("Banker B", body="#3B2E4A", inner="#F3F3F3", tie="#D9363E", glasses="round")


def sh180(f):  # So why would a company open its doors at all?
    bg.blue_wall(f)
    pr.doors(f, 960, 930, 560, 600, open_p=1.0)
    ch.draw(f, ELON, 960, 930, 430, expr="thinking", pose="hips", seed=101)


def sh190(f):  # Reason one: money. Selling new slices -> cash -> build things.
    bg.gold_radial(f)
    wlabel(f, "REASON 1: MONEY", 960, 190, T(19, "Reason"), 84, color=PAL["gold"])
    popped(f, f.T - f.t, 420, 560, lambda: pr.pizza_slice(f, (330, 640), 200, 1), pre=True)
    popped(f, T(19, "cash"), 960, 640, lambda: pr.sack(f, 960, 760, 260))
    if f.T >= T(19, "build"):
        popped(f, T(19, "build"), 1500, 560, lambda: (pr.rocket(f, 1500, 540, 380, angle=0.25),))
    for x0, t0 in ((620, T(19, "cash")), (1180, T(19, "build"))):
        if f.T >= t0:
            p2.big_arrow(f, x0, 600, 140 * min(1, (f.T - t0) / 0.2) + 1, 0, color=PAL["paper"], width=50)


def sh200(f):  # Reason two: the club gets a way to sell. + That's called cashing out.
    bg.club_red(f)
    wlabel(f, "REASON 2", 960, 170, T(20, "Reason"), 80, color=PAL["gold"])
    sold = f.T >= T(20, "sell")
    for i, (lk, x) in enumerate(((EMPLOYEE, 560), (BIG_FUND, 960), (FOUNDER_FRIEND, 1360))):
        a = ch.draw(f, lk, x, 900, 440, expr="grin" if sold else "smug", pose="hold_r", seed=110 + i)
        hx_, hy_ = a["hand_r"]
        if sold:
            k = pop(f.T, T(20, "sell") + i * 0.12)
            if k > 0:
                scaled(f.ctx, hx_, hy_ - 30, k)
                pr.bill(f, hx_ + 10, hy_ - 30, 110, angle=-0.2)
                f.ctx.restore()
        else:
            pr.pizza_slice(f, (hx_ - 8, hy_ - 8), 64, 1)
    pop_label(f, "CASHING OUT", 960, 330, T("20b", "cashing"), 96, color=PAL["money_lt"])


def sh210(f):  # And SpaceX needed a lot of cash.
    bg.white_void(f, disc_y=900)
    popped(f, LS(21), 820, 520, lambda: p2.cheque(f, 820, 520, 900, "$???"), pre=True)
    ch.draw(f, ELON, 1480, 900, 460, expr="worried", pose="shrug", seed=120)


def _panel(f, x, w, fill, draw):
    ctx = f.ctx
    ctx.save()
    ctx.rectangle(x, 0, w, H)
    ctx.clip()
    ctx.rectangle(x, 0, w, H)
    from crayon_engine.draw import set_color
    set_color(ctx, fill)
    ctx.fill()
    draw()
    ctx.restore()
    from crayon_engine.draw import line, INK
    line(ctx, [(x, -10), (x, H + 10)], f.lw(10))


def sh220(f):  # rockets, Starlink satellites, xAI, giant AI computers
    ctx = f.ctx
    bg.card(f)
    w = W / 3
    t1, t2, t3 = T(22, "rockets"), T(22, "Starlink"), T(22, "giant")
    # the three panels are in frame from the cut; their objects pop on the words
    _panel(f, 0, w, "#3A4278", lambda: (popped(f, t1, w / 2, 540, lambda: pr.rocket(f, w / 2, 540, 460, flame=0.7))))
    _panel(f, w, w, "#2E3570", lambda: (fx.sparkle(f, w + 120, 220, 16, f.T), fx.sparkle(f, w + 520, 760, 12, f.T, 1),
                                       popped(f, t2, w * 1.5, 540, lambda: p2.satellite(f, w * 1.5, 540, 1.6, 0.3 + 0.05 * f.t))))
    _panel(f, 2 * w, w, "#2B5373", lambda: [popped(f, t3, 2 * w + 120 + i * 180, 600, (lambda i=i: p2.server_rack(
        f, 2 * w + 140 + i * 170, 860, 140, 560, f.T, i))) for i in range(3)])
    for i, (s, t0) in enumerate((("rockets", t1), ("satellites", t2), ("AI computers", t3))):
        wlabel(f, s, w * i + w / 2, 980, t0 + 0.1, 64)
    wlabel(f, "+ xAI (merged Feb 2026)", W - 330, 110, T(22, "ex"), 46, color=PAL["gold"])


def sh230(f):  # In 2025 brought in ~$18.7B but lost nearly $5B
    bg.white_void(f, disc_y=930, disc_rx=760)
    cal(f, 300, 330, 260, "2025", "YEAR")
    t1 = T(23, "eighteen")
    t2 = T(23, "lost")
    if f.T >= t1:
        h = 560 * ease_out((f.T - t1) / 0.6)
        p2.money_tower(f, 860, 930, 230, h, top_label="$18.7B" if f.T > t1 + 0.6 else None, label="came in")
    if f.T >= t2:
        h = 160 * ease_out((f.T - t2) / 0.5)
        p2.money_tower(f, 1350, 930, 230, h, color="#E58A8A", top_label="-$4.9B" if f.T > t2 + 0.5 else None,
                       label="net loss", label_c="#FF9C9C")


def sh235(f):  # lemonade stand that spends more building a giant factory
    bg.day_pad(f)
    p2.lemonade_stand(f, 420, 840, 300)
    built = clamp((f.T - T("23b", "spends")) / 1.5)
    p2.factory(f, 1260, 840, 760, 420, built=0.35 + 0.4 * built, t=f.T)
    wlabel(f, "sells a lot", 420, 360, T("23b", "sells"), 56)
    wlabel(f, "spends even more", 1260, 260, T("23b", "spends"), 56, color="#FF9C9C")


def sh240(f):  # Building the future is expensive.
    bg.white_void(f, disc_y=930)
    p2.receipt(f, 1240, 120, 420, ease_out((f.t - 0.1) / 1.2),
               [("rockets", "$$$"), ("satellites", "$$$"), ("AI chips", "$$$$"), ("Mars", "$$$$$")], "TOTAL: A LOT", max_h=800)
    ch.draw(f, ELON, 640, 930, 470, expr="worried", pose="idle", seed=125)


# ------------------------------------------------------------------ CHAPTER 2
STEPS = ["PAPERWORK", "ROADSHOW", "ORDER BOOK", "PRICING"]


def sh250(f):  # Going public is like launching a rocket. There's a countdown.
    bg.day_pad(f)
    pr.rocket(f, 1500, 520, 520)
    lit = 1 if f.T >= T(25, "countdown") else 0
    p2.countdown_board(f, 700, 520, 760, STEPS, lit)


def sh260(f):  # Step one: the paperwork.
    bg.white_void(f, disc_y=900)
    n = int(4 + 10 * ease_out((f.t - 0.05) / 0.8))
    p2.doc_stack(f, 960, 900, 380, n=n, top_text="S-1")
    label(f.ctx, f, "STEP 1: PAPERWORK", 960, 170, 84, color=PAL["gold"], chars=write_on_chars(f.T, f.T - f.t + 0.05, 30))


def sh270(f):  # sent the SEC a secret draft on April first
    bg.office(f)
    slot = p2.mailbox(f, 1340, 900, 300, "SEC")
    cal(f, 360, 330, 250, "APR 1", "2026")
    t0 = T(27, "secret")
    p = ease_in_out((f.T - t0) / 1.0)
    if p < 1:
        x = lerp(560, slot[0], p)
        y = lerp(700, slot[1], p) - math.sin(math.pi * p) * 200
        p2.envelope(f, x, y, 300 * (1 - 0.45 * p), angle=-0.2 + 0.2 * p)
    wlabel(f, "secret draft", 760, 960, t0, 58)


def sh280(f):  # On May twentieth, it made that document public.
    bg.office(f, "#4F7A9C")
    cal(f, 300, 320, 240, "MAY 20", "2026")
    k = ease_out((f.T - T(28, "public")) / 0.5) if f.T >= T(28, "public") else 0.15
    ctx = f.ctx
    ctx.save()
    ctx.translate(1000, 430)
    ctx.scale(1, max(0.08, k))
    p2.contract(f, 0, 0, 420, title="S-1", sub="PUBLIC")
    ctx.restore()
    for i, (lk, x) in enumerate(((RETAIL[0], 640), (RETAIL[1], 1380), (RETAIL[3], 1560))):
        ch.draw(f, lk, x, 960, 340, expr="sparkle" if k > 0.9 else "neutral", facing=0.6 if x < 1000 else -0.6, seed=130 + i)


def sh290(f):  # S-1 = diary: earns / owes / could go wrong
    bg.gold_radial(f)
    tabs = [("EARNS", "#3F9E4D", pop(f.T, T(29, "earns"))), ("OWES", "#E0A020", pop(f.T, T(29, "owes"))),
            ("RISKS", PAL["loss"], pop(f.T, T(29, "wrong")))]
    p2.diary(f, 900, 600, 1000, tabs, cover="S-1")
    wlabel(f, "the company's diary", 900, 200, T(29, "diary"), 76, color=PAL["gold"])


def sh295(f):  # anyone can read it for free on the SEC's website
    bg.office(f, "#5B8CA8")
    sx, sy, sw, sh_ = p2.laptop(f, 1060, 860, 600)
    p2.diary(f, sx, sy, sw * 0.86, [("RISKS", PAL["loss"], 1.0)], cover="S-1")
    ch.draw(f, RETAIL[4], 520, 960, 420, expr="sparkle", facing=0.7, seed=140)
    wlabel(f, "free to read online", 1060, 240, T("29b", "free"), 64, color=PAL["gold"])


def sh300(f):  # Step two: the roadshow.
    bg.day_pad(f)
    p = ease_out((f.t - 0.0) / 0.9)
    x = lerp(-500, 900, p)
    wx, wy = p2.bus(f, x, 900, 820, t=f.T, moving=1 - p)
    if p < 0.95:
        fx.speed_lines(f, x - 430, 760, 0.0, n=5, length=160, spread=160, t=f.T, color=PAL["ink"])
    ch.draw(f, ELON, wx, wy + 60, 150, expr="grin", seed=150, shadow_floor=False, lw_px=5)
    label(f.ctx, f, "STEP 2: ROADSHOW", 960, 170, 84, color=PAL["gold"], chars=write_on_chars(f.T, f.T - f.t + 0.1, 30))


def sh310(f):  # Starting June fourth, SpaceX and its banks pitched the stock to huge investors.
    bg.office(f)
    cal(f, 220, 300, 220, "JUN 4", "2026")
    p2.easel_chart(f, 600, 900, 360)
    ch.draw(f, ELON, 860, 930, 420, expr="grin", pose="point", seed=160)
    for i, x in enumerate((1180, 1420, 1660)):
        ch.draw(f, BIG_FUND if i != 1 else FOUNDER_FRIEND, x, 900, 400, expr="thinking" if i == 1 else "smug", seed=161 + i,
                facing=-0.6)
    p2.table_front(f, 1420, 720, 720, 220)


def sh320(f):  # The lead banks were Goldman Sachs and Morgan Stanley.
    bg.office(f, "#4D6E8C")
    ch.draw(f, BANKER_A, 700, 930, 500, expr="smug", pose="hips", seed=170)
    ch.draw(f, BANKER_B, 1220, 930, 500, expr="happy", pose="hips", seed=171)
    pop_label(f, "Goldman Sachs", 700, 250, T(32, "Goldman"), 70)
    pop_label(f, "Morgan Stanley", 1220, 250, T(32, "Morgan"), 70)


def sh330(f):  # underwriters: organise the sale and find buyers
    bg.office(f, "#4D6E8C")
    a = ch.draw(f, BANKER_A, 760, 930, 500, expr="smug", pose="hold", seed=172)
    p2.ledger(f, 760, 800, 240, [], 0, title="BOOK")
    pop_label(f, "UNDERWRITERS", 1250, 300, T(33, "underwriters"), 80, color=PAL["gold"])
    tb = T(33, "buyers")
    for i, (lk, x) in enumerate(((RETAIL[0], 1240), (BIG_FUND, 1460), (RETAIL[2], 1680))):
        if f.T >= tb + i * 0.15:
            popped(f, tb + i * 0.15, x, 800, lambda lk=lk, x=x, i=i: ch.draw(f, lk, x, 930, 330, expr="happy", seed=173 + i,
                                                                               facing=-0.5))


def sh335(f):  # fee = a small slice of the money raised
    bg.white_void(f, disc_y=930, disc_rx=700)
    top = p2.money_tower(f, 760, 930, 260, 620, top_label="money raised")
    a = ch.draw(f, BANKER_A, 1350, 930, 460, expr="grin", pose="hold_r", seed=175)
    t0 = T("33b", "fee")
    p = ease_in_out((f.T - t0) / 0.7)
    if f.T >= t0:
        x = lerp(760, a["hand_r"][0], p)
        y = lerp(top + 40, a["hand_r"][1] - 20, p) - math.sin(math.pi * p) * 160
        p2.money_tower(f, x, y + 20, 120, 26, color="#9AD89A")
    wlabel(f, "fee", 1520, 330, t0 + 0.2, 80, color=PAL["gold"])


ORDERS = ["10,000 @ $135", "250,000 @ $135", "1,000,000 @ $135", "50,000 @ $135", "3,000,000 @ $135",
          "120,000 @ $135", "800,000 @ $135", "5,000,000 @ $135", "75,000 @ $135", "2,000,000 @ $135",
          "40,000 @ $135", "9,000,000 @ $135"]


def sh340(f):  # Step three: the order book. + Investors write how many slices, at what price.
    bg.gold_radial(f)
    label(f.ctx, f, "STEP 3: ORDER BOOK", 960, 150, 80, color=PAL["gold"], chars=write_on_chars(f.T, f.T - f.t + 0.05, 30))
    t0 = T(35, "write")
    n = 0 if f.T < t0 else int((f.T - t0) / 0.28) + 1
    p2.ledger(f, 960, 600, 1200, ORDERS, min(n, len(ORDERS)))
    for i in range(3):
        ts = t0 + i * 0.6
        if ts <= f.T < ts + 0.6:
            p = (f.T - ts) / 0.6
            p2.slip(f, lerp(200 + i * 600, 900, p), lerp(1000, 600, p) - math.sin(math.pi * p) * 200, 200, ORDERS[i], angle=0.3 - p * 0.3)


def sh360(f):  # Normally a price range. If the book overflows, the price can rise.
    bg.gold_radial(f)
    to = T(36, "overflows")
    pos = 0.3 + 0.55 * ease_in_out((f.T - to) / 1.0) if f.T >= to else 0.3
    p2.price_slider(f, 960, 760, 1100, pos)
    wlabel(f, "price range", 960, 620, T(36, "range"), 64)
    n = 6 + (int((f.T - to) / 0.12) if f.T >= to else 0)
    for i in range(min(n, 22)):
        p2.slip(f, 960 + math.sin(i * 2.1) * 360, 420 - i * 12, 190, ORDERS[i % len(ORDERS)], angle=math.sin(i) * 0.4)


def sh370(f):  # skipped the range: one fixed price $135
    bg.gold_radial(f)
    p2.price_tag(f, 960, 520, 800, "$135", angle=-0.1)
    tf = T(37, "fixed")
    p2.stamp(f, 1180, 760, 460, "FIXED", pop(f.T, tf, dur=4 / 30, peak=1.15), angle=-0.15)
    wlabel(f, "no price range", 960, 960, T(37, "skipped"), 58)


def sh375(f):  # buyers asked for about four times more shares than there were
    bg.white_void(f, disc_y=930, disc_rx=800)
    p2.money_tower(f, 380, 900, 240, 360, color="#F7D56A", label="shares for sale")
    t0 = T("37b", "four")
    for i in range(4):
        h = 360 * ease_out((f.T - (T("37b", "asked") + i * 0.18)) / 0.4)
        if h > 1:
            p2.money_tower(f, 800 + i * 290, 900, 240, h, color="#FFFBEA", label="orders" if i == 0 else None)
    pop_label(f, "4x the orders", 1240, 330, t0, 100, color=PAL["gold"])


def sh380(f):  # Step four: pricing night. June eleventh, locked in.
    bg.night_window(f)
    cal(f, 360, 330, 240, "JUN 11", "2026")
    p2.contract(f, 900, 560, 380, title="FINAL PRICE", sub="$135")
    tl = T(38, "locked")
    closed = ease_out((f.T - tl) / 0.25) if f.T >= tl else 0.0
    p2.padlock(f, 1100, 760, 1.2, closed)
    label(f.ctx, f, "STEP 4: PRICING", 960, 140, 78, color=PAL["gold"], chars=write_on_chars(f.T, f.T - f.t + 0.05, 30))


def sh390(f):  # sold about 556 million new shares
    bg.gold_radial(f)
    t0 = f.T - f.t
    n = 12 + int(clamp((f.T - t0) / 2.6) * 48)
    for i in range(n):
        r, c = divmod(i, 12)
        pr.pizza(f, 190 + c * 140, 250 + r * 125, 58, slices=6)
    if f.T >= T(39, "five"):
        p2.counter_number(f, 960, 980, 110, "556,000,000 shares")


def sh400(f):  # $135 x 556 million = about $75 billion
    bg.white_void(f, floor=False)
    t0, t1 = T(40), LE(40)
    total = len("$135") + len("x 556,000,000") + len("about $75 billion")
    c = write_on_chars(f.T, t0, total / max(0.5, (t1 - t0) * 0.8))
    p2.chalkboard(f, 960, 540, 1300, 700, ["$135", "x 556,000,000", "=about $75 billion"], chars=c, size=96)


def sh410(f):  # The old record: Saudi Aramco, about $29 billion, 2019.
    bg.white_void(f, disc_y=950, disc_rx=820)
    ts = T(41, "Saudi")
    h = 300 * ease_out((f.T - ts) / 0.6) if f.T >= ts else 0
    if h > 1:
        p2.money_tower(f, 620, 900, 260, h, color="#B9C7A8", top_label="$29.4B" if f.T > ts + 0.6 else None,
                       label="old record (2019)")
    from crayon_engine.draw import rrect, set_color
    f.ctx.save()
    f.ctx.set_dash([20, 16])
    rrect(f.ctx, 1180, 180, 260, 720, 10)
    set_color(f.ctx, "#9A9AA0")
    f.ctx.set_line_width(f.lw(6))
    f.ctx.stroke()
    f.ctx.restore()
    text(f.ctx, "?", 1310, 600, 220, color="#C9CAD0", kind="marker")
    wlabel(f, "Saudi Aramco", 620, 500, ts + 0.1, 56, color=PAL["gold"])


def sh420(f):  # SpaceX's deal was more than 2.5x bigger
    bg.white_void(f, disc_y=950, disc_rx=820)
    p2.money_tower(f, 620, 900, 260, 300, color="#B9C7A8", top_label="$29.4B", label="Saudi Aramco 2019")
    t0 = LS(42)
    h = 700 * ease_out((f.T - t0) / 1.2)
    top = p2.money_tower(f, 1310, 900, 260, h, top_label="$75B" if h > 680 else None, label="SpaceX 2026")
    pop_label(f, "2.5x+", 960, 420, T(42, "half"), 110, color=PAL["gold"])


def sh430(f):  # regular people got a real seat at the table
    bg.office(f, "#6A5B8C")
    sp = f.T >= T(43, "seat")
    seats = [(BIG_FUND, "smug"), (RETAIL[0], "sparkle" if sp else "happy"), (BANKER_B, "smug"),
             (RETAIL[1], "sparkle" if sp else "happy"), (RETAIL[2], "sparkle" if sp else "happy")]
    for i, (lk, ex) in enumerate(seats):
        a = ch.draw(f, lk, 400 + i * 280, 880, 400, expr=ex, seed=180 + i, pose="hold_r" if lk in RETAIL else "idle")
        if lk in RETAIL:
            pr.phone(f, a["hand_r"][0] + 6, a["hand_r"][1] - 6, 60, 0.15)
    p2.table_front(f, 960, 700, 1600, 240)


def sh440(f):  # usually 5-10% to everyday investors
    bg.gold_radial(f)
    p2.pie(f, 820, 540, 330, 0.075, label="5-10%")
    wlabel(f, "everyday investors", 1460, 380, T(44, "everyday"), 60, arrow_to=(1080, 440))
    ch.draw(f, RETAIL[3], 1460, 960, 380, expr="sad", seed=190, facing=-0.6)


def sh450(f):  # planned 30%, final ~ a fifth; apps
    bg.gold_radial(f)
    tp, tf = T(45, "thirty"), T(45, "fifth")
    frac = 0.075
    if f.T >= tf:
        frac = lerp(0.075, 0.20, ease_out((f.T - tf) / 0.5))
    p2.pie(f, 640, 520, 320, frac, label="~20%" if f.T >= tf + 0.4 else None, ghost=0.30 if f.T >= tp else None)
    wlabel(f, "planned: up to 30%", 640, 960, tp, 54)
    for i, name in enumerate(("Robinhood", "Fidelity", "Schwab")):
        t0 = T(45, name)
        if f.T >= t0:
            popped(f, t0, 1320 + i * 0.0, 300 + i * 220, lambda name=name, i=i: (
                pr.phone(f, 1220, 300 + i * 220, 150, 0.0),
                label(f.ctx, f, name, 1500, 320 + i * 220, 58)))


def sh460(f):  # one more trick: the greenshoe
    bg.white_void(f, disc_y=860)
    popped(f, T(46, "greenshoe"), 960, 600, lambda: p2.green_shoe(f, 960, 600, 560))
    ch.draw(f, RETAIL[2], 1520, 900, 400, expr="thinking", seed=200, facing=-0.5)
    if f.T >= T(46, "greenshoe") + 0.3:
        fx.exclaim(f, 1600, 380, 100, "??", color=PAL["gold"])


def sh470(f):  # lets the banks sell 15% extra shares if demand is hot
    bg.white_void(f, disc_y=860)
    p2.green_shoe(f, 620, 640, 460)
    t0 = T(47, "extra")
    for i in range(3):
        p = ease_out((f.T - (t0 + i * 0.2)) / 0.5)
        if p > 0:
            pr.pizza_slice(f, (lerp(700, 1120 + i * 200, p), lerp(560, 480 - i * 30, p)), 90, 1)
    wlabel(f, "+15% extra shares", 1300, 820, t0, 70, color=PAL["money_lt"])


def sh480(f):  # total grew to about $85.7 billion
    bg.white_void(f, disc_y=950, disc_rx=700)
    t0 = T(48, "grew")
    h = 600 + (85 * ease_out((f.T - t0) / 0.8) if f.T >= t0 else 0)
    p2.money_tower(f, 960, 950, 300, h, top_label="$85.7B" if f.T >= t0 + 0.8 else "$75B")
    if f.T >= T(48, "hot"):
        for i in range(5):
            fx.sparkle(f, 760 + i * 100, 300 + (i % 2) * 120, 26, f.T, i)
    wlabel(f, "greenshoe used", 1500, 520, T(48, "used"), 56, color=PAL["money_lt"])


def sh490(f):  # Elon kept about four-fifths of the votes
    bg.office(f, "#6B5B7A")
    slot = p2.ballot_box(f, 960, 900, 360)
    a = ch.draw(f, ELON, 1420, 930, 460, expr="smug", pose="hold_r", seed=210)
    for i in range(4):
        p2.ballot(f, a["hand_r"][0] + 10, a["hand_r"][1] - 20 - i * 26, 120, angle=-0.2 + i * 0.05)
    b = ch.draw(f, RETAIL[0], 480, 930, 400, expr="neutral", pose="hold_r", seed=211, facing=0.5)
    p2.ballot(f, b["hand_r"][0] + 10, b["hand_r"][1] - 20, 120)
    pop_label(f, "~80% of the votes", 1420, 280, T(49, "four"), 70, color=PAL["gold"])


def sh500(f):  # The public could own slices, but Elon still picks the toppings.
    bg.gold_radial(f)
    pr.pizza(f, 1080, 620, 260)
    tt = T(50, "toppings")
    for i in range(5):
        if f.T >= tt + i * 0.15:
            k = pop(f.T, tt + i * 0.15)
            a = i * 1.3
            ctx = f.ctx
            from crayon_engine.draw import circle, fill_stroke
            circle(ctx, 1080 + math.cos(a) * 140, 620 + math.sin(a) * 140, 26 * k)
            fill_stroke(ctx, "#4FAE5A", f.lw(4))
    ch.draw(f, ELON, 640, 960, 440, expr="grin", pose="point", seed=220)
    for i, (lk, x) in enumerate(((RETAIL[1], 240), (RETAIL[3], 1640))):
        a = ch.draw(f, lk, x, 960, 360, expr="neutral", pose="hold_r", seed=221 + i, facing=0.6 if x < 960 else -0.6)
        pr.pizza_slice(f, (a["hand_r"][0], a["hand_r"][1] - 10), 54, 1)


def shots():
    m = dict
    return [
        S("SH180", sh180, C(18), cam(0.03, (960, 560)), "MS", camtxt="push-in 3%/s", action="Elon in the open IPO doors", expr="thinking"),
        S("SH190", sh190, C(19), cam(0.02), "Infographic", camtxt="push-in 2%/s", action="slice -> sack -> rocket pop on words", txt="REASON 1: MONEY", sfx="pop x3"),
        S("SH200", sh200, C(20), cam(-0.03), "MS lineup", camtxt="pull-out 3%/s", action="Club members sell slices, bills pop", expr="smug -> grin", txt="REASON 2, CASHING OUT", sfx="cash"),
        S("SH210", sh210, C(21), cam(0.03, (1000, 560)), "MS", camtxt="push-in 3%/s", action="Giant blank cheque, Elon worried", expr="worried", txt="$???", sfx="pop"),
        S("SH220", sh220, C(22), cam(0.02), "Split x3", camtxt="push-in 2%/s", action="Triptych: rocket / satellite / servers pop on words", txt="rockets, satellites, AI computers, xAI", sfx="pop x3"),
        S("SH230", sh230, C(23), cam(-0.025), "Infographic", camtxt="pull-out 2.5%/s", action="Calendar 2025; green tower $18.7B vs red $4.9B loss", txt="$18.7B, -$4.9B", sfx="cash, thud"),
        S("SH235", sh235, C("23b"), cam(0.025), "WS", camtxt="push-in 2.5%/s", action="Lemonade stand vs giant factory under construction", txt="sells a lot / spends even more"),
        S("SH240", sh240, C(24), cam(0.03, (900, 560)), "MS", camtxt="push-in 3%/s", action="Receipt unrolls to the floor beside Elon", expr="worried (+sweat)", txt="TOTAL: A LOT", sfx="whoosh", trans="hard cut to card"),
        S("SH245", chapter_card(2, "Building the Biggest Launch"), LS("card_ch02"), None, "Card", camtxt="locked-off", action="Chapter card write-on", txt="Chapter 2", sfx="ticks"),
        S("SH250", sh250, C(25), cam(0.025), "WS", camtxt="push-in 2.5%/s", action="Countdown board with the 4 steps, rocket on the pad", txt="COUNTDOWN"),
        S("SH260", sh260, C(26), cam(0.04), "MS", camtxt="push-in 4%/s", action="Document stack grows", txt="STEP 1: PAPERWORK, S-1", sfx="flips"),
        S("SH270", sh270, C(27), cam(-0.03), "WS", camtxt="pull-out 3%/s", action="Confidential envelope arcs into the SEC mailbox", txt="APR 1, secret draft", sfx="whoosh"),
        S("SH280", sh280, C(28), cam(0.025), "MS", camtxt="push-in 2.5%/s", action="S-1 unfolds public; onlookers sparkle", expr="neutral -> sparkle", txt="MAY 20, S-1 PUBLIC", sfx="pop"),
        S("SH290", sh290, C(29), cam(0.02), "Insert", camtxt="push-in 2%/s", action="Diary tabs pop on 'earns', 'owes', 'wrong'", txt="EARNS / OWES / RISKS", sfx="pop x3"),
        S("SH295", sh295, C("29b"), cam(-0.025), "MS", camtxt="pull-out 2.5%/s", action="Retail investor reads the S-1 on a laptop", expr="sparkle", txt="free to read online"),
        S("SH300", sh300, C(30), cam(0.03), "WS", camtxt="push-in 3%/s", action="Roadshow bus drives in and stops (ease-out)", expr="grin", txt="STEP 2: ROADSHOW", sfx="whoosh"),
        S("SH310", sh310, C(31), cam(0.02), "WS", camtxt="push-in 2%/s", action="Elon pitches at an easel to big funds behind a table", expr="grin / smug", txt="JUN 4"),
        S("SH320", sh320, C(32), cam(0.03), "MS two-shot", camtxt="push-in 3%/s", action="Two generic bankers, name labels pop", txt="Goldman Sachs, Morgan Stanley", sfx="pop x2"),
        S("SH330", sh330, C(33), cam(-0.025), "MS", camtxt="pull-out 2.5%/s", action="Banker with the book; buyers pop in", txt="UNDERWRITERS", sfx="pop"),
        S("SH335", sh335, C("33b"), cam(0.025), "MS", camtxt="push-in 2.5%/s", action="A thin slice of the money tower flies to the banker", expr="grin", txt="fee", sfx="cash"),
        S("SH340", sh340, C(34), cam(0.02, (960, 560)), "Insert", camtxt="push-in 2%/s", action="Order book fills with handwritten orders; slips fly in", txt="STEP 3: ORDER BOOK, orders", sfx="ticks"),
        S("SH360", sh360, C(36), cam(-0.02), "Infographic", camtxt="pull-out 2%/s", action="Price-range slider rises as slips overflow", txt="price range, $?? - $??"),
        S("SH370", sh370, C(37), cam(0.03), "Insert", camtxt="push-in 3%/s", action="Price tag $135; FIXED stamp slams", txt="$135, FIXED, no price range", sfx="thud"),
        S("SH375", sh375, C("37b"), cam(-0.025), "Infographic", camtxt="pull-out 2.5%/s", action="1 stack of shares vs 4 stacks of orders", txt="4x the orders", sfx="pop"),
        S("SH380", sh380, C(38), cam(0.025), "MS", camtxt="push-in 2.5%/s", action="Night window; padlock snaps on the final price", txt="JUN 11, STEP 4: PRICING", sfx="thud"),
        S("SH390", sh390, C(39), cam(-0.03), "Infographic", camtxt="pull-out 3%/s", action="Grid of slices fills the frame", txt="556,000,000 shares", sfx="ticks"),
        S("SH400", sh400, C(40), cam(0.02), "Insert", camtxt="push-in 2%/s", action="Chalkboard maths write-on", txt="$135 x 556,000,000 = about $75 billion", sfx="ticks"),
        S("SH410", sh410, C(41), cam(0.02), "Infographic", camtxt="push-in 2%/s", action="Aramco tower grows; empty dashed slot", txt="$29.4B, Saudi Aramco"),
        S("SH420", sh420, C(42), cam(-0.03), "Infographic", camtxt="pull-out 3%/s", action="SpaceX tower grows past it", txt="$75B, 2.5x+", sfx="riser"),
        S("SH430", sh430, C(43), cam(0.02), "WS", camtxt="push-in 2%/s", action="Retail investors seated with funds at the big table", expr="happy -> sparkle"),
        S("SH440", sh440, C(44), cam(0.025), "Infographic", camtxt="push-in 2.5%/s", action="Pie: 5-10% retail slice", expr="sad", txt="5-10%"),
        S("SH450", sh450, C(45), cam(-0.02), "Infographic", camtxt="pull-out 2%/s", action="Ghost 30%, slice grows to ~20%; app phones pop", txt="planned up to 30%, ~20%, Robinhood/Fidelity/Schwab", sfx="pop x3"),
        S("SH460", sh460, C(46), cam(0.03), "MS", camtxt="push-in 3%/s", action="A literal green shoe pops (gag)", expr="thinking", txt="??", sfx="boing"),
        S("SH470", sh470, C(47), cam(-0.025), "MS", camtxt="pull-out 2.5%/s", action="Extra slices slide out of the shoe", txt="+15% extra shares", sfx="whoosh"),
        S("SH480", sh480, C(48), cam(0.03), "Infographic", camtxt="push-in 3%/s", action="Tower grows $75B -> $85.7B, sparkles", txt="$85.7B, greenshoe used", sfx="cash"),
        S("SH490", sh490, C(49), cam(0.02), "WS", camtxt="push-in 2%/s", action="Elon holds 4 ballots, retail holds 1", expr="smug", txt="~80% of the votes", sfx="pop"),
        S("SH500", sh500, C(50), cam(-0.025), "MS", camtxt="pull-out 2.5%/s", action="Pizza callback: Elon adds toppings, crowd holds slices", expr="grin", trans="hard cut to card", sfx="pop x5"),
    ]


def cues():
    return [
        (T(19, "slices"), "pop", -2), (T(19, "cash"), "pop", -2), (T(19, "build"), "pop", -2),
        (T(20, "sell"), "cash", -3), (T("20b", "cashing"), "pop", -2), (LS(21), "pop", -2),
        (T(22, "rockets"), "pop", -3), (T(22, "Starlink"), "pop", -3), (T(22, "giant"), "pop", -3),
        (T(23, "eighteen"), "cash", -4), (T(23, "lost"), "thud", -4), (LS(24), "whoosh", -6),
        (LS("card_ch02") + 0.15, "tick", 0), (LS("card_ch02") + 0.6, "tick", -2), (LS("card_ch02") + 1.0, "tick", -1),
        (T(25, "countdown"), "tick", 0), (LS(26), "flip", -2), (LS(26) + 0.2, "flip", -3),
        (T(27, "secret"), "whoosh", -4), (T(28, "public"), "pop", -3),
        (T(29, "earns"), "pop", -3), (T(29, "owes"), "pop", -3), (T(29, "wrong"), "pop", -1),
        (C(30), "whoosh", 0), (T(32, "Goldman"), "pop", -3), (T(32, "Morgan"), "pop", -3), (T(33, "underwriters"), "pop", -3),
        (T("33b", "fee"), "cash", -5), (T(37, "fixed"), "thud", 0), (T("37b", "four"), "pop", -2),
        (T(38, "locked"), "thud", -2), (T(39, "five"), "tick", 0), (LS(42), "riser", -4), (T(42, "half"), "pop", -2),
        (T(45, "Robinhood"), "pop", -4), (T(45, "Fidelity"), "pop", -4), (T(45, "Schwab"), "pop", -4),
        (T(46, "greenshoe"), "boing", -2), (T(47, "extra"), "whoosh", -6), (T(48, "grew"), "cash", -3),
        (T(49, "four"), "pop", -2), (T(50, "toppings"), "pop", -4),
    ]
