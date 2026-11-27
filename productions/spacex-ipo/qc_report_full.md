# QC Report: The SpaceX IPO Explained Like You're 5, FULL v1 (2026-11-27)

Method: full pass (`workflows/animation_quality_assurance.md` §2) adapted for a cloud session. Duration **10:02.1** · **124 shots** · Reviewer: Claude (automated measurements + review of extracted frames).

**What was actually checked**
- **All 18,064 frames** of the final MP4 were streamed: frame-to-frame difference (cut and flash-frame detection, dead holds), luminance and saturation sampled every 10 frames. Data: `qc_auto_full.json`.
- **Frames viewed visually**: A/M/Z for all 124 shots (372 engine stills, identical code path to the render), plus **frames −1/0/+1 around all 123 cuts taken from the final MP4** (369 frames, `qc_frames_full/cuts_sheet_*.jpg`). Full-resolution detail checks were done on more than 20 frames.
- **Audio**: EBU R128 + true peak on the final MP4. The **final mix and the VO-only master were both re-transcribed** with faster-whisper and compared.
- **Not done** (D): a real-time viewing with sound by a human, and a YouTube private upload.

## Summary
- A: **0** remaining (S1 0, S2 0) · B: **3** open · C (logged): **10** · D: **3**
- **During production: 20 findings were fixed** (table below).
- Release status: **APPROVED WITH NOTES** (ready for human review/listening; see D)

## Technical measurements (final MP4)
| Item | Target | Measured | Status |
|---|---|---|---|
| Duration | 10–12 min | **10:02.1** | ✅ (lower bound) |
| Video | H.264 High, 1920×1080, 30 fps | h264 High, 1920×1080, yuv420p, 30/1, 18,064 frames | ✅ |
| Bitrate | 12–20 Mbps (checklist) | master **8.9 Mbps** (690 MB) · share version 1.0 Mbps (76 MB, visually equal on confetti/text, see below) | B-S4 |
| Audio | AAC 48 kHz stereo | AAC 48 kHz 2 ch ≈233 kbps | ✅ |
| Loudness | −14 LUFS | **−14.0 LUFS** | ✅ |
| True peak | ≤ −1 dBTP | **−4.1 dBTP** (WAV mix master −1.3) | ✅ |
| VO per chapter | −14 LUFS / ≤ −1 dBTP | hook −14.2/−1.2 · ch1 −14.3/−1.2 · ch2 **−14.0/−1.3** (was −0.9, fixed) · ch3 −14.3/−1.2 · ch4 −14.3/−1.2 · ch5 −14.3/−1.2 | ✅ |
| VO pace | ≈149 wpm | 144–153 wpm per chapter (including pauses) | ✅ |
| VO not masked by SFX/music | mix ≈ VO-only | transcript match **mix 0.879 vs VO-only 0.876** (the ~12% gap is number formats such as "$135" vs words, plus long-form whisper drift, not masking) | ✅ |
| Flash frames | 0 | **0** | ✅ |
| Cut → phrase | 0.1–0.3 s | **118/118 cuts that open a phrase at exactly 0.20 s** (+≤1 frame quantisation) | ✅ |
| Cut placement | per timeline | 110/123 auto-detected within ±1 f; the other 13 are low-contrast cuts (same background hue) and **all 123 were confirmed in the −1/0/+1 frame sheets** | ✅ |
| Camera drift | 2–8 %/s, constant | 2.0–6.0 %/s, linear; locked-off only on cards and 2 shots where the subject moves | ✅ |
| Dead holds | 0 | **0** picture shots with >40% unchanged frames (cards excluded) | ✅ |
| Dark frames | median lum < 0.25 for no more than 3 s | **0 shots** (lowest picture shot 0.259, median 0.72) | ✅ |
| Saturation | reference 0.26–0.32 | median HSV-S **0.39** on all frames | B-S4 |
| Shot rhythm | reference 9.5 shots/min, median 5.2 s | **12.4 shots/min, median 4.74 s** | C (denser ELI5) |
| Outline at zoom | constant | 7–8 px at zoom 1.00 → 1.07 (stroke compensation, measured in the pilot, same engine) | ✅ |

