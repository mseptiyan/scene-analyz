# ANIMATION PRODUCTION SOP: Crayon Verse

17 SOP. Masing-masing berisi **Tujuan, Standar, Langkah, Hindari, Kriteria keberhasilan, Checklist**. Detail teknis ada di file referensi yang ditautkan, sehingga SOP ini bisa dipakai sebagai pedoman tanpa mengulang riset.

---

## SOP-01 Visual Direction
- **Tujuan:** setiap frame langsung dikenali sebagai Crayon Verse dan menyampaikan satu ide.
- **Standar:** flat-vector cartoon; karakter kepala bulat, badan bean, tungkai garis; outline `#1A1617` 8–10 px; 1 shadow sabit; hierarki warna (hero berwarna, figuran putih, kerumunan abu); satu hue per lokasi; teks tulisan tangan; metafora literal. (`SKILL.md` §2)
- **Langkah:** (1) tetapkan style frame per lokasi; (2) buat 3 *style frame* hero (hook, mekanisme, klimaks); (3) dapatkan persetujuan director; (4) jadikan acuan semua artis.
- **Hindari:** gradien di karakter, garis tipis bergetar (gaya lama), terlalu banyak tokoh berwarna, latar putih kosong (kecuali sengaja), logo/aset asli channel referensi.
- **Kriteria:** 10 frame acak dari video lulus "tes identitas" (dikenali gaya tanpa logo) dan "tes 1 detik" (ide terbaca).
- **Checklist:** `scene_quality_checklist` (Staging, Lighting).

## SOP-02 Character Design Standards
- **Tujuan:** semua tokoh dibangun dari satu sistem bentuk yang appealing dan mudah dianimasikan.
- **Standar:** `character_design_standards.md` §1–5.
- **Langkah:** brief tokoh → ambil dari bank → desain siluet + props identitas → warna (HEX) → 12 ekspresi → mouth chart → turnaround → pose sheet → review.
- **Hindari:** leher, hidung, tangan detail di video, kepala oval, tokoh yang hanya bisa dibedakan dari warna.
- **Kriteria:** silhouette test membedakan semua tokoh hero; model sheet lengkap.
- **Checklist:** `character_consistency_checklist` §A.

## SOP-03 Character Consistency Rules
- **Tujuan:** nol off-model yang tidak disengaja di seluruh video dan seri.
- **Standar:** toleransi Ø kepala ±3% pada shot size sama; HEX identik; props identitas selalu ada; outline tetap saat scale. (`character_design_standards.md` §7)
- **Langkah:** pakai aset master dari bank → overlay model sheet di 1 frame per shot → catat modifikasi lighting.
- **Hindari:** copy-paste aset dari project lama tanpa sinkron bank; redraw kepala manual.
- **Kriteria:** 0 temuan off-model kategori A di QC.
- **Checklist:** `character_consistency_checklist` §B, §C.

## SOP-04 Environment Design Standards
- **Tujuan:** latar yang menjelaskan lokasi dan mood tanpa mencuri fokus.
- **Standar:** satu hue dominan per lokasi (`lighting_and_color.md` §3); band nilai atau gradien; outline lebih tipis di BG jauh; layer `BG_far/mid/near/FG/LIGHT`; perspektif sederhana yang benar.
- **Langkah:** moodboard → BG key per lokasi → tetapkan key light → master BG → varian crop/lighting.
- **Hindari:** detail sibuk di belakang wajah; hue lokasi berubah tanpa motivasi; perspektif salah.
- **Kriteria:** tokoh kepala putih kontras di semua BG (grayscale test); lokasi berulang identik.
- **Checklist:** `scene_quality_checklist` (Latar).

## SOP-05 Storyboarding Standards
- **Tujuan:** setiap kalimat VO punya visual yang jelas sebelum animasi dimulai.
- **Standar:** 1 panel/shot (lebih untuk aksi kompleks); berisi Shot ID, framing, panah gerak, ekspresi, teks, SFX. (`pre_production.md` §6, §7.2)
- **Langkah:** script breakdown → thumbnail board kasar → board bersih → review keterbacaan → animatic.
- **Hindari:** panel yang hanya "kepala bicara" berturut-turut; visual yang mengulang VO secara harfiah tanpa metafora.
- **Kriteria:** setiap panel terbaca tanpa VO; variasi shot terpenuhi.
- **Checklist:** `pre_production.md` §8.

