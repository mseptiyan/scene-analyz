# QC Report: The SpaceX IPO, PILOT v1 (2026-11-27)

Method: full pass (`workflows/animation_quality_assurance.md` §2), adapted for a cloud session. Duration: 00:59.63 · 17 shots · Reviewer: Claude (automated measurements + review of extracted frames).

**What was actually checked**
- **Every frame (1,789)**: frame-to-frame difference (cut detection, flash frames, dead holds), luminance and saturation sampled every 6 frames. Script: `qc_auto.json`.
- **Frames viewed visually**: A/M/Z for all 17 shots (51 frames, `qc_frames/contact_{A,M,Z}.jpg`), ±3 frames around all 16 cuts (112 frames, `qc_frames/cuts_sheet.jpg`), plus 8 full-resolution frames for detail checks.
- **Audio**: EBU R128 + true peak on the final MP4. The **final mix was re-transcribed** with faster-whisper to prove the VO is not masked by SFX or the bed.
- **Not done** (open items, see D): a real-time viewing with sound by a human (Pass 1–2), and a YouTube private upload (Pass 7). I cannot listen to audio or watch video in real time, so audio was judged from measurements and transcription.

## Summary
- A: **0** (S1 0, S2 0) · B: **4** · C (logged): **8** · D: **3**
- Release status: **APPROVED WITH NOTES** (pilot for direction review, not a public release)

## Technical measurements (final MP4)
| Item | Target | Measured | Status |
|---|---|---|---|
| Container/codec | H.264 High, yuv420p | h264 High, 1920×1080, yuv420p | ✅ |
| Frame rate | 30 fps constant (brief) | 30/1, 1,789 frames, 59.63 s | ✅ |
| Video bitrate | 12–20 Mbps (checklist) | ≈10.3 Mbps (ABR target 14, flat cartoon content compresses well) | B-S4 |
| Audio | AAC 48 kHz, stereo | AAC 48 kHz 2 ch, ≈225 kbps (requested 320k, VBR result) | ✅ |
| Loudness | −14 LUFS integrated | **−14.0 LUFS** | ✅ |
| True peak | ≤ −1 dBTP | **−4.3 dBTP** (WAV mix master: −1.3 dBTP) | ✅ |
| VO per chapter | −14 LUFS / ≤ −1 dBTP | hook −14.2 / −1.2 · ch1 −14.2 / −1.2 | ✅ (±0.2 LU) |
| VO pace | ≈149 wpm | hook 157.6 wpm, ch1 146.6 wpm (including pauses) | ✅ |
| VO intelligibility over SFX/bed | readable | re-transcription of the final mix matches the script **94.9%** (the differences are number formats only: "$135" vs. "one hundred and thirty-five") | ✅ |
| Flash frames | 0 | **0** | ✅ |
| Cut → phrase | 0.1–0.3 s before the phrase | **0.20 s** on all 13 cuts that open a phrase (the other 3 are card/end-slate cuts) | ✅ |
| Cuts in the right place | per timeline | 14/16 auto-detected within ±1 frame; the other 2 (white→white SH010→020, gold→gold SH080→090) are low-contrast and were confirmed visually | ✅ |
| Camera drift | 2–8 %/s constant | 13 shots 2.0–5.0 %/s (linear); 2 cards locked-off; SH060 −2.8 %/s | ✅ |
| Outline at zoom | constant | head outline 7 px @zoom 1.00 → 8 px @zoom 1.07 (stroke compensated; threshold lum < 0.18) | ✅ |
| Dead holds | 0 | 0% unchanged frames on all 15 picture shots; cards 61% / 84% (static text after write-on, intentional) | ✅ |

Luminance (median) per shot: white 0.99 · gold 0.72 · market 0.61 · doors 0.37 · newspaper 0.30 · launch pad 0.25 · club 0.25 · chart 0.16 (2.6 s, under the 3 s limit for luminance < 0.25).

