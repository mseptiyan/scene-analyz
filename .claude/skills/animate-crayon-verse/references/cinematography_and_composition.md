# Cinematography & Composition: Crayon Verse

**Sumber industri:** Joseph V. Mascelli, *The Five C's of Cinematography* (camera angles, continuity, cutting, close-ups, composition); Bruce Block, *The Visual Story*; StudioBinder (shot sizes, 180° rule); Toon Boom/Tahoma2D (layout: komposisi scene, sudut kamera, dan staging karakter disusun dari storyboard). Katalog shot channel referensi: `crayon_capital_analysis.md` §4.

---

## 1. Shot sizes (definisi untuk karakter kepala-besar)

Karena kepala ≈ 30% tinggi tubuh, definisi shot disesuaikan:
| Kode | Nama | Framing | Penggunaan |
|---|---|---|---|
| EWS | Extreme wide | Lokasi penuh, tokoh < 10% tinggi frame | Peta, kota, medan perang, pembuka bab |
| WS | Wide | Tokoh penuh dengan ruang di sekitar | Aksi multi-karakter, kendaraan |
| MWS | Medium wide | Tokoh penuh, frame ketat | Jalan, interaksi 2–4 orang |
| MS | Medium | Kepala + badan sampai pinggang/meja | **Default dialog dan lineup** |
| MCU | Medium close-up | Kepala + bahu | Reaksi, dialog penting |
| CU | Close-up | Kepala memenuhi 60–80% tinggi | Emosi kuat, wajah tokoh saat diperkenalkan |
| ECU | Extreme close-up | Mata atau mulut saja | Shock, ketakutan (gigi kertak), detail objek |
| OTS | Over-the-shoulder | Kepala/bahu foreground besar (sering terpotong) | Menempatkan penonton di ruangan |
| INSERT | Insert props | Objek memenuhi frame | Dokumen, uang berlabel, layar grafik |

**Ukuran kepala per shot size (Ø kepala di kanvas 1920×1080).** Ini acuan konsistensi lintas shot. [Teramati: estimasi dari frame sampel 720p dikali 1,5. Mis. Wolf ≈4:08 MS/MCU Ø ≈ 450 px; NVIDIA ≈7:15 lineup MS ≈ 300 px; Wolf ≈8:16 WS ≈ 150 px.]
| Shot size | Ø kepala (px @1080p) |
|---|---|
| WS (tokoh penuh, ada ruang) | 100–160 |
| MWS (tokoh penuh, ketat) | 160–240 |
| MS lineup 3–5 tokoh | 260–340 |
| MS/MCU 1–3 tokoh | 400–500 |
| CU | 650–900 |
| ECU | kepala melebihi frame |

**Rasio penggunaan target per video [Rekomendasi]:** MS 35% · MCU/CU 20% · WS/MWS 15% · INSERT/infographic 15% · OTS 5% · EWS 5% · ECU 3% · split-screen 2–5%.

## 2. Sudut kamera
- **Default eye-level frontal** [Teramati]. Karakter menghadap kamera, termasuk saat "berbicara" satu sama lain (konvensi explainer).
- **Low angle** (kamera rendah): tokoh berkuasa, tycoon, diktator.
- **High angle**: korban, kerumunan kecil, karyawan yang dipecat [Teramati: Wolf ≈8:16 sedikit high-angle].
- **Dutch tilt (5–12°)**: kekacauan, krisis. Gunakan jarang.
- **Top-down**: meja/peta/infographic.

## 3. Gerak kamera (semua dengan easing)
| Gerak | Parameter | Motivasi |
|---|---|---|
| Push-in | skala 100→105–110%, 3–6 detik | penekanan, realisasi |
| Pull-out / reveal | 110→100% atau lebih lebar | mengungkap skala ("dan ternyata...") |
| Pan horizontal | 1 layar dalam 2–4 detik | ikut tokoh/mengungkap lineup |
| Tilt | vertikal | gedung tinggi, grafik naik |
| Truck/parallax | 3–5 layer kedalaman, FG 1,5× BG | lokasi establishing |
| Shake | 4–8 frame, 6–12 px, decay | impact, ledakan, crash |
| Whip pan | 4–6 frame + motion blur | transisi energetik |
| Zoom ke objek (transisi) | 8–16 frame | masuk ke "dunia" dalam objek (layar, peta) |

