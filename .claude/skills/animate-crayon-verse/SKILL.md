---
name: animate-crayon-verse
description: Standar produksi animasi 2D "Crayon Verse". Gaya explainer cartoon dengan karakter kepala bulat, badan bean, dan tungkai garis, outline tebal, cel-shading satu bayangan, serta narasi keuangan/sejarah "Explained Like You're 5". Gunakan saat membuat konsep animasi, character design brief, storyboard, shot list, animation direction, kamera, timing/spacing, menjaga konsistensi karakter, mendeteksi animation bug, atau QC sebelum final render. Disusun dari riset standar industri dan reverse engineering channel YouTube Crayon Capital, tanpa menyalin karakter, aset, atau identitasnya.
---

# animate-crayon-verse

Skill ini adalah **standar kerja produksi animasi 2D explainer** dengan gaya yang kita sebut *Crayon Verse*. Gaya ini dirumuskan dari:

1. Riset standar industri animasi: 12 prinsip Disney, pipeline studio 2D, sinematografi, dan QC. Lihat `references/animation_fundamentals.md` dan `references/professional_animation_pipeline.md`.
2. Audit 36 video channel YouTube **Crayon Capital** (data per 2026-11-26) dan analisis visual 144 frame asli. Lihat `references/crayon_capital_analysis.md`.
3. Reverse engineering keduanya menjadi SOP yang bisa langsung dipakai.

> **Aturan orisinalitas.** Kita meniru *kualitas dan prinsip*, bukan *identitas*. Jangan memakai ulang karakter, maskot, logo, judul, thumbnail, atau aset Crayon Capital. Semua karakter dan palet di proyek baru harus didesain sendiri dengan mengikuti aturan bentuk di bawah.

---

## 1. Kapan skill ini dipakai

Pakai skill ini setiap kali user meminta salah satu hal berikut:

| Permintaan | File yang dibuka |
|---|---|
| Konsep/ide video animasi baru (explainer, finance, sejarah, bisnis) | `workflows/pre_production.md` §1–2 |
| Character design brief / model sheet | `references/character_design_standards.md` |
| Storyboard, shot list, animatic | `workflows/pre_production.md` §4–6, `references/cinematography_and_composition.md` |
| Animation direction, acting, timing, spacing | `references/character_animation_standards.md`, `workflows/production.md` |
| Kamera dan komposisi | `references/cinematography_and_composition.md` |
| Warna dan lighting | `references/lighting_and_color.md` |
| Transisi, editing, sound | `references/transition_and_editing.md`, `workflows/post_production.md` |
| Cek bug atau QC sebelum render | `references/quality_control_and_bug_detection.md`, `workflows/animation_quality_assurance.md`, `checklists/*` |
| Prompt untuk generator gambar/video AI | §10 di bawah + `references/character_design_standards.md` §8 |
| SOP produksi lengkap (17 standar: tujuan, standar, langkah, larangan, kriteria, checklist) | `references/animation_production_sop.md` |
| Contoh nyata per shot (timing, kamera, transisi, hook) dari video referensi | `references/wolf_frame_analysis.md` |

Untuk tugas besar (satu video penuh), ikuti **Workflow Ide → Final Render** di §9 secara berurutan.

---

## 2. Identitas visual Crayon Verse (ringkas)

**Kategori:** 2D vector cartoon explainer dengan karakter, untuk narasi faceless voice-over (narator tidak tampil). Durasi target 10–21 menit (median channel referensi 15:05).

**Ciri yang wajib ada:**