## Findings
| # | TC | Shot | Cat | Sev | Description | Evidence | Fix | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | 00:02.35 | SH020 | A | S2 | "$135" appeared **before** it was spoken: token "one" matched the word "One" at the start of the line | old contact_A | `T(1,"one",1)` (2nd occurrence) | **fixed** |
| 2 | 00:08.0 | SH030 | A | S2 | Falling bills covered the hero's face (FX in front of the face) | old SH030_Z | rain drawn behind the character | **fixed** |
| 3 | 00:22.0 | SH060 | A | S2 | Foreground crowd arms crossed the neighbours' heads (looked like scribbles) | old SH060_Z | foreground crowd without arms (`crowd(arms=False)`), cheering by bob only | **fixed** |
| 4 | 00:39.5 | SH130 | A | S3 | Reverse angle broke the 180° rule: the bouncer stayed on the left | old SH130 | bouncer moved screen-right, on the crowd side | **fixed** |
| 5 | 00:10.6 | SH040 | B | S3 | "$225 / +67%" labels only on screen for 0.5 s (rule: ≥ 1 s per 3 words) | timing | draw-on 2.0 → 1.35 s, labels on screen ≈ 1.2 s | **fixed** |
| 6 | 00:24.5, 00:50.0 | SH080, SH160 | B | S3 | Pop-in started exactly on the cut, so the first frame was near-empty | old contact_A | pre-rolled pop (≈45% on the cut frame) | **fixed** |
| 7 | 00:24.5–00:56 | SH080/100/160 | B | S3 | Dead holds (72–83% unchanged frames) | qc_auto | 2–2.5 %/s drift added | **fixed** |
| 8 | 00:31–00:40 | SH060, SH110–130 | B | S3 | Dark scenes (lum 0.18) | qc_auto | bands brightened, lum now 0.25 | **fixed** |
| 9 | 00:11.1 | SH050 | B | S4 | 7-word headline readable for ≈2.15 s (rule ≈2.3 s). The headline is large and repeats the VO | timing | slide-in sped up 0.75 → 0.5 s | partly fixed, open |
| 10 | whole video | — | B | S4 | Median HSV saturation on coloured shots 0.48–0.73, above the reference's 0.26–0.32 (white shots 0.01). The reference metric may differ | qc_auto | desaturate BG bands 10–15% in the full production | open |
| 11 | whole video | — | B | S4 | Video bitrate 10.3 Mbps < 12 Mbps recommendation | probe | 2-pass/higher target for the final master | open |
| 12 | whole video | — | B | S4 | Median shot 2.66 s vs. reference 5.2 s: dense pilot (hook + definitions) | shotlist | Ch 2–5 target 4–6 s per shot | open (carried into full production) |

## Stylistic choices confirmed (C)
1. Instant pose swaps with no in-betweens (SH060, every 21 f) = the reference's limited animation.
2. Grey face → colour exactly on the frame of the word "SpaceX" (anonymous → reveal).
3. Linear (unease) camera drift, as measured in the reference.
4. Big actions with no anticipation (doors, pop-ins): the action happens "on the cut/beat", as in the reference.
5. Character tweens on ones (30 fps), not on twos; the reference was also measured on ones.
6. No lip-sync: faceless narrator. The bouncer's lines use a balloon.
7. Slices "float" above the investors' phones in SH150 (bought through the app = digital).
8. Generic tickers ("ABC", "XYZ", "PIZZA") + SPCX (factual), no real logos.

## Unverified (D)
1. **Human real-time viewing with sound** (clicks/pops, SFX feel, bed level). Measurements are good, but no one has listened yet.
2. **Platform test** (YouTube private, desktop + phone).
3. **Facts after the cutoff**: the pilot only uses A1–A8 / B4 / C5 (✅ in `sources.md`). The Ch 4–5 lines marked 🔎/⚠️ must be re-checked when the full video is locked.

---

## Checklist results

