# Laporan Akhir: Skill `animate-crayon-verse`

Tanggal: 2026-11-26 · Lokasi skill: [`.claude/skills/animate-crayon-verse/`](.claude/skills/animate-crayon-verse/SKILL.md)

---

## A. Channel Audit
- **Video teraudit:** 36/36 (seluruh tab Videos @crayon_capital; 327 rb subscriber).
- **Sumber data:** RSS resmi YouTube (15 video terbaru: likes + tanggal tepat), Return YouTube Dislike API (21 video lama: likes cache), tab Videos (durasi, views, tanggal perkiraan).
- **Statistik:** total views 28,09 jt · total likes 494.911 · **median likes 7.503** (Q1 4.026 / Q3 16.301) · median views 444.476 · median rasio likes/views 1,99% · median durasi 15:05.
- **Format ELI5** (17 video) median likes 10.317 vs format lain 4.466 (±2,3×).
- **Engagement terbaik:** *The Wolf of Wall Street Scam Explained Like You're 5*. #1 likes (80.296 = 10,7× median), #1 views (4,31 jt), rasio 1,86%.
- **Rasio tertinggi:** *The Greatest Slave System Ever Created* (3,37%), tetapi dengan views 59× lebih kecil.
- **Alasan memilih Wolf:** juara absolut likes dan views, dengan rasio yang dekat median. Artinya video ini memuaskan audiens luas, bukan hanya audiens inti. Rasio tinggi pada views kecil lebih mencerminkan subscriber setia.
- **Tidak tersedia:** jumlah komentar per video.
- Detail: `references/crayon_capital_analysis.md` §2, data mentah `references/data/channel_audit.csv`.

## B. Professional Animation Research
- **Referensi:** Thomas & Johnston *The Illusion of Life* (12 prinsip); Williams *The Animator's Survival Kit* (timing/spacing); Preston Blair *Cartoon Animation* (mouth chart); Mascelli *The Five C's of Cinematography*; Toon Boom Learn & Harmony docs (pipeline, cut-out rig, lip-sync); Tahoma2D docs (layout); CG Spectrum, Pixune, Fiveable (pipeline); Adobe, StudioBinder, NYFA (prinsip); Wikipedia "Model sheet", Animation Field Notes, Digicel, Keith Lango checklist, Netflix Backlot (QC/off-model/boil).
- **Prinsip paling relevan:** staging, timing, exaggeration, appeal, anticipation, easing, follow-through.
- **Pipeline acuan:** pre-production (konsep → naskah → design → storyboard → animatic terkunci) → production (aset → rig → layout → blocking → polish → FX → lighting) → post (comp → grade → edit → sound → QC → render), diadaptasi untuk explainer yang dipimpin VO.