## SOP-06 Scene Composition Standards
- **Tujuan:** perhatian penonton jatuh ke tempat yang benar dalam ≤ 1 detik.
- **Standar:** satu titik fokus; tengah/sepertiga; lineup 3–5 tokoh; headroom teks 15–20%; title-safe 90%; FG framing. (`cinematography_and_composition.md` §4)
- **Langkah:** layout dari animatic → cek silhouette & grayscale → cek safe area → cek 180°.
- **Hindari:** tangensi, frame penuh tanpa negative space, teks di pojok kanan bawah.
- **Kriteria:** lulus silhouette, grayscale, dan thumbnail-size test.
- **Checklist:** `scene_quality_checklist` (Staging & komposisi).

## SOP-07 Camera Movement Standards
- **Tujuan:** kamera hanya bergerak bila menambah makna.
- **Standar:** default locked-off eye-level; maks 1 gerak bermotivasi per shot; semua dengan easing; parameter di `cinematography_and_composition.md` §3.
- **Langkah:** tentukan motivasi → pilih gerak → set kurva ease-in-out → cek stroke scaling.
- **Hindari:** gerak linear, zoom tanpa alasan, shake berlebihan, kombinasi pan+zoom+rotate sekaligus.
- **Kriteria:** setiap gerak kamera dapat dijelaskan dengan satu kata (tekankan/ungkap/ikuti/impact).
- **Checklist:** `animation_motion_checklist` (Kamera).

## SOP-08 Animation Timing Standards
- **Tujuan:** gerak sinkron dengan narasi dan terasa berbobot.
- **Standar:** 24 fps; on twos untuk akting; tabel timing di `animation_fundamentals.md` §9; aksi di kata kunci VO; hold akhir ≥ 12 f.
- **Langkah:** tandai kata kunci di waveform → key pose pada frame tersebut → blocking step → spline → step ke twos.
- **Hindari:** aksi yang terlambat dari VO; gerakan semua karakter bersamaan; hold mati.
- **Kriteria:** penonton uji dapat menunjuk "momen" setiap kalimat penting.
- **Checklist:** `animation_motion_checklist` (Timing).

## SOP-09 Character Movement Standards
- **Tujuan:** tokoh bergerak hidup, jelas, dan konsisten dengan kepribadian.
- **Standar:** rig + rubber-hose; moving hold; jalan/lari/take/jatuh sesuai `character_animation_standards.md` §3–6.
- **Langkah:** pilih gerak dari kosakata → blocking → review → polish (arc, overlap, smear) → bayangan kontak.
- **Hindari:** foot slide, rig pop, motion blur berat di wajah, tungkai memanjang aneh.
- **Kriteria:** 0 temuan A pada motion; aksi terbaca tanpa suara.
- **Checklist:** `animation_motion_checklist`.

## SOP-10 Facial Expression Standards
- **Tujuan:** emosi terbaca instan dari wajah minimal.
- **Standar:** 12 ekspresi library; alis memimpin; mulut ekspresi atau flap/fonem sesuai situasi (`character_animation_standards.md` §5).
- **Langkah:** tentukan beat emosi per kalimat → pilih ekspresi → alis bergerak 1–2 f lebih dulu → mulut → kedip.
- **Hindari:** ekspresi berubah acak; mulut bergerak saat tokoh tidak bicara; exaggeration komedik di topik tragis.
- **Kriteria:** ekspresi terbaca saat mulut ditutup (tes alis+mata).
- **Checklist:** `animation_motion_checklist` (Wajah).

## SOP-11 Lighting Standards
- **Tujuan:** membangun mood dan mengarahkan mata tanpa merusak gaya flat.
- **Standar:** 1 key light per scene; shadow sabit 1 tone; rim berwarna opsional; overlay atmosfer 10–25% (`lighting_and_color.md` §4–5).
- **Langkah:** catat arah key di layout → shadow pass → rim/color cast → overlay → cek wajah dan teks tidak tertutup.
- **Hindari:** arah shadow campur dalam satu scene; gradien di karakter; overlay menutupi wajah.
- **Kriteria:** semua shadow konsisten; tokoh fokus paling terang/kontras.
- **Checklist:** `scene_quality_checklist` (Lighting).