1. **Karakter "kepala bulat, badan bean, tungkai garis".** Kepala lingkaran sempurna yang besar, badan berbentuk telur/bean yang sekaligus jadi pakaian, tangan dan kaki berupa satu garis tebal tanpa volume. Lihat §4.
2. **Outline gelap tebal dan seragam.** Warnanya hampir hitam yang sedikit hangat (`#1A1617`), bukan hitam murni. Ketebalan ±8–10 px di 1080p untuk karakter. Hasil ukur: median 5–6 px di frame 720p.
3. **Cel-shading satu bayangan.** Setiap kepala, rambut, dan badan punya satu bentuk bayangan keras (bulan sabit) di sisi yang menjauhi key light. Tidak ada gradien di karakter.
4. **Hierarki warna = hierarki cerita.** Tokoh utama/bernama memakai warna kulit dan rambut khas. Figuran memakai kepala putih/abu tanpa warna kulit. Kerumunan latar didesaturasi menjadi abu.
5. **Latar penuh dan berwarna (gaya modern).** Latar flat-vector dengan satu hue dominan per lokasi, cahaya atmosferik (sorotan jendela, spotlight, glow), dan depth lewat blur atau desaturasi.
6. **Teks tulisan tangan.** Dialog muncul sebagai teks italic tulisan tangan putih ber-stroke gelap di dekat pembicara, dengan *tick* kecil yang menunjuk ke mulut. Label objek dan angka juga ditulis tangan.
7. **Metafora visual literal (ELI5).** Konsep abstrak digambar sebagai benda konkret: tumpukan uang, karung `$`, gelembung, papan konspirasi, peta, grafik panah merah/hijau.
8. **Efek grafis kartun.** Confetti, uang beterbangan, garis kecepatan/smear, keringat, tanda `!!`/`??`, retakan, asap, api, dan petir. Fungsinya menekankan emosi, bukan dekorasi.

Detail lengkap ada di `references/crayon_capital_analysis.md` §3.

---

## 3. Prinsip animasi yang wajib diperhatikan

Dari 12 prinsip (Thomas & Johnston, *The Illusion of Life*, 1981), urutan prioritas untuk gaya ini adalah:

| Prioritas | Prinsip | Bentuknya di Crayon Verse |
|---|---|---|
| 1 | **Staging** | Satu ide per shot. Karakter frontal, berbaris, mudah dibaca dalam ≤1 detik. Silhouette selalu jelas. |
| 2 | **Timing** | Mengikuti narasi. Aksi utama jatuh tepat pada kata kunci VO. Hold cukup lama agar teks terbaca. |
| 3 | **Exaggeration** | Ekspresi ekstrem: mata sparkle, gigi kertak, rambut berdiri, mulut kotak berteriak. |
| 4 | **Appeal** | Bentuk sederhana dan bulat, proporsi chibi, wajah minimal tapi ekspresif. |
| 5 | **Anticipation** | Squash kecil atau mundur sebelum aksi besar (lompat, lari, kaget). |
| 6 | **Slow in / slow out** | Easing untuk gerak karakter, pop-in, dan gerak kamera cepat. **Pengecualian:** drift zoom latar yang lambat (2–8%/dtk) memang dibuat berkecepatan konstan, sesuai referensi. |
| 7 | **Follow-through & overlapping** | Dasi, rambut, ekor jas, dan kertas tetap bergerak setelah tubuh berhenti. |
| 8 | **Squash & stretch** | Dipakai pada badan bean dan kepala saat jatuh/mendarat. Volume harus konstan. |
| 9 | **Secondary action** | Kedip, napas, keringat, atau props kecil yang mendukung tanpa mencuri fokus. |
| 10 | **Arcs** | Ayunan tangan-garis dan lintasan kepala mengikuti busur. |
| 11 | **Pose to pose** | Dasar seluruh blocking (rig/cut-out). Straight-ahead hanya untuk efek seperti api, asap, dan confetti. |
| 12 | **Solid drawing** | Lingkaran kepala selalu bulat sempurna dan ketebalan outline konsisten. Perspektif props dan latar benar. |

Penjelasan dan contoh penerapan per prinsip: `references/animation_fundamentals.md`.

---

## 4. Standar karakter (wajib)

**Proporsi (berdiri penuh):** tinggi total ≈ 3–3,5 kepala.
- Kepala: lingkaran, diameter ≈ 28–32% tinggi total.
- Badan bean: ≈ 35–40% tinggi total, lebar ≈ 0,9–1,1× diameter kepala. Tidak ada leher; badan menempel langsung di bawah dagu.
- Kaki: dua garis lurus atau sedikit melengkung, ≈ 30% tinggi. Telapak opsional (titik/garis kecil).
- Lengan: satu garis per lengan dari sisi badan (gaya *rubber-hose*). Tangan dihilangkan atau berupa mitten/oval putih sederhana. Tangan detail hanya untuk close-up atau thumbnail.

