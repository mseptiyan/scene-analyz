# Workflow: Production

Input: animatic terkunci, shot list, model sheet, BG key.
Output: semua shot teranimasi, dengan FX dan pass lighting dasar, siap di-comp.

---

## 1. Asset build
1. Bangun karakter sebagai vektor berlapis dengan penamaan `CHR_<nama>_<bagian>`:
   `head`, `head_shade`, `hair`, `hair_shade`, `hair_hl`, `brow_L`, `brow_R`, `eye_L`, `eye_R`, `mouth` (switch), `body`, `body_shade`, `collar/tie`, `arm_L`, `arm_R`, `leg_L`, `leg_R`, `contact_shadow`, `props_*`.
2. Kepala = shape primitif lingkaran (jangan path freehand).
3. Outline: stroke `#1A1617`, 8–10 px @1080p, round cap.
4. Bank: simpan badan (jas/kemeja/seragam/gaun/kaos), rambut, aksesori, ekspresi, dan props sebagai library yang bisa dipakai ulang.
5. BG: per lokasi, dengan layer `BG_far`, `BG_mid`, `BG_near`, `FG`, `LIGHT_overlay`.

## 2. Rigging
1. Root → body → head (pivot di dasar kepala) → wajah (switch layer) .
2. Lengan dan kaki: rubber-hose (titik bahu/pinggul, siku/lutut opsional, ujung). Kunci panjang agar tidak memanjang tidak wajar.
3. Smart control atau slider untuk: arah toleh (wajah bergeser 0–15% Ø), squash badan, napas.
4. Swap set: alis (8+), mata (8+), mulut (9 fonem + 8 ekspresi).
5. **Rig test (wajib):** pose ekstrem (lengan di atas kepala, duduk, jongkok, toleh penuh, squash 120%). Lulus bila tidak ada robek, outline tetap rata, dan volume terjaga.

## 3. Layout
1. Impor panel animatic sebagai referensi per shot.
2. Tempatkan BG, karakter (ukuran sesuai shot size), props, kamera.
3. Catat **arah key light** di nama shot/metadata.
4. Verifikasi aturan 180°, eyeline, screen direction, headroom untuk teks.
5. Pose awal dan akhir shot sesuai handoff dari shot sebelumnya/berikutnya.

## 4. Blocking (pose to pose)
1. Key pose storytelling di frame kata kunci VO (lihat `references/character_animation_standards.md` §7).
2. Tambahkan extremes dan antisipasi.
3. Set interpolasi **step/hold** saat blocking (tanpa interpolasi halus) untuk menilai pose dan timing murni.
4. Tambahkan ekspresi (alis-mata-mulut) di setiap key.
5. **Review blocking** dengan director: staging, akting, timing. Revisi di tahap ini, bukan setelah polish.

## 5. Spline dan polish
1. Ubah ke interpolasi bezier. Atur easing (slow in/out).
2. Breakdown untuk arc: periksa trail ujung lengan dan kepala.
3. Overlap dan follow-through: dasi, rambut, kertas (offset 2–4 frame).
4. Step karakter ke **on twos** (kecuali aksi cepat yang disengaja on ones).
5. Moving hold untuk semua karakter yang terlihat: napas, kedip acak, mikro-alis.
6. Lip/flap sync ke VO; bentuk mulut mendahului suara 1–2 frame.
7. Smear/multiples 1–2 frame pada aksi cepat (gambar manual di atas rig).
8. Bayangan kontak mengikuti kaki.

## 6. FX dan secondary
| FX | Teknik | Catatan |
|---|---|---|
| Confetti, koin, uang terbang | partikel atau straight-ahead | jangan menutupi wajah tokoh utama |
| Asap, debu | frame-by-frame on twos | 3–4 bentuk, menghilang dengan shrink |
| Api | loop 6–8 drawing on twos | warna `gold` → `loss` |
| Retakan impact | draw-on 2–3 frame | bersama camera shake |
| Speed lines | garis horizontal ink 40–80% opacity | 2–4 frame |
| Keringat, `!!`, `?!` | pop 2–3 frame + wobble | di sisi kepala yang tidak tertutup teks |
| Glow | radial blur screen | objek berharga/teknologi |
| Stempel | slam scale + shake | teks tebal di kotak merah miring |

## 7. Lighting pass (di scene)
1. Shadow sabit di sisi berlawanan key light (seragam dalam scene).
2. Rim berwarna bila ada sumber cahaya berwarna.
3. Overlay atmosfer (sorotan, spotlight, vignette) sesuai `references/lighting_and_color.md` §5.
4. Desaturasi kerumunan dan blur latar untuk depth.

## 8. Self-check animator (sebelum kirim ke comp)
Jalankan `checklists/animation_motion_checklist.md` dan `checklists/character_consistency_checklist.md` §B untuk setiap shot. Kirim shot dengan catatan:
```
SHOT: SQ030_SH0120 v003
Status: polish selesai
Self-check: motion ✓ consistency ✓
Catatan: smear 2f di f48–49 (disengaja, kategori C)
```
