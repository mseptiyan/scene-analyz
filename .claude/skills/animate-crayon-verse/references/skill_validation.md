# Validasi Skill: Uji Pakai pada Proyek Fiktif

**Tanggal:** 2026-11-26
**Kasus uji:** video baru *"Tulip Mania Explained Like You're 5"*. Topik ini orisinal dan tidak ada di katalog channel referensi.
**Metode:** setiap kemampuan diuji dengan benar-benar menghasilkan deliverable **hanya** dari isi skill. Bila skill tidak memberi cukup panduan, itu dicatat sebagai kekurangan dan diperbaiki.

---

## Matriks hasil

| # | Kemampuan | Sumber di skill | Hasil awal | Kekurangan | Perbaikan | Status akhir |
|---|---|---|---|---|---|---|
| 1 | Konsep animasi baru | `pre_production.md` §1–3, §7.1 | Lulus | — | — | ✅ |
| 2 | Character design brief | `character_design_standards.md` §9 | Lulus | — | — | ✅ |
| 3 | Storyboard | `pre_production.md` §6, §7.2 | Lulus | — | — | ✅ |
| 4 | Shot list | `pre_production.md` §7.3, `cinematography_and_composition.md` | Sebagian | Rujukan § template shot list salah setelah penomoran berubah | Rujukan diperbaiki ke §9 | ✅ |
| 5 | Animation direction | `character_animation_standards.md` §8 | Lulus | — | — | ✅ |
| 6 | Camera movement | `cinematography_and_composition.md` §3 | Lulus | Tidak ada panduan format vertikal | Ditambah §8 adaptasi 9:16 | ✅ |
| 7 | Timing & spacing | `animation_fundamentals.md` §6, §9 | **Gagal sebagian** | Timing ada, tapi tidak ada cara menulis *spacing chart* | Ditambah notasi spacing chart + aturan breakdown | ✅ |
| 8 | Konsistensi karakter | `character_consistency_checklist.md` | **Gagal sebagian** | Toleransi ±3% tidak punya ukuran acuan per shot size | Ditambah tabel Ø kepala per shot size (dari frame teramati) | ✅ |
| 9 | Identifikasi animation bugs | `quality_control_and_bug_detection.md` | Lulus | — | — | ✅ |
| 10 | QC sebelum final render | `animation_quality_assurance.md`, `final_render_checklist.md` | Lulus | Aturan exaggeration untuk topik tragis hanya ada di file referensi, tidak terlihat di SKILL.md | Ditambahkan ke `SKILL.md` §5 | ✅ |

---

## Bukti uji (output yang dihasilkan)

### T1. Konsep (format §7.1)
```markdown
# Tulip Mania Explained Like You're 5
- **Logline:** Bagaimana satu bunga tulip pernah lebih mahal dari sebuah rumah, dan kenapa semua orang ikut gila.
- **Format judul:** "Tulip Mania Explained Like You're 5" (alt: "The First Bubble in History", "How a Flower Crashed an Economy")
- **Audiens & janji:** penonton akan memahami cara kerja gelembung spekulasi lewat tulip.
- **Durasi target:** 12 menit (±1.700 kata VO)
- **Struktur:** Hook (tulip = harga rumah) → Setup (Belanda abad 17, tulip langka) → Mekanisme (kontrak berjangka di kedai minum) → Skala (harga ×20 dalam bulan) → Konsekuensi (Februari 1637: pembeli menghilang) → Pelajaran (harga ≠ nilai)
- **Metafora kunci:** 1) tulip sebagai kartu koleksi langka 2) kontrak = janji di serbet kedai 3) gelembung sabun yang membesar
- **Tokoh:** [hero] Pieter, pedagang tulip (orisinal); [antagonis] tidak ada, "keserakahan kerumunan"; [figuran] pembeli kedai; [maskot] milik channel sendiri
- **Lokasi & hue:** pasar (padang/sejarah krem), kedai (oranye hangat), rumah mewah (emas), crash (abu krisis)
- **Konsep thumbnail:** wajah Pieter shock memegang 1 tulip bercahaya, teks "1 FLOWER = 1 HOUSE", grafik merah jatuh
- **Momen hero:** 1) hook tulip vs rumah 2) reveal harga tertinggi 3) crash Februari 1637
- **Risiko:** angka sejarah diperdebatkan → sebut rentang dan sumber
```
→ Semua kolom terisi dari panduan skill. Uji topik §1 lulus 5/5.

### T2. Character brief (format §9)
```markdown
## Character Brief: PIETER
- Peran naratif: protagonis-korban; mewakili "orang biasa yang ikut arus"
- Kelas warna: hero
- Siluet kepala: topi bertepi lebar abad 17 (orisinal: pinggiran bergelombang)
- Props identitas: kerah putih bundar besar + 1 tulip merah di saku
- Palet: kulit #F2D3B0 (shade #D9AE8A), rambut #6B4A2E/#4E341F/#8A6544, mantel #2F3B57 (shade #232C42), aksen tulip #D9363E
- Proporsi: tinggi 3,2 × Ø kepala; badan lebar 1,0 × Ø
- Kepribadian visual: optimis, gugup, mudah terbawa → bahu naik saat senang, keringat saat cemas
- Ekspresi khas: mata sparkle (melihat harga), gugup + keringat (crash), senyum lebar (puncak)
- Gaya gerak: cepat dan bersemangat, sering merapikan topi (secondary action khas)
- Do/Don't: Do kerah selalu terlihat; Don't beri tangan berjari di video
- Model sheet: turnaround ✓ ekspresi ✓ mouth chart ✓ pose ✓
```