**Wajah:**
- Mata: dua oval vertikal hitam kecil, opsional highlight putih mungil. Ketinggiannya di garis tengah kepala.
- Alis: stroke pendek melengkung yang mengambang terpisah dari mata. Alis adalah **pemain utama** ekspresi.
- Mulut: garis atau bentuk kecil. Mulut terbuka berisi merah tua plus baris gigi atas putih.
- Hidung: tidak ada (kecuali karikatur tokoh tertentu).
- Wajah ditempatkan sedikit ke arah yang dilihat karakter (sebagai *turn cue* ¾).

**Identitas tokoh = siluet kepala + 1–2 props.** Rambut khas, kacamata, kumis, topi, warna jas/dasi. Satu tokoh harus bisa dikenali dari siluetnya saja.

**Kelas karakter:**
| Kelas | Kepala | Warna | Fungsi |
|---|---|---|---|
| Hero/tokoh bernama | warna kulit + rambut khas | jenuh penuh | fokus cerita |
| Figuran aktif | putih/abu terang | pakaian berwarna | reaksi, dialog pendek |
| Kerumunan latar | abu, desaturasi 60–100% | abu | konteks, tidak mencuri fokus |
| Maskot reaksi (opsional) | desain sendiri | aksen kuat | reaksi kaget di thumbnail/hook |

Spesifikasi lengkap, model sheet, turnaround, dan library ekspresi ada di `references/character_design_standards.md`. Aturan konsistensi ada di `checklists/character_consistency_checklist.md`.

---

## 5. Standar gerakan

- **Frame rate:** video referensi **30 fps**, dengan tween tubuh dan kamera **on ones** [Teramati, 29.774 frame]. Untuk produksi baru: 24 atau 30 fps. Akting boleh on twos bila digambar tangan, tetapi kamera, efek, dan tween rig on ones.
- **Limited animation yang disengaja [Teramati]:** ekspresi dan pose **di-swap instan** tanpa in-between (S5: dua pose bergantian tiap ±21 frame), sedangkan objek lepas (confetti, kertas uang, cairan) dianimasikan penuh on ones. Aksi besar sering terjadi *di cut* (pose sebelum → sesudah).
- **Teknik:** cut-out/rig + tween (After Effects/Moho/Animate/Harmony) untuk badan, kepala, dan kamera; swap drawing untuk mulut/mata/alis; frame-by-frame atau partikel untuk efek. Bukti: interpolasi halus per frame, bentuk identik antar-shot, swap tanpa in-between, motion blur software. Software pastinya **tidak dapat dipastikan**.
- **Hold tidak boleh mati.** Saat diam, karakter tetap kedip tiap 2–5 detik, napas (skala badan 1–2%, siklus 2–3 detik), dan sesekali menggeser alis.
- **Timing referensi (24 fps):** kedip 4–6 frame; *take* kaget = antisipasi 3–4f → pose ekstrem 2f → settle 6–10f; pop-in objek 6–8f dengan overshoot 105–110%; jalan biasa 12f per langkah; lari 6–8f per langkah.
- **Aksi cepat** memakai smear atau multiples 1–2 frame plus speed lines. Jangan memakai motion blur berat pada wajah (lihat QC di `references/crayon_capital_analysis.md` §6).
- **Spacing:** tulis spacing chart untuk aksi hero (`references/animation_fundamentals.md` §6).
- **Topik tragis/sensitif** (perang, perbudakan, korban nyata): kurangi exaggeration dan humor visual, pakai ekspresi lebih tenang, dan tanpa confetti/efek komedik.

Detail ada di `references/character_animation_standards.md` dan `checklists/animation_motion_checklist.md`.

---

## 6. Standar kamera dan komposisi

