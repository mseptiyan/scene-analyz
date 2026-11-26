# Workflow: Animation Quality Assurance

Tujuan: memastikan tidak ada temuan kategori A dengan keparahan S1/S2 yang lolos ke publik, dan semua stylistic choice terdokumentasi.
Referensi katalog error: `references/quality_control_and_bug_detection.md`.

---

## 1. Tiga lapis QC
| Lapis | Kapan | Siapa | Alat |
|---|---|---|---|
| L1 Self-check | setiap shot selesai polish | animator | `animation_motion_checklist`, `character_consistency_checklist` §B |
| L2 Director review | animatic, blocking, polish, comp | director/lead | catatan per shot |
| L3 Final full-pass | sebelum render final & setelah upload private | QC/TD | prosedur §2 + `final_render_checklist` |

## 2. Prosedur full-pass (L3)
1. **Pass 1, tanpa suara, real-time:** staging, akting, keterbacaan, kejelasan cerita visual.
2. **Pass 2, dengan suara, real-time:** sinkron VO/SFX/teks, pacing, mix.
3. **Pass 3, cut-by-cut frame-step** (±3 frame tiap cut): flash frame, kontinuitas pose/props/warna, transisi.
4. **Pass 4, inspeksi teknis:** zoom 200% pada loop 2 detik untuk shot hero dan shot berisiko (blur, partikel, teks kecil).
5. **Pass 5, model check:** overlay model sheet di 1 frame per shot tokoh hero.
6. **Pass 6, fakta dan legal:** semua angka, nama, logo, musik.
7. **Pass 7, platform:** tonton versi private di YouTube (desktop + ponsel), cek kompresi dan thumbnail.

## 3. Klasifikasi setiap temuan
Untuk setiap temuan, tanyakan berurutan:
1. Apakah disengaja dan konsisten dengan gaya? → **C** (catat, tidak diperbaiki).
2. Apakah jelas salah dan terlihat penonton umum? → **A**, lalu tentukan S1/S2.
3. Apakah hanya terlihat jika diperhatikan? → **B** (S3/S4).
4. Apakah belum pasti (mungkin kompresi/transisi)? → **D**, lalu verifikasi di master dan versi upload.

**Jangan** melaporkan sesuatu yang tidak bisa ditunjukkan dengan timecode + screenshot.

## 4. Aturan rilis
- 0 temuan S1.
- 0 temuan A-S2.
- Temuan B-S3 boleh ≤ 5, semua tercatat untuk perbaikan episode berikut.
- Semua temuan D sudah diverifikasi menjadi A/B/C atau ditutup.

## 5. Format laporan QC (output standar)
```markdown
# QC Report: <judul> v<versi> (<tanggal>)
Metode: full-pass 7 tahap | Durasi: __:__ | Reviewer: __

## Ringkasan
- A: _ (S1 _, S2 _) | B: _ | C (tercatat): _ | D: _
- Status rilis: BLOCKED / APPROVED WITH NOTES / APPROVED

## Temuan
| # | TC | Shot ID | Kategori | Keparahan | Deskripsi | Bukti | Perbaikan | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | 00:03:12:08 | SQ030_SH0120 | A | S2 | Lengan kiri menembus meja 4 frame | ss_001.png | swap layer lengan ke depan meja | open |

## Stylistic choices yang dikonfirmasi
- Smear/multiples di SQ040_SH0050 (lari), disengaja.

## Catatan untuk episode berikut
- …
```