## SOP-12 Color Grading Standards
- **Tujuan:** kontinuitas warna antar-shot dan mood per bab.
- **Standar:** grade per sekuens; luminance median 0,40–0,55; saturasi median 0,25–0,35; preset mood (`lighting_and_color.md` §6).
- **Langkah:** samakan ke BG key → grade sekuens → bandingkan shot berurutan → cek grayscale.
- **Hindari:** grade per shot yang meloncat; frame gelap > 3 detik tanpa alasan.
- **Kriteria:** tidak ada lompatan warna yang terasa saat cut.
- **Checklist:** `scene_quality_checklist` (Lighting dan warna).

## SOP-13 Transition Standards
- **Tujuan:** perpindahan mempertahankan alur dan tidak mengganggu.
- **Standar:** hierarki transisi (`transition_and_editing.md` §1); hard cut on beat default; bumper sponsor.
- **Langkah:** tentukan jenis per cut di shot list → eksekusi → frame-step ±3 f di setiap cut.
- **Hindari:** preset NLE generik; flash/black frame; dissolve berlebihan.
- **Kriteria:** 0 flash frame; setiap transisi non-cut punya alasan naratif.
- **Checklist:** `final_render_checklist` (Video), QA Pass 3.

## SOP-14 Sound Synchronization Standards
- **Tujuan:** suara memperkuat aksi dan narasi.
- **Standar:** −14 LUFS, ≤ −1 dBTP; musik −18 s/d −24 dB di bawah VO; SFX impact ±1 f; mulut mendahului suara 1–2 f (`transition_and_editing.md` §4).
- **Langkah:** clean VO → spotting SFX dari shot list → sinkron → music bed + ducking → master → cek di ponsel.
- **Hindari:** musik menutupi VO; SFX telat; aset audio tanpa lisensi.
- **Kriteria:** VO terdengar jelas di speaker ponsel; tidak ada desync terasa.
- **Checklist:** `final_render_checklist` (Audio).

## SOP-15 Visual Effects Standards
- **Tujuan:** FX menegaskan emosi dan aksi.
- **Standar:** tabel FX di `workflows/production.md` §6; outline ink yang sama; on ones/twos sesuai jenis.
- **Langkah:** tentukan FX di storyboard → animasikan setelah aksi utama final → cek tidak menutupi wajah/teks → cek kompresi.
- **Hindari:** partikel terlalu padat; blur besar (artefak kompresi); FX realistis yang keluar gaya.
- **Kriteria:** FX terlihat di versi YouTube tanpa blocking; tidak mengalihkan dari aksi utama.
- **Checklist:** `scene_quality_checklist` (FX).

## SOP-16 Quality Assurance Standards
- **Tujuan:** tidak ada error berarti yang lolos; stylistic choice terdokumentasi.
- **Standar:** 3 lapis QC; kategori A/B/C/D; keparahan S1–S4; aturan rilis (`workflows/animation_quality_assurance.md`).
- **Langkah:** L1 self-check → L2 director review → L3 full-pass 7 tahap → laporan → perbaikan → verifikasi ulang.
- **Hindari:** melaporkan bug tanpa bukti; melabeli gaya sebagai bug; skip upload private.
- **Kriteria:** 0 S1, 0 A-S2, semua D tertutup.
- **Checklist:** semua checklist.

## SOP-17 Final Rendering Standards
- **Tujuan:** master berkualitas tinggi dan versi upload optimal untuk YouTube.
- **Standar:** spesifikasi di `workflows/post_production.md` §6.
- **Langkah:** lock edit → render master → encode upload → upload private → QC platform → publik → arsip.
- **Hindari:** fps campur, bitrate rendah, placeholder tertinggal.
- **Kriteria:** versi publik bebas artefak berat; thumbnail terbaca di semua ukuran.
- **Checklist:** `final_render_checklist`.
