# Quality Control & Bug Detection: Crayon Verse

**Sumber industri:** konsep *off-model* dan model sheet (Wikipedia "Model sheet"; Animation Field Notes "Off-model mayhem"), kontrol *boil* dan flicker (Digicel), checklist animasi Keith Lango (arcs, timing, IK pops, hitches), kerangka error animasi pada platform distribusi (Netflix Backlot "Animation Error"), dan QA matrix untuk animasi berbasis AI (dev.to, Magic Hour) untuk produksi yang memakai generator AI. Temuan nyata pada referensi: `crayon_capital_analysis.md` §6.

---

## 1. Kategori dan keparahan

**Kategori temuan (wajib dipakai di setiap laporan QC):**
| Kode | Kategori | Definisi |
|---|---|---|
| **A** | Actual visual error | Jelas salah dan tidak disengaja: menembus objek, props hilang, off-model |
| **B** | Minor imperfection | Terlihat bila diperhatikan dan tidak merusak cerita: spacing kasar 1 frame, outline sedikit beda |
| **C** | Stylistic choice | Disengaja dan konsisten dengan gaya: smear, multiples, tangan tidak digambar |
| **D** | Potential technical issue | Perlu cek lebih lanjut: artefak kompresi, frame yang mungkin di tengah transisi |

**Keparahan:**
| Level | Definisi | Tindakan |
|---|---|---|
| S1 Blocker | Merusak pemahaman, fakta salah di layar, aset berhak cipta/sensitif | wajib perbaikan sebelum render |
| S2 Major | Langsung terlihat penonton umum | wajib perbaikan |
| S3 Minor | Terlihat penonton jeli | perbaiki bila waktu cukup |
| S4 Polish | Hanya terlihat frame-by-frame | catat untuk episode berikut |

**Larangan:** jangan mengklasifikasikan stylistic choice sebagai bug. Jangan melaporkan bug yang tidak benar-benar terlihat; sertakan timecode dan screenshot untuk setiap temuan.

## 2. Katalog error, deteksi, pencegahan, perbaikan