### character_consistency_checklist
**§A Design & model sheet:** ✅ perfect round head · ✅ 3.2 × D · ✅ no neck (overlap 0.1 D) · ✅ bean 1.0 D · ✅ limbs single line (1.15 × outline) · ✅ oval eyes + floating brows · ✅ outline `#1A1617` 8 px round cap (measured 7–8 px) · ✅ flat fill + 1 crescent · ✅ colour classes · ✅ silhouette + props differ · ✅ HEX base/shadow (+ hair highlight) · ⚠️ **turnaround 5 views not made yet** (front + ¾ via `facing` only); 12 expressions ✅; mouth shapes 7 ✅; poses 10 ✅ · ✅ original design (no Crayon Capital mascot) · ✅ light caricature.
**§B Per shot:** ✅ identical HEX (one `Look` object per character) · ✅ identity props present · ✅ outline constant under zoom · ✅ shadow on the same side (single key light, upper-left) · ✅ no morphing (procedural geometry) · ✅ expressions match the script · ✅ ≤ 1 skin-coloured hero per frame · ✅ consistent costume.
**§C AI images:** not applicable (no generative AI images; everything is code).

### scene_quality_checklist
✅ one focal point per shot · ✅ grayscale test (white heads/outline vs. mid-value backgrounds) · ✅ subject centre/thirds · ✅ headroom for text · ✅ important text inside title-safe; bottom-right clear · ✅ 180° (after fix #4) · ✅ max 3 consecutive shots with the same size+angle · ✅ consistent location hue (club, gold, white) · ✅ props consistent (rope: 3 gold posts) · ✅ depth: grey crowd as a layer · ✅ one key light · ✅ overlays never cover faces · ✅ red/green always with arrows/labels (chart, newspaper, ticker ▲▼) · ✅ text/numbers match the script + `sources.md` ($135, $75 B, $225 rounded from $225.64, +67% computed, 24 years) · ✅ white text + ink stroke · ⚠️ text hold time: #9 · ✅ balloon tick points at the speaker · ✅ FX never cover faces (after #2) · ✅ no heavy blur · ✅ contact shadows · ✅ held objects attached to the hand anchor.

### animation_motion_checklist
✅ main action on the keyword (pop/reveal/doors/labels at the word start, ±0 frames) · ✅ end poses held ≥ 12 f before the cut · ✅ read hold ≥ 1.5 s (min 1.56 s) · C anticipation (see C4) · ✅ easing on pops, slides, doors, slice flights (camera linear by design) · ✅ arcs (slices fly on a parabola; waving arm) · ⚠️ follow-through only on loose objects (confetti, money); no ties/hair yet → enhancement for the full production · N/A squash & stretch (no jumps/landings in the pilot) · ✅ secondary action (blink, breath, sweat, twinkling stars, swaying searchlights) · ✅ moving holds on every character, **blinks desynced** (seed) · ✅ pop-in 7 f, overshoot 108% · N/A walk/run/take · C lip-sync · ✅ 1 camera move per shot · ✅ outline does not change on zoom · ✅ no flicker/boil (deterministic rendering).

### final_render_checklist
✅ 0 S1, 0 A-S2 · ✅ no placeholders ("To be continued" is the intended pilot slate) · ✅ facts on screen checked (`sources.md`) · ✅ licences: fonts OFL 1.1 (`tools/crayon_engine/fonts/OFL-*.txt`), SFX + pad procedural (no samples), Kokoro-82M Apache-2.0 · ✅ logos generic · ✅ 1920×1080 · C 30 fps (brief + reference; the checklist says 24) · ⚠️ ProRes master not made yet (H.264 only) · B bitrate (#11) · ✅ no black/flash frames · N/A end screen (pilot) · ✅ −14 LUFS / TP ≤ −1 · ✅ VO clear (94.9%) · ✅ SFX sync (cues at word times) · D clicks/pops (#D1) · ✅ 48 kHz 24-bit WAV master · D platform (#D2) · ⚠️ thumbnail: concept only (`concept.md`) · ✅ subtitles `pilot.srt` · ✅ title options + sources ready · ✅ archive: code, script, VO timings, model sheet committed to git (video/WAV are not committed; they can be reproduced).
