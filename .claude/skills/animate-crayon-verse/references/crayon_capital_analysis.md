# Crayon Capital: Audit Channel dan Analisis Visual

> Dokumen bukti untuk skill `animate-crayon-verse`. Semua angka di sini berasal dari data yang benar-benar diambil pada **2026-11-26**. Setiap klaim visual diberi label **[Teramati]** (terlihat di frame), **[Inferensi]** (kesimpulan yang masuk akal dari bukti, tapi belum pasti), atau **[Tidak dapat diverifikasi]**.
>
> Tujuan dokumen ini adalah memahami *kualitas dan sistem* produksi, bukan menyalin. Jangan memakai ulang karakter, maskot, judul, atau aset channel ini.

---

## 1. Metode dan keterbatasan

### 1.1 Sumber data
| Data | Sumber | Cakupan |
|---|---|---|
| Daftar video, durasi, views | Tab Videos channel `youtube.com/@crayon_capital` (via yt-dlp flat-playlist) | 36/36 video |
| Likes + views + tanggal terbit tepat | RSS resmi YouTube `feeds/videos.xml?channel_id=UCP9RPj_BG0vit2TNM7LuRxA` (`media:starRating count` = like count) | 15 video terbaru |
| Likes + views (video lebih lama) | Cache publik Return YouTube Dislike API (`likes` = like count publik YouTube saat di-cache) | 21 video sisanya |
| Tanggal terbit (video lama) | Perkiraan dari teks relatif "x months/1 year ago" di tab Videos | presisi bulan; label `~` |
| Subscriber | Tab Videos: 327.000 (2026-11-26) | — |
| Konteks pesaing/strategi | OutlierKit (analisis pihak ketiga, angka estimasi AI, data per 2026-09-16) | sekunder |
| Frame visual | Gambar statis YouTube per video: `maxresdefault` (thumbnail) + `maxres1/2/3` (frame otomatis 1280×720) | **144 gambar** (4 × 36) |

### 1.2 Metode analisis visual (jujur)
- Metode yang dipakai adalah **sampling frame**, bukan frame-by-frame dan bukan shot-by-shot.
- Untuk tiap video tersedia 3 frame otomatis YouTube. Menurut konvensi umum, posisinya ≈ 25%, 50%, dan 75% durasi, tapi ini **tidak didokumentasikan resmi**, jadi semua timestamp di dokumen ini adalah perkiraan (`≈`). Ditambah 1 thumbnail kustom.
- Video utama (Wolf of Wall Street) hanya punya 4 gambar. Gaya keseluruhan dianalisis dari 108 frame isi + 36 thumbnail lintas channel, ditambah pengukuran kuantitatif (palet k-means, saturasi, luminance, ketebalan garis lewat run-length piksel gelap).

### 1.3 Keterbatasan (wajib dibaca sebelum membuat klaim)
1. **File video penuh tidak dapat diakses.** Halaman watch YouTube mengembalikan halaman verifikasi bot (`google.com/sorry`) untuk IP container ini, dan host streaming video tidak diizinkan jaringan. Akibatnya:
   - **Hook 0–5 detik tidak teramati.** Analisis hook di §5.2 hanya mencakup *packaging* (judul+thumbnail). Standar hook di skill adalah [Rekomendasi].
   - **Breakdown shot-by-shot dengan timestamp nyata tidak mungkin dibuat.** Yang ada adalah katalog tipe shot dari 108 frame sampel.
   - **Gerak, timing, fps, transisi, dan kamera bergerak** hanya bisa disimpulkan dari jejak statis (smear, motion blur, multiples) dan diberi label [Inferensi].
2. **Audio (narasi, musik, SFX) tidak teramati.** Standar sound di skill = [Standar industri]/[Rekomendasi].
3. **Transkrip tidak tersedia.** Layanan transkrip pihak ketiga tidak dapat dibaca saat riset.
4. **Jumlah komentar tidak tersedia** per video. Rata-rata comment rate kanal menurut Playboard ≈ 0,09% (pihak ketiga).
5. Data likes RYD adalah nilai cache. Video yang tumpang tindih dengan RSS menunjukkan selisih < 0,5% (contoh: `wu398eFxGMg` 1.169 vs 1.170), sehingga dinilai andal.
6. Tanggal bertanda `~` berpresisi bulan. Video bertanda "2025-11~" diterbitkan **paling lambat** sekitar Nov 2025 ("1 year ago"); menurut OutlierKit beberapa terbit sekitar Sep–Okt 2025.

---

