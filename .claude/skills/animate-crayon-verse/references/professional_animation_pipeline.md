# Professional 2D Animation Pipeline (Dasar Industri → Adaptasi Crayon Verse)

**Sumber:** Toon Boom Learn ("Traditional Animation Workflow", "Pre-production", "Cut-out Animation Workflow"), dokumentasi Toon Boom Harmony "How to Rig a Cut-out Character", Tahoma2D docs "Production workflow", CG Spectrum "Guide to animation pipeline", Pixune "The Complete 2D Animation Pipeline", Fiveable "Animation workflow and production pipeline". Secara umum sumber-sumber ini sepakat pada tiga fase (pre-production, production, post-production). Batas tiap tahap berbeda antar-studio.

---

## 1. Peta pipeline

| Fase | Tahap | Output | Pemilik | Gate kualitas |
|---|---|---|---|---|
| **Pre-production** | Concept development | Logline, angle, judul + konsep thumbnail | Director/Writer | Topik lulus uji "kenapa sekarang & kenapa peduli" |
| | Riset & scriptwriting | Naskah VO final (±130–150 kata/menit) | Writer | Fakta terverifikasi, struktur ELI5 |
| | Visual research | Moodboard per lokasi, referensi periode | Art director | Palet & hue per lokasi ditetapkan |
| | Character development | Daftar tokoh + peran + ciri | Director | Tiap tokoh punya fungsi naratif |
| | Character design | Model sheet, turnaround, ekspresi, mouth chart | Character designer | Lulus `character_consistency_checklist` |
| | Environment design | Background key per lokasi | BG designer | Hue dominan & arah cahaya jelas |
| | Storyboarding | Panel per shot + catatan aksi/kamera | Storyboard artist | Setiap kalimat VO punya visual |
| | Animatic | Storyboard dengan timing ke VO scratch/final | Editor + director | **Timing dikunci** |
| | Shot planning | Shot list + breakdown aset | AD/production manager | Semua aset teridentifikasi |
| **Production** | Asset creation | Karakter, props, BG dalam vektor berlapis | Asset artist | Penamaan layer standar |
| | Rigging | Rig cut-out (bone, rubber-hose limbs, swap mata/mulut/alis) | Rigger | Lulus rig test (pose ekstrem tanpa robek) |
| | Layout | Posisi kamera, karakter, BG final per shot | Layout artist | Sesuai animatic, aturan 180° |
| | Keyframe animation (blocking) | Key + extremes + breakdown | Animator | Review director |
| | In-between / spline | Gerak halus, easing | Animator | `animation_motion_checklist` |
| | Background production | BG final + overlay cahaya | BG painter | Konsisten dengan key |
| | Scene composition | Layer karakter/BG/FG | Compositor | Depth & fokus jelas |
| | Camera movement | Push, pan, shake | Layout/compositor | Easing, motivasi jelas |
| | Lighting | Shadow pass, rim, atmosfer | Compositor | Arah cahaya konsisten |
| | Visual effects | Smear, partikel, api, asap, glow | FX animator | Tidak menutupi aksi utama |
| **Post-production** | Compositing | Gabung semua pass | Compositor | `scene_quality_checklist` |
| | Color correction/grading | Grade per sekuens | Colorist | Kontinuitas warna antar-shot |
| | Sound design | SFX, ambience | Sound designer | Sinkron dengan aksi (±1 frame) |
| | Music synchronization | Music bed + stinger | Editor/composer | Ducking di bawah VO |
| | Editing | Cut final, teks layar, transisi | Editor | Pacing, kejelasan |
| | Final rendering | Master + delivery | Tech director | `final_render_checklist` |
| | Quality assurance | Full-pass QC + laporan | QC/TD | Semua issue A/B selesai |

---

## 2. Adaptasi untuk explainer YouTube 10–20 menit

Produksi explainer berbeda dari film animasi karena **narasi memimpin, gambar mengikuti**. Konsekuensinya:

1. **VO dikunci sebelum animatic.** Rekam VO final (atau scratch berkualitas tinggi) sebelum storyboard di-timing. Semua timing visual mengikuti gelombang VO.
2. **Rig dan library aset adalah investasi utama.** Dengan puluhan tokoh per video, gunakan *body bank* (badan bean dengan jas, seragam, gaun, kaos) + *head bank* (rambut, kacamata, topi, kumis) + *expression bank* (set alis, mata, mulut). Tokoh baru = rakit dari bank + 1–2 aset khusus.
3. **Animasi "cukup" per shot.** Prioritaskan: (1) pose dan ekspresi yang tepat, (2) gerak yang menekankan kata kunci, (3) moving hold. Animasi penuh hanya untuk momen kunci (hook, reveal, klimaks).
4. **Satu BG bisa dipakai banyak shot.** Variasikan dengan crop/framing, pencahayaan, dan karakter di dalamnya.
5. **Thumbnail diproduksi paralel** sejak pre-production, sebagai *render premium* dari model karakter yang sama.

### Anggaran waktu indikatif (video 15 menit, tim kecil) [Rekomendasi]
| Tahap | Porsi |
|---|---|
| Riset + naskah | 15% |
| Design + storyboard + animatic | 20% |
| Asset & rig (berkurang drastis di video ke-3+ berkat bank aset) | 15% |
| Animasi | 35% |
| Compositing, edit, sound | 10% |
| QC + revisi | 5% |

---

## 3. Struktur file dan penamaan (standar studio)

```
PROJECT_CODE/
├── 00_admin/            (brief, jadwal, laporan QC)
├── 01_script/           (naskah_v##.md, vo_scratch.wav, vo_final.wav)
├── 02_design/           (characters/, environments/, props/, model_sheets/)
├── 03_storyboard/       (board_v##.pdf)
├── 04_animatic/         (animatic_v##.mp4)
├── 05_assets/           (rigs/, bg/, fx/, fonts/, sfx/, music/)
├── 06_shots/            (SQ010_SH0010/, SQ010_SH0020/, ...)
├── 07_comp/
├── 08_edit/
└── 09_delivery/         (master/, youtube/, thumbnail/)
```
- Shot ID: `SQ###_SH####` (sekuens 10-an, shot 10-an, agar mudah menyisip).
- Versi: `_v###`, jangan pernah menimpa versi lama.
- Layer karakter: `CHR_<nama>_<bagian>` (mis. `CHR_banker_head`, `CHR_banker_brow_L`).

---

## 4. Review dan approval

| Checkpoint | Yang direview | Siapa |
|---|---|---|
| Naskah | Fakta, struktur, hook | Director + fact-checker |
| Model sheet | Proporsi, siluet, warna | Director |
| Animatic | Timing, kejelasan, pacing | Director |
| Blocking | Pose, staging, akting | Director/lead animator |
| Polish | Spacing, arcs, overlap | Lead animator |
| Comp | Cahaya, warna, depth | Art director |
| Final | Full-pass QC | QC/TD |

Prinsip: **koreksi paling murah dilakukan paling awal**. Masalah staging harus tertangkap di animatic, bukan di comp.
