# Workflow: Post-production

Input: shot teranimasi + FX + lighting pass.
Output: master video, versi YouTube, thumbnail final, laporan QC.

---

## 1. Compositing
1. Susun layer per shot: `BG_far` → `BG_mid` → `BG_near` → karakter → `FG` → `LIGHT_overlay` → FX → teks.
2. Depth: blur BG jauh 4–12 px dan FG 8–16 px bila diperlukan. Karakter fokus selalu tajam.
3. Bayangan kontak dan ambient occlusion sederhana di tempat karakter menyentuh objek.
4. Color cast lingkungan (multiply/overlay 15–35%) untuk adegan bercahaya kuat.
5. Cek di grayscale: tokoh fokus harus kontras nilai terhadap latarnya.
6. Jalankan `checklists/scene_quality_checklist.md` per shot.

## 2. Color correction dan grading
1. Grade per **sekuens** (bukan per shot).
2. Samakan nilai lokasi yang berulang dengan BG key (`references/lighting_and_color.md` §3).
3. Mood bab: krisis (−sat, +kontras), flashback (sepia 10–15%), resolusi (+nilai).
4. Target luminance median 0,40–0,55 dan saturasi median 0,25–0,35.

## 3. Editing
1. Conform shot ke timeline animatic (durasi terkunci).
2. Transisi mengikuti hierarki (`references/transition_and_editing.md` §1).
3. Teks layar: posisi, font, durasi baca (≥ 1 detik per 3 kata), safe area 90%.
4. Re-hook visual setiap 2–4 menit.
5. Segmen sponsor dibungkus bumper.
6. End screen: 20 detik terakhir menyisakan ruang untuk elemen end screen YouTube (2 video + subscribe).

## 4. Sound design dan musik
1. Bersihkan VO (noise reduction, de-ess, EQ, kompresi ringan).
2. Spotting SFX dari shot list: setiap pop, whoosh, impact, uang, stempel.
3. Sinkron SFX impact tepat di frame kontak (±1 frame).
4. Music bed per bab, ducking −18 s/d −24 dB di bawah VO.
5. Stinger di reveal; hening 6–12 frame sebelum reveal besar.
6. Ambience pelan per lokasi.
7. Master: −14 LUFS integrated, true peak ≤ −1 dBTP.
8. Dokumentasikan lisensi semua musik dan SFX.

## 5. Thumbnail final
1. Render premium dari model karakter yang sama: lighting volumetrik, glow, tekstur.
2. Komposisi: 1 wajah emosi kuat (tengah/sepertiga), 1–3 kata raksasa (sans-serif tebal putih + bayangan, atau banner aksen), 1 simbol (grafik, logo generik, bubble, papan konspirasi), maskot reaksi milik sendiri di pojok (opsional).
3. Uji di 320×180 (terbaca?) dan 168×94 (siluet terbaca?).
4. Kontras dengan UI YouTube terang dan gelap.
5. Konsistensi: siluet, warna, dan props tokoh sama dengan di video.

## 6. Render dan delivery
| Deliverable | Spesifikasi |
|---|---|
| Master | 1920×1080 (atau 3840×2160), 24 fps, ProRes 422 HQ / DNxHR HQ, audio WAV 48 kHz 24-bit |
| YouTube upload | H.264 High Profile, bitrate 12–20 Mbps (1080p) / 35–45 Mbps (4K), AAC 320 kbps 48 kHz |
| Thumbnail | 1280×720 JPG/PNG < 2 MB |
| Subtitle | SRT dari naskah final |
| Arsip | project file + aset + lisensi |

Tips anti-artefak: render 4K walau sumber 1080p dapat menaikkan bitrate yang dialokasikan YouTube; hindari blur besar dan confetti padat berlebihan, karena keduanya rawan blocking setelah kompresi.

## 7. Final QC
Jalankan `workflows/animation_quality_assurance.md` (full pass) + `checklists/final_render_checklist.md` sebelum upload publik. Upload **private/unlisted** terlebih dahulu dan cek hasil kompresi.