## 2. TAHAP 1: Audit channel

### 2.1 Ringkasan statistik (36 video)
| Metrik | Nilai |
|---|---|
| Subscriber | 327.000 |
| Total views (36 video) | 28.091.122 |
| Total likes | 494.911 |
| **Median likes** | **7.503** (Q1 4.026, Q3 16.301) |
| Rata-rata likes | 13.748 (terdistorsi outlier) |
| Median views | 444.476 (Q1 195.778, Q3 1.119.877) |
| Median rasio likes/views | 1,99% (Q1 1,49%, Q3 2,47%; rata-rata 2,00%, SD 0,63) |
| Median durasi | 15:05 (rentang 10:15–21:25) |
| Format "Explained Like You're 5" (17 video) | median likes 10.317, views 551.973, rasio 2,12% |
| Format lain (19 video) | median likes 4.466, views 304.185, rasio 1,82% |

Format ELI5 unggul ±2,3× pada median likes dan lebih tinggi pada rasio. Ini mendukung klaim OutlierKit bahwa ELI5 adalah formula utama.

### 2.2 Inventaris lengkap (urut skor engagement komposit)
Skor komposit = 0,45 × peringkat likes + 0,25 × peringkat views + 0,30 × peringkat rasio (dibalik ke skala 1–36). Bobot ini mengikuti prioritas brief: likes didahulukan, lalu views, lalu rasio. Data mentah: `data/channel_audit.csv`.