| # | Error | Cara deteksi | Pencegahan | Perbaikan |
|---|---|---|---|---|
| 1 | **Character morphing tak disengaja** (kepala jadi oval, badan berubah) | Overlay model sheet 50% di atas frame; scrub | Rig terkunci, kepala = shape primitif | Reset ke rig default, re-pose |
| 2 | **Perubahan proporsi antarscene** | Ukur Ø kepala di 3 shot berurutan dengan jarak kamera sama (toleransi ±3%) | Template ukuran per shot size | Skala ulang karakter di layout |
| 3 | **Inconsistent design** (props identitas hilang, warna salah) | Color picker vs HEX model sheet; checklist props | Bank aset terpusat, jangan copy-paste aset lama | Ganti dengan aset master |
| 4 | **Unnatural movement / tanpa bobot** | Tonton real-time tanpa suara; cek spacing chart | Antisipasi + easing + settle | Tambah antisipasi/overshoot, perbaiki spacing |
| 5 | **Broken anatomy** (lengan garis putus, sendi patah) | Onion skin pada pose ekstrem | Rig test pose ekstrem; batas panjang rubber-hose | Atur ulang titik kontrol, tambah drawing koreksi |
| 6 | **Floating objects / kaki melayang** | Cek bayangan kontak dan garis lantai | Bayangan kontak wajib, *foot lock* | Kunci kaki ke ground plane |
| 7 | **Incorrect object interaction** (tangan tidak menyentuh, objek tidak ikut) | Frame-step pada kontak | Parent objek ke tangan di frame kontak | Re-parent, tambah frame kontak |
| 8 | **Clipping** (lengan menembus badan/meja) | Scrub di zoom 200% | Urutan layer per pose (lengan depan/belakang swap) | Swap urutan layer, mask |
| 9 | **Visual artifacts** (pixelasi, banding, aliasing) | Tonton render final di 100% + upload private | Render ProRes/high-bitrate, hindari blur berat pada detail kecil | Kurangi blur, naikkan bitrate, tambah dither |
| 10 | **Flickering / boiling tak disengaja** | Loop 2 detik; perhatikan titik "kunci" (pupil, sudut mulut, garis rambut) | Vektor dari rig (tanpa redraw), jaga ketebalan stroke | Ganti drawing yang tidak konsisten |
| 11 | **Inconsistent lighting** (arah shadow berbeda dalam scene) | Cek sisi shadow sabit semua karakter | Catat arah key light per scene di layout | Flip shadow layer |
| 12 | **Inconsistent shadows** (bayangan kontak hilang/beda) | Checklist per shot | Bayangan kontak sebagai bagian rig | Tambah/seragamkan |
| 13 | **Discontinuous movement** (pose loncat antar-cut) | Bandingkan frame terakhir shot A dengan frame pertama shot B | Handoff pose tercatat di shot list | Sesuaikan pose awal/akhir |
| 14 | **Incorrect perspective** | Garis bantu titik hilang | Template BG dengan grid | Redraw props |
| 15 | **Unnatural camera** (gerak linear, jitter) | Cek kurva kamera di graph editor | Easing wajib; 1 gerak bermotivasi per shot | Haluskan kurva |
| 16 | **Poor transitions** (flash frame, frame hitam 1f, lompatan warna) | Frame-step di setiap cut | Edit di timeline frame-accurate | Trim/extend 1–2 frame |
| 17 | **Inconsistent frame timing** (campur ones/twos tidak disengaja) | Hitung exposure per karakter | Aturan exposure per shot di direction sheet | Step ulang |
| 18 | **Temporal artifacts** (AI: tekstur bergerak, bentuk berdenyut) | Loop dan perbesar | Gunakan AI hanya untuk BG statis/konsep | Ganti dengan aset vektor |
| 19 | **Unintended deformation** (stroke melebar saat scale, mesh robek) | Scrub pada keyframe skala | Scale-stroke dikompensasi | Perbaiki setting stroke/mesh |
| 20 | **Background inconsistency** (props BG pindah antarshot) | Bandingkan shot di lokasi yang sama | Satu master BG per lokasi | Ganti dengan master |
| 21 | **Teks terpotong / di luar safe area** | Overlay title-safe 90% | Template teks | Reposisi |
| 22 | **Lip/brow desync** dengan VO | Tonton dengan suara, cek kata kunci | Timing dari waveform | Geser ±1–2 frame |
| 23 | **Fakta/angka salah di layar** | Cocokkan semua angka ke naskah final + sumber | Fact-check sebelum animasi | Perbaiki aset teks |
| 24 | **Aset bermasalah hukum** (logo, foto, musik tanpa lisensi) | Audit daftar aset | Library berlisensi | Ganti/hapus |

## 3. Teknik pemeriksaan
1. **Real-time tanpa suara** → kejelasan staging dan akting.
2. **Real-time dengan suara** → sinkron, pacing.
3. **Frame-step di setiap cut** (±3 frame) → flash frame, kontinuitas pose.
4. **Loop pendek 2 detik** di zoom 200% → boil, flicker, clipping.
5. **Overlay model sheet** pada 1 frame per shot → off-model.
6. **Mirror/flip horizontal** → ketidakseimbangan komposisi dan drawing yang miring.
7. **Grayscale check** → kontras nilai tokoh vs latar.
8. **Thumbnail-size check** (frame dikecilkan ke 320×180) → keterbacaan siluet.
9. **Upload private ke YouTube** → artefak kompresi (terutama blur, gradien, confetti).

## 4. Pelajaran dari referensi
- Motion blur berat pada tokoh jatuh bisa menghasilkan blok pixel setelah kompresi (Great Depression ≈8:14, kategori D). → Pakai smear tergambar untuk wajah, dan batasi blur pada badan/tungkai.
- Segmen sponsor foto-realistis memutus gaya (kategori C). → Wajib dibungkus bumper.
- Label dan teks di tepi frame bisa tampak terpotong pada frame transisi (kategori D). → Cek frame tengah transisi, bukan hanya frame akhir.
- Thumbnail boleh lebih detail dari model video, asal siluet dan warna identik (kategori C).