## C. Deep Video Analysis
**Pembaruan 2026-11-27: frame-by-frame dari file video asli** (via Google Drive). Hasil lengkap ada di `references/wolf_frame_analysis.md`.
- **Metode:** semua **29.774 frame** (30 fps, 16:32) diukur otomatis: selisih piksel, warna, dan gerak kamera. Yang saya lihat langsung: **180 frame hook (0–6 dtk)**, ±4 frame di **157 titik potong**, frame awal/tengah/akhir di **158 shot**, dan **6 sekuens aksi** per frame. Narasi ditranskrip Whisper dengan timestamp per kata (2.470 kata). Saya tidak melihat semua frame satu per satu dengan mata.
- **Hook:** f0 langsung menampilkan tokoh **anonim berwajah abu** memegang "$1". Lima hard cut dalam 18 dtk ($1 → gunung uang → penjara → koran Hollywood → panggung). Wajah tokoh berwarna tepat saat namanya disebut (10,4 dtk). Pull-out mengungkap penonton bersorak di kalimat "People still cheer for him".
- **Shot-by-shot:** tabel 158 shot dengan timestamp, scene, karakter, aksi, ekspresi, kamera terukur, warna, prinsip, transisi, narasi, dan kualitas.
- **Pacing:** shot median 5,2 dtk · 9,5 shot/menit · narasi 149 kata/menit · cut median 0,22 dtk sebelum frasa.
- **Motion:** tween on ones + **swap pose instan tanpa in-between** (limited animation) + objek lepas dianimasikan penuh (confetti, kertas uang). Kesimpulan teknik: rig/cut-out + tween; software tidak dapat dipastikan.
- **Kamera:** 94/158 shot memakai drift zoom lambat **berkecepatan konstan** (median 4%/dtk, dominan pull-out), 52 locked-off.
- **Lighting/color:** spotlight radial elips di latar sebagai alat staging; palet bergeser per bab (cerah → kantor → pesta → krisis → abu gelap → kembali merah panggung).
- **Transisi:** 125/157 hard cut 1 frame, 25 cut ke/dari kartu hitam write-on, 1 fade, 0 dissolve; ada callback dan bookend.
- **Bug:** kontras teks putih di langit biru muda rendah (minor); balon teks menumpuk tak terbaca; true peak audio −0,4 dBFS (perlu cek teknis). Satu dugaan "teks ganda" ternyata artefak lembar kontak saya, bukan bug video.
- **Skill diperbarui** berdasarkan data ini: SKILL.md, kamera, animasi karakter, transisi/pacing, standar hook, QC.

## D. Animation Production SOP
- **17 SOP**: visual direction, character design, consistency, environment, storyboard, composition, camera, timing, movement, facial expression, lighting, grading, transition, sound, VFX, QA, final render. Masing-masing berisi tujuan, standar, langkah, larangan, kriteria, dan checklist (`references/animation_production_sop.md`).
- **Workflow produksi:** 16 langkah, dari brief sampai render, dengan gate per fase (`SKILL.md` §9 + `workflows/`).
- **QC:** 3 lapis (self-check, director, full-pass 7 tahap), kategori A/B/C/D, keparahan S1–S4, aturan rilis, dan 4 checklist.

## E. Skill Creation
- **Lokasi:** `.claude/skills/animate-crayon-verse/` di repo ini. Otomatis terbaca oleh Claude Code di setiap sesi yang membuka repo ini (cloud maupun laptop).
- **File (24):**
  - `SKILL.md`
  - `references/`: animation_fundamentals, professional_animation_pipeline, character_design_standards, character_animation_standards, cinematography_and_composition, lighting_and_color, transition_and_editing, quality_control_and_bug_detection, crayon_capital_analysis, **animation_production_sop** (tambahan), **skill_validation** (tambahan), `data/channel_audit.csv`, **wolf_frame_analysis** + `data/wolf_shots.csv` + `data/wolf_transcript.tsv` (frame-by-frame)
  - `workflows/`: pre_production, production, post_production, animation_quality_assurance
  - `checklists/`: character_consistency, scene_quality, animation_motion, final_render
- **Kemampuan:** konsep, character brief, storyboard, shot list, animation direction, kamera, timing/spacing, konsistensi karakter, deteksi bug, QC, template prompt gambar AI, adaptasi 9:16.
- **Pakai di semua proyek (laptop):** salin folder ke `~/.claude/skills/animate-crayon-verse/`.

## F. Skill Validation
- **Uji:** proyek fiktif *"Tulip Mania Explained Like You're 5"*, mencakup 10 kemampuan yang diminta (`references/skill_validation.md`).
- **Kekurangan yang ditemukan (5):** tidak ada cara menulis spacing chart; tidak ada ukuran acuan Ø kepala per shot size; rujukan § template shot list salah; tidak ada panduan format vertikal; aturan topik tragis tidak terlihat di SKILL.md.
- **Perbaikan:** kelimanya sudah diperbaiki.
- **Status akhir:** ✅ 10/10 lulus. Batas yang tersisa adalah standar hook, transisi, dan audio, yang berbasis industri karena video penuh referensi tidak dapat diakses. Bagian ini bisa diperbarui bila akses tersedia.