### T3. Storyboard (format §7.2, hook)
```markdown
**SQ010_SH0010** | CU eye-level | 2s
Pieter memegang 1 tulip merah bercahaya, mata sparkle. Teks pop: "1 TULIP". SFX: shimmer. Cut.
**SQ010_SH0020** | MS frontal | 2s
Split-screen vertikal: kiri tulip di pot, kanan rumah kanal Belanda. Tanda "=" pop di tengah. SFX: stamp. Cut.
**SQ010_SH0030** | MS lineup | 3s
4 figuran kepala putih menatap tulip dengan mulut "O", kerumunan abu di belakang. Pieter di tengah berwarna. Push-in 100→105%.
**SQ010_SH0040** | WS | 3s
Gelembung sabun besar berisi tulip melayang di atas kota (metafora). Panah grafik naik hijau. Teks: "How did a flower become a bubble?"
```

### T4. Shot list (0–15 detik)
| # | Shot ID | TC in | Dur | Size/Angle | Kamera | Karakter & aksi | Ekspresi | Teks layar | SFX/Musik | Transisi out |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SQ010_SH0010 | 00:00:00:00 | 2s00f | CU eye-level | locked | Pieter mengangkat tulip (arc) | sparkle | "1 TULIP" | shimmer | hard cut |
| 2 | SQ010_SH0020 | 00:00:02:00 | 2s00f | MS split | locked | tulip vs rumah pop-in | — | "=" | stamp | hard cut |
| 3 | SQ010_SH0030 | 00:00:04:00 | 3s00f | MS lineup | push 100→105 | figuran menoleh serempak (offset 2f) | kaget "O" | — | crowd gasp | hard cut |
| 4 | SQ010_SH0040 | 00:00:07:00 | 3s00f | WS | pull-out 110→100 | gelembung melayang | — | pertanyaan hook | music swell | match cut (gelembung → mata Pieter) |
| 5 | SQ010_SH0050 | 00:00:10:00 | 2s12f | ECU mata | locked | refleksi tulip di mata | — | — | heartbeat | hard cut |
| 6 | SQ010_SH0060 | 00:00:12:12 | 2s12f | MCU | locked | maskot reaksi menggaruk kepala | bingung | "?!" | boing | dip to title |

→ Variasi shot terpenuhi (tidak ada 3 shot berturut-turut dengan size yang sama). Cut setiap 2–3 detik sesuai standar hook.

### T5. Animation direction
```markdown
### SQ010_SH0030 (00:00:04:00 – 00:00:07:00, 3s)
- VO: "...people were paying the price of a **house**."
- Staging: MS lineup 4 figuran + Pieter tengah (Ø kepala 300 px; tabel MS lineup 260–340)
- Key poses: f0 moving hold; f20 antisipasi (kepala turun 6px); f24 figuran menoleh ke tulip (offset 0/2/4/6 f); f26 ekspresi "O" pada kata "house"
- Secondary: kerumunan abu bergumam (flap mulut acak), Pieter merapikan topi f48
- Timing: akting on twos; push-in kamera on ones
- Kamera: push-in 100→105% f0–72 ease-in-out
- SFX: crowd gasp f26
- QC fokus: kedip tidak sinkron; outline konsisten saat push-in
```

### T6. Camera
Hook memakai 3 gerak bermotivasi (push = tekankan, pull-out = ungkap skala, ECU locked = intensitas). Setiap shot punya ≤ 1 gerak. Lulus SOP-07.

### T7. Timing & spacing (pop-in angka "×20")
```
f1 ─┬────────┬──────┬────┬───┬──┬─ f11   fast-out slow-in, skala 0→110% (f9) → 100% (f11)
    1        3      5    7   9  11
```
Antisipasi tidak dipakai (objek grafis), overshoot 110%, jatuh 1 frame sebelum kata "twenty".

### T8. Konsistensi
Checklist §A diterapkan pada brief Pieter:
- ✅ kepala lingkaran, ✅ tanpa leher, ✅ props identitas (topi + kerah + tulip), ✅ HEX lengkap.
- ⚠️ Temuan: topi lebar bisa menutupi alis pada CU → **keputusan desain:** tepi topi dinaikkan 10% Ø agar alis selalu terlihat (alis adalah pemain utama ekspresi).
→ Checklist menangkap masalah desain sebelum produksi. Lulus.

### T9. Identifikasi bug (skenario uji)
| Skenario | Klasifikasi oleh skill |
|---|---|
| Kaki Pieter meluncur 6 px saat berdiri di f30–40 | A, S3 → error #6 floating/foot slide → kunci kaki |
| 3 kaki terlihat saat lari f12 | C → smear/multiples disengaja |
| Wajah pecah kotak-kotak saat jatuh dengan blur, hanya di versi YouTube | D → error #9 artefak kompresi → kurangi blur wajah, naikkan bitrate |
| Shadow sabit Pieter di kiri, figuran di kanan, dalam scene yang sama | A, S2 → error #11 inconsistent lighting |
| Angka "1673" seharusnya "1637" | A, S1 → error #23 fakta salah → blocker |

### T10. QC sebelum render
Laporan disusun dengan format `animation_quality_assurance.md` §5. Aturan rilis (0 S1, 0 A-S2) diterapkan: skenario T9 → **BLOCKED** sampai temuan S1 (tahun salah) dan S2 (lighting) diperbaiki. Lulus.

---

## Kesimpulan
- 10/10 kemampuan dapat dijalankan dari isi skill saja.
- Ditemukan 5 kekurangan; semuanya sudah diperbaiki di file terkait.
- Batas yang tetap ada (tidak bisa diperbaiki dengan dokumentasi): standar hook, transisi, dan audio berbasis industri karena data video penuh channel referensi tidak dapat diakses (`crayon_capital_analysis.md` §1.3). Bila akses video tersedia di kemudian hari, perbarui §5 analisis tersebut dengan breakdown shot-by-shot nyata.