| # | Judul | Durasi | Terbit | Views | Likes | Likes/Views | ×median likes | Sumber |
|---|---|---|---|---:|---:|---:|---:|---|
| 1 | [The Wolf of Wall Street Scam Explained Like You're 5](https://www.youtube.com/watch?v=HawmGu7oNrc) | 16:33 | 2025-11~ | 4,311,233 | 80,296 | 1.86% | 10.7 | RYD |
| 2 | [The 2008 Financial Crisis Explained Like You’re 5](https://www.youtube.com/watch?v=KE-WJevx-7c) | 13:26 | 2025-11~ | 2,388,328 | 50,517 | 2.12% | 6.73 | RYD |
| 3 | [The Great Depression Explained Like You’re 5](https://www.youtube.com/watch?v=LuEcoqizj0o) | 16:29 | 2025-11~ | 3,058,628 | 45,910 | 1.5% | 6.12 | RYD |
| 4 | [Palantir Technologies Explained Like You’re 5](https://www.youtube.com/watch?v=GSkySDNmjV8) | 15:19 | 2026-01~ | 1,105,917 | 23,937 | 2.16% | 3.19 | RYD |
| 5 | [The Worst Time to be Rich as a Human](https://www.youtube.com/watch?v=wOjdbltaXSQ) | 20:29 | 2026-03~ | 516,439 | 14,704 | 2.85% | 1.96 | RYD |
| 6 | [The AI Bubble Explained Like You're 5](https://www.youtube.com/watch?v=kx_okFl98Vw) | 12:13 | 2025-12~ | 551,973 | 14,199 | 2.57% | 1.89 | RYD |
| 7 | [The Man Who Built Singapore in One Generation](https://www.youtube.com/watch?v=y51JjcymEAY) | 16:09 | 2026-01~ | 1,220,709 | 22,240 | 1.82% | 2.96 | RYD |
| 8 | [Rockefeller: The First Confirmed Billionaire (And How He Did It)](https://www.youtube.com/watch?v=sMH8WchxQR8) | 20:16 | 2026-03~ | 1,794,770 | 27,014 | 1.51% | 3.6 | RYD |
| 9 | [NVIDIA Explained Like You're 5](https://www.youtube.com/watch?v=1GowFTjbUnk) | 14:30 | 2026-07-09 | 2,089,153 | 30,600 | 1.46% | 4.08 | RSS |
| 10 | [How Jeff Bezos Actually Built Amazon](https://www.youtube.com/watch?v=rSgS4wNLLDM) | 20:13 | 2025-12~ | 1,233,114 | 20,892 | 1.69% | 2.78 | RYD |
| 11 | [The $63 BILLION Company That Sold Nothing](https://www.youtube.com/watch?v=VSbO8vmZNm0) | 13:13 | 2025-11~ | 1,161,755 | 19,780 | 1.7% | 2.64 | RYD |
| 12 | [The Dot-Com Bubble Explained Like You're 5](https://www.youtube.com/watch?v=CCXYfrAfW6g) | 12:09 | 2025-11~ | 488,135 | 10,980 | 2.25% | 1.46 | RYD |
| 13 | [The Rise of Anthropic Explained Like You're 5](https://www.youtube.com/watch?v=H5GYXhpE5yI) | 17:51 | 2026-10-16 | 1,275,940 | 15,141 | 1.19% | 2.02 | RSS |
| 14 | [Iran War Explained Like You're 5](https://www.youtube.com/watch?v=wu1GfDhAYvE) | 12:11 | 2026-04~ | 204,722 | 6,538 | 3.19% | 0.87 | RYD |
| 15 | [Petrodollar Explained Like You're 5](https://www.youtube.com/watch?v=9r-45QPLl-Y) | 11:20 | 2026-05~ | 360,269 | 8,732 | 2.42% | 1.16 | RYD |
| 16 | [NVIDIA Scandal Explained Like You're 5](https://www.youtube.com/watch?v=eS1zZKHFzwE) | 14:30 | 2026-11-14 | 652,321 | 10,317 | 1.58% | 1.38 | RSS |
| 17 | [Elon Musk: The First Confirmed Trillionaire (and How He Did It)](https://www.youtube.com/watch?v=npoPedEq3hs) | 19:10 | 2026-08-11 | 626,493 | 9,432 | 1.51% | 1.26 | RSS |
| 18 | [Xi Jinping: China’s Most Powerful Leader (And How He Did It)](https://www.youtube.com/watch?v=RB-DTXw1Yzw) | 21:01 | 2026-02~ | 310,836 | 7,218 | 2.32% | 0.96 | RYD |
| 19 | [Why The Richest Company in History Went Bankrupt](https://www.youtube.com/watch?v=GpapVTX1umU) | 15:38 | 2026-06-24 | 201,831 | 5,724 | 2.84% | 0.76 | RSS |
| 20 | [The ENTIRE History of Elizabeth Holmes Explained Like You're 5](https://www.youtube.com/watch?v=p9x9s_-IOOM) | 16:21 | 2025-11~ | 905,342 | 9,966 | 1.1% | 1.33 | RYD |
| 21 | [Margin Call Scandal Explained Like You're 5](https://www.youtube.com/watch?v=adpt6KW4Jb4) | 13:45 | 2026-04~ | 528,543 | 7,788 | 1.47% | 1.04 | RYD |
| 22 | [The Rise of Paypal Explained Like You're 5](https://www.youtube.com/watch?v=EedHneVKmpo) | 12:36 | 2025-11~ | 134,243 | 3,840 | 2.86% | 0.51 | RYD |
| 23 | [TSMC Explained Like You're 5](https://www.youtube.com/watch?v=aDCKVS8aA8E) | 20:35 | 2026-08-22 | 370,239 | 5,910 | 1.6% | 0.79 | RSS |
| 24 | [5000 Years of Gold Explained in 16 Minutes](https://www.youtube.com/watch?v=GPgaG9D7S6I) | 16:06 | 2026-02~ | 177,620 | 4,397 | 2.48% | 0.59 | RYD |
| 25 | [How One Man Pulled Off a $65 Billion Scam](https://www.youtube.com/watch?v=xhbukTTkwJY) | 11:34 | 2025-11~ | 252,796 | 5,348 | 2.12% | 0.71 | RYD |
| 26 | [Ozempic Explained Like You're 5](https://www.youtube.com/watch?v=ybP8g6xzCIs) | 12:41 | 2026-08-01 | 159,513 | 4,088 | 2.56% | 0.54 | RSS |
| 27 | [The Greatest Slave System Ever Created](https://www.youtube.com/watch?v=GdpGd0U2wmo) | 12:18 | 2026-06-28 | 72,670 | 2,446 | 3.37% | 0.33 | RSS |
| 28 | [How Jeffrey Epstein Actually Got So Rich,](https://www.youtube.com/watch?v=AKrjI9m6fpk) | 12:33 | 2026-07-21 | 82,649 | 2,122 | 2.57% | 0.28 | RSS |
| 29 | [BYD: The Copycat That Beat Tesla (And How It Did It)](https://www.youtube.com/watch?v=ggFpIjvXQi4) | 16:41 | 2026-09-09 | 304,185 | 4,466 | 1.47% | 0.6 | RSS |
| 30 | [Bitcoin Explained Like You're 5](https://www.youtube.com/watch?v=_pUOpoihjA4) | 10:15 | 2025-11~ | 159,595 | 3,653 | 2.29% | 0.49 | RYD |
| 31 | [J.P. Morgan: The Most Powerful Man in America](https://www.youtube.com/watch?v=tsZIyy18qIo) | 16:40 | 2026-11-10 | 411,728 | 4,446 | 1.08% | 0.59 | RSS |
| 32 | [Every Financial Crisis Explained in 10 Minutes](https://www.youtube.com/watch?v=KHLY6SyLvgQ) | 10:54 | 2025-11~ | 80,948 | 1,903 | 2.35% | 0.25 | RYD |
| 33 | [The Economic Secret of WW2](https://www.youtube.com/watch?v=A_wtItX_kIE) | 13:22 | 2026-05-23 | 71,914 | 1,778 | 2.47% | 0.24 | RSS |
| 34 | [The First Big Victim of the AI Bubble](https://www.youtube.com/watch?v=6X0ib0Jt9cs) | 18:45 | 2026-10-06 | 477,224 | 3,718 | 0.78% | 0.5 | RSS |
| 35 | [How Steve Jobs Actually Built Apple](https://www.youtube.com/watch?v=rkJ9v-GJzLw) | 21:25 | 2026-10-31 | 264,753 | 3,701 | 1.4% | 0.49 | RSS |
| 36 | [The Biggest Hack in History Just Happened](https://www.youtube.com/watch?v=wu398eFxGMg) | 14:51 | 2026-11-21 | 84,594 | 1,170 | 1.38% | 0.16 | RSS |

Catatan: video #36 baru berumur 5 hari dan #16/#31 di bawah 3 minggu, sehingga angkanya belum matang. Konsistensi engagement: 18 dari 36 video di atas median likes, dan rasio likes/views stabil di sekitar 1,5–2,5% (IQR). Dengan kata lain, kualitas produksi menjaga engagement per penonton cukup konsisten. Yang membedakan hit adalah *reach* (topik + packaging).

### 2.3 Pemilihan video utama
| Kriteria | Pemenang | Angka |
|---|---|---|
| Likes absolut | **#1 Wolf of Wall Street** | 80.296 (10,7× median) |
| Views | **#1 Wolf of Wall Street** | 4.311.233 |
| Rasio likes/views tertinggi | #27 The Greatest Slave System | 3,37% (2.446 likes, 72.670 views) |
| Skor komposit | **#1 Wolf of Wall Street** | 30,6 |

**Video yang dipilih: [The Wolf of Wall Street Scam Explained Like You're 5](https://www.youtube.com/watch?v=HawmGu7oNrc)** (16:33).

**Alasan:**
1. Video ini juara mutlak likes dan views dengan margin besar (likes 1,6× video #2).
2. Rasio likes/views-nya 1,86%, dekat median channel (1,99%). Artinya video ini *tidak* bergantung pada audiens inti yang sempit; kualitasnya memuaskan audiens luas pada skala jutaan.
3. Video dengan rasio tertinggi (#27, 3,37%) punya basis views 59× lebih kecil. Rasio tinggi pada views kecil umumnya mencerminkan subscriber setia, bukan daya tarik visual yang teruji di audiens umum. Video ini tetap dipakai sebagai pembanding, dan frame-nya termasuk dalam sampel gaya.
4. Video ini mewakili format paling sukses (ELI5 + skandal keuangan ber-pop-culture).

---

## 3. Sistem visual channel (dari 144 frame)

### 3.1 Kategori dan art direction
- **[Teramati]** 2D flat-vector cartoon, karakter-sentris, explainer naratif. Bukan whiteboard murni. Video awal (2025) memang lebih "papan tulis" (latar putih, garis tipis goyah), tapi sejak 2026 semua scene memakai latar penuh berwarna.
- **[Teramati]** Tagline channel "Big finance, drawn small." Konsepnya: hal besar (miliaran dolar, krisis global) digambar kecil, lucu, dan bulat.
- **[Inferensi]** Target: dewasa muda yang ingin memahami ekonomi tanpa jargon. OutlierKit memperkirakan audiens 25–34 tahun, mayoritas laki-laki, dan berbahasa Inggris global.
- **Tone:** satir ringan + drama. Skandal disajikan sebagai cerita moral dengan tokoh protagonis/antagonis yang jelas.

### 3.2 Evolusi gaya [Teramati + terukur]
| Era | Ciri | Data terukur (median per frame) |
|---|---|---|
| ≤ Nov 2025 (video awal, mis. #32, #25, #30, #22) | Latar putih/kosong, garis lebih tipis dan bergetar (hand-drawn), props sederhana | piksel putih-netral 16,3%, saturasi 0,32, luminance 0,56 |
| H1 2026 | Latar penuh, cel-shading kepala, cahaya atmosferik | putih 9,9%, saturasi 0,30, luminance 0,49 |
| H2 2026 | Latar lebih gelap/sinematik, depth blur, glow, lighting berwarna | putih 5,4%, saturasi 0,26, luminance 0,44 |

Arahnya: dari "doodle explainer" menuju "sinematik flat cartoon". Ketebalan outline tetap stabil, sekitar 5–6 px di 720p (≈ 8–9 px di 1080p). Frame berlatar putih dominan hanya ada di 6/108 frame isi, hampir semua dari video lama.

### 3.3 Desain karakter [Teramati]
- **Kepala:** lingkaran besar dan bulat sempurna di semua sampel. Mata berupa dua oval vertikal hitam, sering dengan titik highlight putih (terutama saat kaget: mata "sparkle", Wolf ≈4:08). Alis pendek mengambang. Mulut kecil; saat terbuka berisi merah tua + gigi atas putih; saat berteriak, bentuk kotak/trapesium (Great Depression ≈8:14).
- **Badan:** bentuk bean/telur yang sekaligus pakaian (jas, kemeja, seragam, gaun). Detail pakaian minimal: kerah, dasi, lapel, kancing, logo kecil. Tidak ada leher.
- **Tungkai:** garis tunggal hitam. Lengan sering melengkung panjang seperti selang (Wolf ≈4:08: lengan melingkar ke belakang tumpukan uang). Tangan umumnya tidak digambar; kadang oval putih (Great Depression ≈8:14). Tangan detail dengan jari dan jam tangan **hanya di thumbnail**.
- **Kelas warna:** tokoh bernama punya warna kulit (`#F0D2AF` pada Wolf) dan rambut khas. Figuran berkepala putih (`#FDFDFD`). Kerumunan didesaturasi abu (thumbnail Wolf: protagonis berwarna di tengah, sekelilingnya kerumunan abu).
- **Shading:** satu bayangan bulan sabit keras di sisi kepala yang jauh dari cahaya. Rambut dua tone + band highlight. Dalam cahaya jendela biru, sisi kepala mendapat rim biru (Palantir ≈7:40).
- **Identitas lewat props:** kacamata, kumis, topi koboi/bowler, sorban, topi Uncle Sam, seragam militer, rompi safety. Ini memungkinkan puluhan tokoh sejarah tetap dalam satu sistem bentuk.
- **[Teramati] Maskot reaksi lintas video:** pria berkacamata bulat, dasi kupu-kupu merah, jas cokelat, ekspresi panik/bingung. Ia muncul di pojok thumbnail (#2, #3, #11, #13, #21, #29, #30, #31, #35). → **Jangan disalin.** Prinsipnya boleh dipakai: satu maskot reaksi milik sendiri yang konsisten sebagai *brand anchor*.

### 3.4 Lingkungan dan latar [Teramati]
- Latar dilukis flat-vector dengan outline, umumnya **satu hue dominan per lokasi**: kantor biru, panggung merah tua, perbendaharaan kuning-emas, malam kota biru navy dengan jendela kuning, gurun pasir, hutan hijau.
- Latar paling sederhana: gradien atau 3 band nilai (Wolf ≈4:08: `#479ABF` → `#5FB0CB` → `#85C2D4`, horizon melengkung).
- Depth: foreground framing (meja di bawah frame, kepala besar di depan), blur latar, kerumunan desaturasi.
- Props informatif: monitor grafik turun merah, tumpukan uang berlabel angka ("$26 billion → $44 billion"), karung `$`, peta dengan negara disorot, papan konspirasi dengan benang merah.

### 3.5 Tipografi layar [Teramati]
- **Dialog:** teks italic bergaya tulisan tangan, putih dengan stroke/bayangan gelap, diletakkan di atas atau di samping pembicara dengan **tick pendek** yang menunjuk ke kepala ("But what if we-", "So…", "Actually,"). Kadang memakai balon kata putih (bulat atau kotak).
- **Label:** huruf kapital tulisan tangan pada props ("(WORST) ASSETS", "U.S. MILITARY BASE", "LIMITED ACCESS").
- **Time card:** italic putih di pojok kanan bawah ("30 minutes later...").
- **Nama tokoh:** italic dengan panah melengkung ke tokoh ("Xi Zhongxu ↗", "Huang Le 黄乐").
- **Thumbnail:** sans-serif sangat tebal, putih, kapital, dengan bayangan; atau banner kuning `#FAB71D` dengan teks hitam (Wolf).

### 3.6 Lighting dan warna [Teramati + terukur]
- Saturasi median frame 0,29 dan luminance median 0,50. Kesannya cerah tapi tidak neon.
- Palet video utama per scene (k-means, persentase piksel):
  - ≈4:08 "meja penuh uang": biru `#479ABF` 27%, `#5FB0CA` 26%, `#84C2D3` 16%, cokelat meja `#875437` 14%, outline `#1C261D` 10%, kulit `#F0D2AF` 4%.
  - ≈8:16 "diusir satpam": abu `#C7C7C5` 19%, biru dinding `#94C4E4` 17%, cokelat `#4B3934` 14%, abu `#757373` 14%, outline `#171415` 9%, putih `#FDFDFD` 7%.
  - ≈12:25 "panggung": merah tua `#561C1B` 28%, `#450E0D` 22%, `#6C3E3D` 13%, gelap `#18131C` 13%, kulit `#EDCAA5` 5%.
  - Thumbnail: abu gelap `#191A1B`/`#3B3B38`/`#535455` 57% total, kuning `#FAB71D` 12%.
- Cahaya atmosferik: sorotan spotlight berbentuk kerucut transparan (panggung), sorotan jendela diagonal (NVIDIA ≈7:15, Palantir), glow lilin/objek (2008 ≈3:21, Ozempic), cahaya berwarna pada wajah (Petrodollar ≈8:30: wajah hijau di bawah lampu hijau).
- Top-light pada props: sisi atas meja lebih terang (`#91583B`) dibanding sisi depan (`#73412A`).

### 3.7 Efek visual [Teramati]
Confetti warna-warni (kemenangan), hujan uang/koin, asap, api, petir, retakan lantai/dinding (impact), garis kecepatan dan **multiples** pada kaki (Wolf ≈8:16), motion blur pada tubuh jatuh (Great Depression ≈8:14), tetes keringat, tanda `!!` dan `?!`, stempel teks miring ("STRIPPED OF POWER"), label "SELL" beterbangan.

### 3.8 Sistem thumbnail [Teramati]
Thumbnail memakai *render* lebih detail dan dramatis daripada isi video: lighting volumetrik, glow, tekstur. Komposisi: 1 wajah protagonis dengan emosi kuat (sering seringai jahat atau tatapan tajam) di tengah atau sepertiga, judul 1–3 kata raksasa di atas, panah grafik merah/hijau, logo perusahaan, papan konspirasi, dan maskot reaksi di pojok. Thumbnail adalah karya terpisah, bukan frame dari video.

---

## 4. Katalog tipe shot (dari 108 frame isi)

| Tipe shot | Contoh (video, ≈posisi) | Fungsi naratif |
|---|---|---|
| Medium frontal 1 tokoh di balik props | Wolf ≈4:08 (meja penuh uang) | memperkenalkan status/kekayaan |
| Lineup 3–5 tokoh menghadap kamera | NVIDIA ≈7:15, Theranos ≈4:05, Epstein ≈6:16, Singapore ≈12:07 | "dewan", "tim", "saksi" |
| Medium 2–3 tokoh + teks dialog | Palantir ≈7:40, Elon ≈4:47 | dialog/plot |
| Over-the-shoulder dengan kepala foreground besar | Wolf ≈8:16, Margin Call ≈10:19 | penonton ikut berada di ruangan |
| Close-up wajah / ECU gigi | VOC ≈3:55 (tiga mulut gigi kertak), Petrodollar ≈2:50 | emosi ekstrem |
| Wide establishing kendaraan/lokasi | Iran War ≈3:03 & ≈9:08, Singapore ≈8:05 | konteks geografi/militer |
| Split-screen 2–3 panel / diagonal | Singapore ≈4:02, Anthropic ≈4:28 & ≈8:56, Steve Jobs ≈10:43, Ozempic ≈9:31 | perbandingan, telepon, paralel |
| Infographic diegetik (uang berlabel, grafik, peta) | NVIDIA Scandal ≈3:37, BYD ≈8:20, Margin Call ≈6:52 | angka dan mekanisme |
| Metafora panggung / selebrasi | Wolf ≈12:25, Amazon ≈10:06 | kemenangan tokoh |
| Wide aksi multi-karakter | Wolf ≈8:16 (satpam mengusir) | konflik |

---

## 5. TAHAP 3: Analisis mendalam video utama

**The Wolf of Wall Street Scam Explained Like You're 5**. Durasi 16:33 (993 dtk). Bahan: 3 frame isi + 1 thumbnail.

### 5.1 Overall
- **Gaya:** era transisi akhir 2025. Garis tegas, latar penuh, cel-shading kepala.
- **Struktur cerita [Inferensi dari 3 titik sampel]:** ≈25% kekayaan menumpuk (tokoh shock di balik uang), ≈50% konflik/penegakan (karyawan diseret satpam), ≈75% puncak glamor (tokoh di panggung, spotlight, confetti). Ini konsisten dengan formula "setup → loophole → scale-up → konsekuensi" yang dilaporkan OutlierKit. Urutan bab sesungguhnya **tidak dapat diverifikasi**.

### 5.2 Hook
- **0–5 detik: [Tidak dapat diverifikasi]** (lihat §1.3).
- **Packaging hook [Teramati]:** judul memakai pop-culture yang sangat dikenal ("The Wolf of Wall Street") + janji penyederhanaan ("Explained Like You're 5"). Thumbnail menampilkan protagonis berwarna yang tenang di tengah pesta kerumunan abu, dengan confetti, alat musik tiup, dan lantai penuh uang. Ada kontras emosional: ekspresi datar-percaya-diri di tengah kekacauan. Banner kuning berisi judul film. **Curiosity gap:** "bagaimana sebenarnya penipuannya bekerja?"
- Standar hook untuk produksi baru ada di `workflows/pre_production.md` §3 ([Rekomendasi]).

### 5.3 Breakdown per frame sampel
| Elemen | ≈4:08 (25%) | ≈8:16 (50%) | ≈12:25 (75%) | Thumbnail |
|---|---|---|---|---|
| Scene | Tokoh di balik meja penuh tumpukan uang dan koin | Kantor: dua karyawan diseret dua satpam ke pintu kaca, rekan kerja menonton | Tokoh di depan tirai merah panggung | Pesta di ruang trading |
| Karakter | Protagonis (kulit, rambut hitam licin) | 2 karyawan + 2 satpam + 4–5 rekan; kepala putih, 1 rambut pirang, 1 wanita berbaju merah | Protagonis berjas navy, dasi abu | Protagonis + ±15 figuran |
| Posisi | Tengah, frontal, badan tertutup meja | Aksi di sepertiga kanan, reaksi di kiri; foreground kepala besar kanan bawah | Tengah, frontal | Tengah, kerumunan simetris |
| Aksi | Diam di balik uang (lengan melingkar) | Diseret keluar, kaki berlari | Melambai tangan kanan | Tangan terlipat, jam emas |
| Ekspresi | Kaget: mata sparkle, mulut "O" lebar, alis naik | Karyawan: mata `> <` meringis; wanita: marah; penonton: kaget | Senyum puas, alis tenang | Datar-percaya-diri vs figuran tertawa/marah |
| Gerak tubuh | Hold (tidak terlihat jejak gerak) | **Multiples kaki** (3–4 kaki per tokoh) + speed lines = smear lari | Lengan terangkat (arc ayunan) | — |
| Kamera | Medium, eye-level, statis | Medium-wide, sedikit high-angle, over-the-shoulder | Medium, eye-level | Medium |
| Komposisi | Simetris, uang membentuk piramida di sepertiga bawah | Diagonal pintu → kanan; foreground framing | Simetris; sorotan diagonal membingkai | Simetris, banner di atas |
| Latar | 3 band biru, horizon melengkung | Dinding biru muda, pintu kaca, meja abu | Tirai merah berlipat dengan highlight | Ruang gelap, lampu neon, lantai uang |
| Lighting | Flat + bayangan sabit kanan kepala | Ambient datar, bayangan elips di lantai | Dua kerucut spotlight transparan | Spotlight dari atas, kerumunan meredup ke tepi |
| Warna | Biru dingin vs cokelat hangat + hijau uang | Abu netral + aksen merah (baju) dan biru | Merah tua monokrom + confetti multi-warna | Abu + kuning + aksen warna kulit |
| Prinsip animasi | Exaggeration (wajah), staging | Smear/multiples (timing cepat), staging aksi vs reaksi, overlapping (dasi) | Arcs (lambaian), secondary (confetti) | Appeal, staging |
| Transisi | [Tidak dapat diverifikasi] | [Tidak dapat diverifikasi] | [Tidak dapat diverifikasi] | — |
| Sound | [Tidak dapat diverifikasi] | [Tidak dapat diverifikasi] | [Tidak dapat diverifikasi] | — |
| Kualitas | Bersih | Lihat QC #2 | Bersih | Lihat QC #7 |

### 5.4 Motion [Inferensi]
- Bentuk karakter sangat konsisten antar-frame dan antar-video (lingkaran sempurna, badan bean identik), dan tungkainya berupa garis yang menekuk mulus. Ini konsisten dengan **rig cut-out + tungkai rubber-hose** (mis. Moho, Harmony, atau AE + Rubberhose/Duik).
- Aksi cepat diselesaikan dengan **multiples/smear yang digambar** (Wolf ≈8:16) atau **motion blur komposit** (Great Depression ≈8:14). Artinya ada kombinasi drawing manual dan efek software.
- Teknik pastinya, fps, dan kurva easing **tidak dapat dipastikan** dari gambar diam.

---

## 6. Bug detection dan quality assurance (temuan nyata)

Kategori: **A** = actual visual error, **B** = minor imperfection, **C** = stylistic choice, **D** = potensi masalah teknis yang perlu dicek pada video penuh.

| # | Video ≈posisi | Temuan | Kategori | Keparahan | Catatan |
|---|---|---|---|---|---|
| 1 | Great Depression ≈8:14 | Tokoh yang jatuh dengan motion blur berat menunjukkan **blok/pixelasi** pada area wajah | D | Rendah | Bisa artefak kompresi YouTube pada blur besar. Pelajaran: batasi blur pada wajah dan render bitrate tinggi. |
| 2 | Wolf ≈8:16 | Kaki ganda (multiples) dan garis kecepatan | C | — | Smear disengaja, bukan bug. |
| 3 | BYD ≈4:10, J.P. Morgan ≈4:10, First Victim of AI Bubble ≈4:41 | Frame foto-realistis AI (sepasang muda di motor, UI "Generate images and videos") | C (bisnis) | Sedang (kontinuitas gaya) | Segmen sponsor. Pelajaran: bungkus dengan bumper agar perubahan gaya terasa disengaja. |
| 4 | NVIDIA ≈3:37 | Label "Cu"/"Ch" terpotong di tepi bawah frame | D | Rendah | Kemungkinan label sedang animasi masuk. Perlu cek video penuh. |
| 5 | Epstein ≈9:25 | Panel tri-split dengan teks dokumen terpotong ("CUTION", "NITY") | D | Rendah | Kemungkinan frame di tengah transisi geser. |
| 6 | Lintas channel | Video lama berlatar putih dan bergaris tipis vs video baru sinematik | C/B | Rendah | Evolusi gaya. Untuk produksi baru, kunci satu era gaya per seri. |
| 7 | Wolf thumbnail vs isi | Thumbnail: tangan berjari + jam emas, shading lebih kaya. Isi video: lengan tanpa tangan | C | — | Disengaja (thumbnail "premium render"). Jaga agar siluet dan warna tokoh tetap sama. |
| 8 | Wolf ≈4:08 | Lengan berupa loop panjang yang hilang di balik uang | C | — | Gaya rubber-hose. Layering-nya benar. |
| 9 | Palantir ≈7:40 | Lengan tokoh kanan melintas di belakang tokoh tengah ke bahu | — | — | Layering benar. **Bukan bug.** |

Dalam 108 frame sampel **tidak ditemukan** error kategori A yang pasti: tidak ada morphing tak disengaja, proporsi yang berubah, objek melayang, atau clipping yang jelas. Dengan sampel sejarang ini, hal itu **tidak membuktikan** video bebas bug, hanya bahwa standar konsistensi model sangat tinggi pada titik-titik yang terlihat.

---

## 7. Pelajaran yang diterjemahkan ke SOP
1. Konsistensi bentuk dibuat dengan *sistem* (lingkaran + bean + garis), bukan dengan menggambar ulang. → Gunakan rig dan library bentuk.
2. Warna dipakai untuk mengarahkan perhatian: hanya tokoh fokus yang "berwarna".
3. Satu hue per lokasi memudahkan orientasi di video 15 menit dengan puluhan lokasi.
4. Teks dialog tulisan tangan menggantikan sebagian lip-sync, sehingga murah diproduksi tapi tetap ekspresif.
5. Metafora literal dan props berlabel angka membuat konsep keuangan "terlihat".
6. Thumbnail adalah produk terpisah dengan render premium, tapi tetap memakai model karakter yang sama.
7. Variasi shot terbatas tapi konsisten (lineup, OTS, split, wide). Kosakata kecil ini membangun identitas.
