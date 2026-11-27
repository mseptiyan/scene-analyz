# Characters: The SpaceX IPO

Format: `references/character_design_standards.md` §9. All designs are **original**. No Crayon Capital character or mascot is reused (in particular, there is no mascot with round glasses and a red bow tie). Real people are shown as **light caricatures only**: one hair silhouette plus an outfit colour, with no physical mockery.

Code source of truth: `looks.py` (palettes) + `tools/crayon_engine/character.py` (shape system).
Model sheets: `assets/modelsheet_pilot.png` (hero anon → revealed, extras, crowd, 12-expression bank) and `assets/modelsheet_silhouettes.png`.

**Shape system (all characters):** total height = 3.2 × head diameter D · round head (31%) · bean body 1.25 D tall, 1.0 D wide (≈39%) · legs 1.05 D (≈33%) · no neck (head overlaps the body by 0.1 D) · rubber-hose single-line limbs at 1.15 × outline · outline `#1A1617`, **8 px at 1080p, constant under camera zoom** (measured 7–8 px at zoom 1.00 and 1.07) · one hard crescent shadow on head, hair and body, away from the key light (upper-left) · no nose, no ears · eyes are vertical black ovals with a highlight · floating brows lead every expression.

---

## Character Brief: ELON (caricature of Elon Musk)
- **Narrative role:** protagonist / face of SpaceX. In the hook he is **anonymous (grey face + grey hair)** until the word "SpaceX". Then the colour is revealed (`anon=True → False`, swapped on the exact frame of the word).
- **Colour class:** hero (the only skin-coloured character in the pilot).
- **Head silhouette:** short dark-brown hair, swept back, with volume and a quiff to screen-right.
- **Identity props:** all-black outfit (black jacket-bean with a dark-grey T-shirt "V").
- **Palette:** skin `#F2D3B0` (shadow `#D9AE8A`) · hair `#3A2B24` (shadow ×0.7, one highlight band ×1.45) · jacket `#24262C` (shadow ×0.78, blue-shifted) · T-shirt `#3C4250`
  · **anon variant:** face `#A6A6AB` / shadow `#8A8A90`, hair `#6E6E74`
- **Proportions:** 3.2 D tall · body 1.0 D wide
- **Visual personality:** confident, showman, restless → poses: hands on hips (`hips`), wave (`wave`), arms up (`arms_up`).
- **Signature expressions:** `proud` (eyes closed, smile: "I did it"), `grin` (showman), `smug` (hook, grey face). Later chapters: `worried` (+sweat) for Ch 4, `shock` for the −53% drop.
- **Motion style:** limited animation. The proud ↔ grin/wave pose is swapped **instantly every 21 frames** (reference S5). Breathing 1.2% / 2.6 s, blink every 2–5 s (4 frames).
- **Do:** keep the quiff on screen-right in every shot, and keep the outfit black.
- **Don't:** no logos on clothing, no exaggerated jaw or nose, no mocking features, no real company logos nearby.
- **Model sheet:** turnaround → front only in the pilot (¾ via `facing`) · expressions ✓ 12 · mouth shapes ✓ 7 (line, smile, frown, smirk, wave, grin, O/shout) · poses ✓ idle/hips/wave/arms_up/hold/hold_r/point/phone/shrug/sad.

## Character Brief: RETAIL INVESTORS ×5 (extras)
- **Role:** everyday buyers who were "stuck behind the rope" and then get slices through apps.
- **Colour class:** active extras, **plain white heads** `#FDFDFB` (shadow `#C9CAD0`) with coloured clothes.
- **Identity per extra (silhouette + 1 prop):**

| ID | Head | Clothes | Prop |
|---|---|---|---|
| Retail A | bald | teal hoodie `#2E9C9A` | phone |
| Retail B | light-grey bob `#E9E9EC` | orange `#E8833A` | phone |
| Retail C | yellow cap `#F2B630` | purple `#7A5CC2` | phone |
| Retail D | bald | yellow hoodie `#F2C14E` | phone |
| Retail E | light-grey bun `#E9E9EC` | blue `#3FA9E0` | phone |

- **Signature expressions:** `worried` (behind the rope), `sparkle` (doors open), `grin` (slice received).
- **Don't:** no skin colour (that would break the colour hierarchy), no more than 2–3 coloured characters dominating a frame.

## Character Brief: PRIVATE CLUB (extras)
| ID | Role | Head | Body | Prop |
|---|---|---|---|---|
| Employee | early employee | white + white hard hat | slate `#5B6B7D` | slice |
| Big fund | big investor | white + black top hat (red band) | burgundy `#6B2234` + white shirt, gold tie `#F2B630` | slice |
| Early investor | private investor | white | navy `#2A3556` + white shirt, red tie `#D9363E` | gold monocle `#C98A12` |
| Bouncer | gatekeeper | white | black suit `#1E1C1F` (width 1.18) | sunglasses + earpiece |

## CROWD (background)
- Grey heads `#8C8C90–#C2C2C4`, grey bodies `#7E7E83–#B3B3B6`, **no faces**, outline 4.5–5 px.
- Cheering = instant up/down bob swap every 9 frames, de-synced per member. Foreground crowds have no arms (QC fix: arms crossed the neighbours' heads).

## MYSTERY: "The next giants" (silhouettes)
- Ink silhouettes `#2A2526` with outline `#0E0C0D`, a violet rim `#6B6280` on the head, and a white ticket marked "IPO".
- Variants: antenna (future: AI company A), round (B), wide (C). Generic shapes, revealed one by one in Ch 5 **without real logos**.

## Colour hierarchy per shot (pilot)
At most 1 skin-coloured hero + white-headed extras + grey crowd. Checked on every A/M/Z frame (`qc_report.md`).