Aturan: maksimal **1 gerak kamera bermotivasi per shot**. Shot tanpa motivasi gerak tetap *locked-off*. Ini sesuai dengan referensi yang didominasi framing statis [Inferensi dari frame sampel].

## 4. Komposisi
1. **Satu titik fokus per frame.** Gunakan kontras warna (berwarna vs abu), nilai (terang vs gelap), posisi, dan ukuran.
2. **Tengah atau sepertiga.** Tokoh tunggal yang diperkenalkan berada di tengah, simetris [Teramati: Wolf]. Dialog 2 tokoh di garis sepertiga kiri/kanan.
3. **Lineup:** 3–5 tokoh sejajar, kepala di garis horizontal yang sama (variasi tinggi ±10% untuk ritme), tokoh terpenting di tengah atau diberi warna [Teramati].
4. **Headroom dan ruang teks:** sisakan 15–20% tinggi frame di atas kepala pembicara untuk teks dialog.
5. **Foreground framing:** meja di bawah frame, kepala buram, pagar, untuk depth [Teramati].
6. **Negative space:** isi dengan hue latar yang bersih. Jangan memenuhi latar dengan detail di belakang wajah.
7. **Safe areas:** title safe 90%, action safe 93%. Hindari teks di 10% bawah kanan (area kontrol/progress bar YouTube).
8. **Rule of odds:** kelompok 3 atau 5 tokoh terasa lebih dinamis dari 2 atau 4.

## 5. Split-screen dan panel [Teramati]
- 2 panel vertikal (perbandingan A vs B, "dulu vs sekarang").
- 3 panel (telepon berantai, banyak perspektif).
- **Diagonal split** (energi, kontras dua kubu).
- Garis pemisah: putih atau outline tebal 8–12 px. Panel masuk dengan wipe atau slide 8–12 frame.

## 6. Kontinuitas
- **Aturan 180°:** dalam satu adegan dialog, tokoh A selalu di kiri dan B di kanan. Ganti sumbu hanya dengan shot netral (frontal/lineup) atau gerak kamera yang terlihat.
- **Arah gerak (screen direction):** perjalanan/progres = kiri → kanan; kemunduran/kembali = kanan → kiri; grafik naik = kiri bawah → kanan atas.
- **Eyeline match:** tokoh yang melihat sesuatu off-screen harus menatap ke arah tempat objek muncul di shot berikutnya.
- **Kontinuitas props dan kostum:** daftar props per adegan di shot list.

## 7. Infographic diegetik (gaya khas)
Angka dan data **dimasukkan ke dunia cerita**, bukan ditempel sebagai overlay korporat [Teramati]:
- Tumpukan uang dengan papan angka tulisan tangan (sebelum → sesudah + panah).
- Monitor/TV di dinding dengan grafik turun merah atau naik hijau.
- Peta dengan negara disorot warna aksen dan tokoh berdiri di depannya.
- Papan konspirasi (foto, benang merah) untuk jaringan relasi.
- Karung `$`, gelembung (bubble) yang pecah, rantai, timbangan.

## 8. Adaptasi vertikal 9:16 (Shorts/Reels) [Rekomendasi]
Channel referensi 100% long-form. Bila membuat versi vertikal 1080×1920:
- Ganti lineup horizontal menjadi tumpukan vertikal (maks 2–3 tokoh) atau potong ke MCU.
- Ø kepala MCU ≈ 500–650 px. Teks dialog di sepertiga atas, sisakan 20% bawah untuk UI platform.
- Split-screen menjadi atas/bawah, bukan kiri/kanan.
- Hook di frame pertama (tanpa build-up). Shot 1–2 detik.

## 9. Template shot list (dipakai di `workflows/pre_production.md`)
| # | Shot ID | TC in | Dur | Size/Angle | Kamera | Karakter & aksi | Ekspresi | Teks layar | SFX/Musik | Transisi out |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SQ010_SH0010 | 00:00:00:00 | 2s12f | CU eye-level | push-in 100→106 | Tycoon menyeringai, mata menyipit | licik | — | bass hit | hard cut |
