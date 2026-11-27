# crayon_engine

A code-based renderer for **Crayon Verse** explainers (skill `.claude/skills/animate-crayon-verse`).
Everything is vector, drawn with cairo: characters, backgrounds, props and text. Output is 1920×1080, 30 fps, H.264 High + AAC.

## Setup (cloud session, already tested)
```bash
apt-get install -y espeak-ng libcairo2-dev pkg-config
uv venv -p 3.12 /home/user/cvenv
VIRTUAL_ENV=/home/user/cvenv uv pip install -r tools/crayon_engine/requirements.txt
VIRTUAL_ENV=/home/user/cvenv uv pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
```
Environment variables: `HF_HUB_DISABLE_XET=1` (the Xet CDN is blocked by the network policy, so HTTP download is used) and `VIRTUAL_ENV=/home/user/cvenv` (misaki/spacy call uv).

## Pipeline
```bash
# 1) VO: Kokoro -> per-chapter WAV (-14 LUFS, TP <= -1 dBTP) -> faster-whisper word timestamps
python -m crayon_engine.vo productions/spacex-ipo/pilot_vo.json /home/user/work/spacex-ipo/audio
# 2) render (cuts are derived from words.json) + SFX/bed mix + mux
python productions/spacex-ipo/pilot.py render   /home/user/work/spacex-ipo/audio out.mp4
# 3) QC stills / shot list generated from the locked timeline
python productions/spacex-ipo/pilot.py stills   /home/user/work/spacex-ipo/audio qc_dir
python productions/spacex-ipo/pilot.py shotlist /home/user/work/spacex-ipo/audio productions/spacex-ipo/shotlist.md
```

## Modules
| File | Contents |
|---|---|
| `core.py` | colour tokens, `shade()` (cel shadow ×0.8 + hue shift toward blue), easing, `pop()` (overshoot 108%, 7 f), `shake()`, `Camera`/`drift()` (constant-speed zoom 2–8%/s), `Frame.lw()` (outline compensated for zoom) |
| `draw.py` | primitives: circle/ellipse/bean/rrect, `crescent()` (one hard crescent shadow away from the key light), contact shadow |
| `character.py` | `Look` + `draw()`: round head, bean body, rubber-hose limbs, hair, hats, glasses, 12 expressions (eye+brow+mouth swap), blink 2–5 s/4 f, breathing 1.2%/2.6 s, 10 poses, anon (grey face) for reveals; `crowd()` (grey, faceless); `silhouette()` |
| `props.py` | certificate, bill, money sack, money mountain, generic rocket, newspaper, pizza/slice, velvet rope, plaque, doors, phone, ticket, **desk calendar (flip)**, **stock chart draw-on** (with rocket tip), word card, office building, ticker tape |
| `props2.py` | finance/process props: countdown board, document stack, envelope, SEC mailbox, S-1 diary with tabs, laptop, roadshow bus, order book, slips, price slider, price tag, stamp, padlock, chalkboard, money tower, pie with ghost slice, green shoe, ballot box, bell, popcorn, auction paddle, weight + chain, contract + pen, knife, suitcase, dam, report card, receipt (unroll), fuel tank, planet, satellite, server rack, cheque, big arrow, balance scale, factory, lemonade stand, chained EXIT door, glass rocket (crack), whiteboard |
| `backgrounds.py` | white void + floor disc, **elliptical radial spotlight**, gold radial, night grid, crisis desk, red club, market hall, blue wall, night launch pad (2 searchlights in a "V"), black card, vignette, light shafts |
| `text.py` | handwritten text from TTF outlines (fontTools → cairo), outer ink stroke, **letter-by-letter write-on**, dialogue balloon with a tail tick, label + hand-drawn arrow |
| `fx.py` | **confetti** & **money rain** (closed-form physics on ones, deterministic), sparkle, speed lines, "!!", smoke |
| `timeline.py` | `Words` (word timestamps → `cut(line, token, lead=0.2)`), `Shot`, `Timeline` |
| `render.py` | parallel render (fork) → raw BGRA → x264, concat, mux AAC 320k stereo |
| `vo.py` | Kokoro TTS, assembly with controlled pauses, limiter + two-pass loudnorm, faster-whisper + difflib alignment, line-start pinning |
| `audio.py` | procedural SFX (pop, whoosh, cash, thud, flip, tick, sparkle, door, boing, riser) + a soft pad ducked under the VO, final mix at −14 LUFS |
| `qc.py` | ffprobe, EBU R128, cut & flash-frame detection, lum/sat per shot, frame extraction, outline thickness measurement, re-transcription of the final mix |

## Full production (SpaceX IPO)
```bash
python -m crayon_engine.vo productions/spacex-ipo/full_vo.json /home/user/work/spacex-ipo/audio_full
python -c "from crayon_engine.vo import realign_per_line as r; r('/home/user/work/spacex-ipo/audio_full')"  # per-line alignment
cd productions/spacex-ipo && python full.py render && python full.py shotlist && python full.py srt && python full.py thumbnail
python qc_full.py <mp4> <qc_dir>
```

## Minimum motion features (request → implementation)
- Instant pose/expression swaps → `expr=`/`pose=` change per frame with no in-betweens (e.g. SH060 every 21 f)
- Constant-speed drift zoom 2–8%/s → `drift(rate, ...)` (linear); measured per shot in `qc_report.md`
- Object pop-in with overshoot → `pop()` 0→108%→98.5%→100% over 7 f
- Falling confetti/money → `fx.confetti`, `fx.money_rain`
- Blinking & breathing → automatic in `character.draw()` (desynced by `seed`)
- Dialogue balloon → `text.balloon()`
- Black card with handwritten write-on → `text.text(..., chars=write_on_chars(...))`
- Desk calendar as a time marker → `props.calendar()`
- Stock chart draw-on → `props.chart(progress=...)`
- Hard cuts synced to word timestamps → `Words.cut()` (0.20 s before the phrase)

## Fonts (OFL 1.1, from npm `@fontsource/*`, converted WOFF→TTF)
Patrick Hand (labels/dialogue), Caveat Bold (chapter cards), Kalam Bold (headlines/signs). Licences are in `fonts/OFL-*.txt`.

## Rules
Do not use real company logos (rockets, tickers, newspapers and buildings are generic). Do not reuse Crayon Capital's characters or mascots.