- **Default [Teramati]:** kamera eye-level frontal dengan **drift zoom lambat berkecepatan konstan** (median 4%/dtk, rentang 2–8%/dtk). Di video referensi, 94 dari 158 shot memakai zoom: 70 pull-out dan 24 push-in; 52 locked-off; 12 pan/tilt. Pull-out dipakai untuk mengungkap konteks (penonton, kerumunan); push-in untuk penekanan. Shake 4–8 frame untuk impact. **Spotlight radial elips di latar** menandai subjek.
- **Kosakata shot gaya ini** (semuanya teramati di referensi):
  1. Establishing wide (lokasi, kendaraan, gedung, peta).
  2. **Lineup**: 3–5 karakter sejajar menghadap kamera di balik meja atau pagar.
  3. Medium 1–3 karakter dengan teks dialog.
  4. Close-up wajah untuk reaksi, dan extreme close-up untuk mulut/gigi atau mata.
  5. Over-the-shoulder dengan kepala besar di foreground.
  6. **Split-screen** 2–3 panel (lurus atau diagonal) untuk perbandingan, telepon, atau "dulu vs sekarang".
  7. Infographic diegetik: grafik di monitor/papan, tumpukan uang berlabel angka, peta.
  8. Metafora panggung: spotlight, tirai, confetti untuk "kemenangan" tokoh.
- **Komposisi:** subjek utama di tengah atau di garis sepertiga. Ruang kosong disiapkan untuk teks dialog. Foreground framing (meja, kepala buram) dipakai untuk depth. Jaga aturan 180° di adegan dialog.

Detail ada di `references/cinematography_and_composition.md`.

---

## 7. Standar lighting dan warna

- Satu **key light** per scene (arah konsisten), shadow keras satu tone (≈ 20–30% lebih gelap, sedikit bergeser ke hue biru/ungu). Tambahkan **rim/bounce berwarna** dari sumber cahaya (jendela biru, lilin oranye, monitor hijau).
- Latar menggunakan 3 band nilai (gelap–sedang–terang) atau gradien lembut. Cahaya atmosferik berupa sorotan diagonal semi-transparan (opacity 10–25%).
- **Mood ditentukan oleh hue lokasi:** biru/teal = netral/kantor/edukatif, merah tua = drama/panggung/bahaya, kuning-emas = kekayaan/kerajaan, abu gelap = krisis/skandal, hijau = pertumbuhan/uang.
- Saturasi median frame ≈ 0,26–0,32. Karakter putih harus kontras terhadap latar mid-value (luminance median ≈ 0,45–0,55).
- Palet token dan resep scene ada di `references/lighting_and_color.md`.

---

## 8. Standar transisi dan QC

- **Transisi default: hard cut on narration beat** [Teramati: 125/157 cut adalah hard cut 1 frame, jatuh median 0,22 dtk sebelum frasa]. **Kartu hitam dengan teks tulisan tangan write-on** untuk judul bab, lompatan waktu, dan punchline (25 cut). Callback/bookend di akhir video. Gunakan match cut atau object/motion transition (whip, wipe oleh objek, zoom ke dalam objek) untuk pergantian bab. Gunakan dip-to-black untuk lompatan waktu besar. Time card ("30 minutes later...") memakai teks italic di pojok kanan bawah.
- **Segmen sponsor** yang gayanya berbeda harus dibungkus bumper keluar-masuk agar tidak terasa sebagai glitch.
- **QC wajib 3 lapis:** (1) self-check animator per shot, (2) review sutradara di animatic dan blocking, (3) final QC full-pass sebelum render. Pakai `workflows/animation_quality_assurance.md` dan keempat checklist. Bedakan *actual error* / *minor imperfection* / *stylistic choice* / *perlu dicek*.

---

## 9. Workflow: dari ide sampai final render