## Findings fixed during the full production
| # | Shot | Cat | Sev | Finding | Fix |
|---|---|---|---|---|---|
| 1 | VO ch02 | A | S2 | True peak −0.9 dBTP | limiter loop in `vo.loudnorm()` → −1.3 dBTP |
| 2 | all | B | S3 | Whisper skipped words on 10-minute audio (e.g. line 33) | `realign_per_line()`: one whisper pass per line, 1,282/1,474 words matched |
| 3 | SH330 | A | S2 | The book covered the banker's face | book lowered to hand height |
| 4 | SH340 | A | S3 | "ORDER BOOK" title overlapped the first entry | ledger layout fixed |
| 5 | SH520 | A | S2 | The "▲" glyph is not in the font, so a "?" appeared on the ticker | triangle drawn as a vector |
| 6 | SH500 | B | S3 | Elon "stood on the pizza" | blocking moved; he now points at the pizza |
| 7 | SH590, SH650, SH670, SH725 | A | S3 | Labels cut by the frame edge, or write-on not finished before the cut | position/start time moved |
| 8 | SH970–990 | A | S3 | Names under the scale cut off; tower labels at the top edge | geometry and labels moved |
| 9 | SH190, SH220, SH390 | A | S2 | Empty/black frame on the cut (SH220 looked like a dip-to-black) | content in frame from the cut; objects pop on the words |
| 10 | SH220, SH300, SH560 | B | S3 | Dead holds | 2–5 %/s drift |
| 11 | 20 shots (chart, space, night) | B | S3 | Median luminance 0.12–0.25 over 3 s | background bands brightened (hue kept), all ≥ 0.26 |
| 12 | all BG | B | S4 | Saturation above the reference | background desaturation 22% (0.405 → 0.394) |
| 13 | SH810, SH875, SH740, SH375, SH410/420, SH290, SH550, SH390 | B | S4 | Composition / readability (empty space, labels too small, arrow direction, overlapping elements) | adjusted per shot |
| 14 | thumbnail | B | S4 | Contact shadow floating under a mid-air character | character now rides the rocket, no floor shadow |
| 15 | full.srt | B | S4 | Subtitles used TTS spelling ("one hundred and thirty-five dollars") | `script_text.display()`: digits, dates and acronyms restored |

## Open findings
| # | Cat | Sev | Description | Recommendation |
|---|---|---|---|---|
| O1 | B | S4 | Median saturation 0.39 > reference 0.26–0.32 (the reference metric may differ) | desaturate props/characters too, or calibrate the metric against the reference frames |
| O2 | B | S4 | Master bitrate 8.9 Mbps < checklist 12 Mbps | 2-pass encode at 14 Mbps if the platform needs it (YouTube recommends 8 Mbps for 1080p30 SDR) |
| O3 | B | S4 | Duration 10:02 sits at the lower bound of 10–12 min | add 1–2 examples in Ch 2/4 if you want ~11 min |

## Stylistic choices confirmed (C)
1. Instant pose swaps (SH060/SH630/SH1100, every 18–21 f), reference limited animation.
2. Grey face → colour on the frame of "SpaceX" (hook) + **bookend** SH1100 = the same launch pad, with the queue now revealed.
3. Linear camera drift; big actions on the beat without anticipation.
4. Tweens on ones (30 fps); no lip-sync (faceless narrator).
5. **Price charts are simplified**: the labelled points are real (sources B1, B4, C3–C7, C9, C11); the line between them is illustrative and says "(simplified)" on screen.
6. Companies (Anthropic, OpenAI, Databricks, Stripe, banks) appear as **generic characters/silhouettes + handwritten labels**, never real logos or brand colours.
7. Black punchline cards ("The fear did more damage than the flood.", "A great company and a great stock…").
8. Chapter cards with handwritten write-on; time markers = desk calendar (APR 1, MAY 20, JUN 4/11/12/16, AUG 4/6, NOV 18, DEC 8, 2027?).
9. Pizza metaphor callbacks (dilution, toppings, lesson 3) + diary (S-1) + popcorn (IPO pop).
10. Shot rhythm denser than the reference (12.4/min): ELI5 with many definitions.

## Unverified (D)
1. **Human real-time viewing with sound** (clicks/pops, SFX feel, bed level, whether the jokes land).
2. **Platform test** (YouTube private, desktop + phone, compression of the share file).
3. **Facts after the training cutoff**: everything is logged in `sources.md` (§A–D, H). Re-check on the publish date: **C8** (the identity of "Customer B" comes from Bloomberg, unconfirmed), **C9** (latest price, 25 Nov), **D1** (Anthropic's share price after its IPO), **D2/D3** (OpenAI timing, Databricks/Stripe).

## Checklist results (summary)
- **character_consistency**: ✅ every §A/§B item (one `Look` per character, outline constant, single key light, ≤1 skin-coloured hero per frame; the AI-company mascots are white-headed extras). ⚠️ The 5-view turnaround is still not made (front + ¾ via `facing` only).
- **scene_quality**: ✅ focal point, grayscale (white heads vs mid-value backgrounds), title-safe, 180°, consistent location hues, red/green always with arrows/labels, FX never on faces, text/numbers match `sources.md`. Text hold time: fixed where it was short (#7).
- **animation_motion**: ✅ action on the keyword (±0 f), holds ≥ 12 f, read ≥ 1.5 s, easing on pops/slides/flights, arcs (slices, envelope), moving holds + desynced blinks, pop-in 108%. ⚠️ Follow-through on ties/hair has not been added yet.
- **final_render**: ✅ 0 S1/A-S2, no placeholders, licences (OFL fonts, procedural SFX/music, Kokoro Apache-2.0), generic logos, −14 LUFS/TP ≤ −1, `full.srt`, thumbnail 1280×720 (`assets/thumbnail.png`), title + sources ready. ⚠️ ProRes master not made (H.264 only); B bitrate (O2); D platform.
