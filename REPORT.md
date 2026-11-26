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
**Metode jujur:** sampling frame, bukan frame-by-frame. Bahannya 144 gambar resmi YouTube (thumbnail + 3 frame otomatis 1280×720 per video), ditambah pengukuran kuantitatif palet, saturasi, luminance, dan ketebalan garis. Video penuh **tidak dapat diakses** (halaman watch YouTube memblokir IP container dengan verifikasi bot), sehingga:
- **Hook 0–5 detik:** tidak teramati. Yang dianalisis adalah packaging hook (judul pop-culture + janji ELI5; thumbnail tokoh tenang berwarna di tengah pesta kerumunan abu).
- **Shot-by-shot:** diganti breakdown 4 frame sampel video utama (≈4:08, ≈8:16, ≈12:25, thumbnail) dan katalog 10 tipe shot dari 108 frame lintas channel.
- **Karakter:** kepala lingkaran sempurna, badan bean = pakaian, tungkai garis (rubber-hose), tanpa leher, mata oval kecil, alis mengambang; hierarki warna (hero berkulit, figuran putih, kerumunan abu); identitas lewat siluet dan props.
- **Motion:** [inferensi] rig cut-out + rubber-hose, smear/multiples digambar, motion blur komposit. Fps tidak dapat diverifikasi.
- **Kamera:** dominan locked-off eye-level frontal; lineup, OTS, split-screen, insert infographic.
- **Lighting/color:** outline `#171415`–`#1C261D` ±5–6 px @720p; shadow sabit 1 tone; 1 hue per lokasi; sorotan dan spotlight atmosferik; saturasi median 0,29, luminance 0,50; tren makin sinematik dan gelap di 2026.
- **Transisi:** tidak dapat diverifikasi. Jejak teramati: split panel, time card.
- **Bug detection:** 9 temuan terklasifikasi. Tidak ada error kategori A yang pasti. Ada 3 kategori D (pixelasi motion blur pada wajah, label/teks terpotong di frame transisi) dan beberapa stylistic choice (smear, segmen sponsor foto-realistis, thumbnail lebih detail).

## D. Animation Production SOP
- **17 SOP**: visual direction, character design, consistency, environment, storyboard, composition, camera, timing, movement, facial expression, lighting, grading, transition, sound, VFX, QA, final render. Masing-masing berisi tujuan, standar, langkah, larangan, kriteria, dan checklist (`references/animation_production_sop.md`).
- **Workflow produksi:** 16 langkah, dari brief sampai render, dengan gate per fase (`SKILL.md` §9 + `workflows/`).
- **QC:** 3 lapis (self-check, director, full-pass 7 tahap), kategori A/B/C/D, keparahan S1–S4, aturan rilis, dan 4 checklist.

## E. Skill Creation
- **Lokasi:** `.claude/skills/animate-crayon-verse/` di repo ini. Otomatis terbaca oleh Claude Code di setiap sesi yang membuka repo ini (cloud maupun laptop).
- **File (21):**
  - `SKILL.md`
  - `references/`: animation_fundamentals, professional_animation_pipeline, character_design_standards, character_animation_standards, cinematography_and_composition, lighting_and_color, transition_and_editing, quality_control_and_bug_detection, crayon_capital_analysis, **animation_production_sop** (tambahan), **skill_validation** (tambahan), `data/channel_audit.csv`
  - `workflows/`: pre_production, production, post_production, animation_quality_assurance
  - `checklists/`: character_consistency, scene_quality, animation_motion, final_render
- **Kemampuan:** konsep, character brief, storyboard, shot list, animation direction, kamera, timing/spacing, konsistensi karakter, deteksi bug, QC, template prompt gambar AI, adaptasi 9:16.
- **Pakai di semua proyek (laptop):** salin folder ke `~/.claude/skills/animate-crayon-verse/`.

## F. Skill Validation
- **Uji:** proyek fiktif *"Tulip Mania Explained Like You're 5"*, mencakup 10 kemampuan yang diminta (`references/skill_validation.md`).
- **Kekurangan yang ditemukan (5):** tidak ada cara menulis spacing chart; tidak ada ukuran acuan Ø kepala per shot size; rujukan § template shot list salah; tidak ada panduan format vertikal; aturan topik tragis tidak terlihat di SKILL.md.
- **Perbaikan:** kelimanya sudah diperbaiki.
- **Status akhir:** ✅ 10/10 lulus. Batas yang tersisa adalah standar hook, transisi, dan audio, yang berbasis industri karena video penuh referensi tidak dapat diakses. Bagian ini bisa diperbarui bila akses tersedia.