```
[1] Brief & topik ──► [2] Riset & naskah ELI5 ──► [3] VO scratch ──► [4] Script breakdown → shot list
      │                                                                     │
      ▼                                                                     ▼
[5] Character/env design + model sheet ──► [6] Storyboard ──► [7] Animatic (lock timing)
                                                                            │
      ┌─────────────────────────────────────────────────────────────────────┘
      ▼
[8] Asset build & rig ──► [9] Layout ──► [10] Blocking (pose-to-pose) ──► review
      ──► [11] Spline/polish + lip/brow/blink ──► [12] FX & secondary ──► review
      ──► [13] Compositing & lighting pass ──► [14] Edit + sound + music ──► [15] QC full-pass ──► [16] Render & deliver
```

| Tahap | File panduan | Gate (tidak boleh lanjut sebelum…) |
|---|---|---|
| 1–4 | `workflows/pre_production.md` | Naskah final dan shot list berisi durasi per shot |
| 5–7 | `workflows/pre_production.md` | Model sheet disetujui, animatic dikunci dengan VO final |
| 8–12 | `workflows/production.md` | Blocking lulus `animation_motion_checklist` |
| 13–14 | `workflows/post_production.md` | Lulus `scene_quality_checklist` |
| 15–16 | `workflows/animation_quality_assurance.md` | Lulus `final_render_checklist` |

**Mode cepat (konsep atau pitch saja):** kerjakan langkah 1, 2, 4, dan 6 dengan format output di `workflows/pre_production.md` §7.

---

## 10. Template prompt gambar AI (bila produksi memakai generator)

```
2D flat vector cartoon, explainer animation still, 16:9.
Characters: perfectly round large heads, bean/egg-shaped bodies that are the clothing,
single thick line arms and legs (rubber-hose), no neck, tiny vertical oval black eyes,
floating short curved eyebrows, small simple mouth.
Main character: [skin tone] skin, [hair], [prop]; extras: plain white heads, desaturated grey crowd.
Thick uniform dark outlines (#1A1617), hard one-tone cel shadow crescent on heads and bodies,
[key light direction]. Background: fully painted flat vector [location], dominant [hue],
soft atmospheric light shafts, slight depth blur on far background.
Mood: [emotion]. Composition: [shot type], subject [center/thirds], space for handwritten caption.
No gradients on characters, no realistic anatomy, no text unless specified.
```

Selalu cek hasil AI dengan `checklists/character_consistency_checklist.md`. Generator AI sering menghasilkan drift proporsi, jumlah jari, dan ketebalan outline.

---

## 11. Cara memakai referensi

- **Jangan membaca semua file sekaligus.** Buka hanya file pada tabel §1 yang relevan dengan tugas.
- Angka-angka di skill ini diberi label sumber: **[Teramati]** = diukur atau dilihat dari frame referensi, **[Standar industri]** = dari literatur/praktik studio, **[Rekomendasi]** = keputusan desain skill ini. Jangan menyajikan [Rekomendasi] sebagai fakta tentang channel referensi.
- Data mentah audit ada di `references/data/channel_audit.csv` (36 video: views, likes, rasio, tanggal, sumber data).
- **Analisis frame-by-frame video utama** (158 shot dengan timestamp, hook per frame, gerak terukur, transkrip, audio, bug) ada di `references/wolf_frame_analysis.md`, dengan data mentah `references/data/wolf_shots.csv` dan `wolf_transcript.tsv`. Ini sumber bukti paling kuat di skill ini.
- Keterbatasan riset untuk 35 video lain (hanya sampling frame) tercatat di `references/crayon_capital_analysis.md` §1.3.
- Contoh output lengkap untuk 10 jenis tugas (konsep, brief, storyboard, shot list, direction, kamera, spacing, konsistensi, bug, QC) ada di `references/skill_validation.md`. Pakai sebagai contoh format.

## 12. Format output standar

Saat menghasilkan deliverable dengan skill ini, gunakan format berikut:
- **Konsep:** `workflows/pre_production.md` §7.1
- **Character brief:** `references/character_design_standards.md` §9
- **Shot list:** `workflows/pre_production.md` §7.3 (tabel: #, timecode, durasi, shot type, kamera, aksi, ekspresi, teks layar, SFX, transisi)
- **Animation direction per shot:** `references/character_animation_standards.md` §8
- **Laporan QC:** `workflows/animation_quality_assurance.md` §5
