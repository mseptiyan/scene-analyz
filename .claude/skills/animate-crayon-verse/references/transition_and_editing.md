# Transition, Editing, Text & Sound: Crayon Verse

> **Data terukur dari video referensi** (Wolf of Wall Street, 29.774 frame, lihat `wolf_frame_analysis.md` §3.3 & §3.7):
> - 157 titik potong: **125 hard cut 1 frame**, 25 cut ke/dari kartu hitam berteks, 1 fade-in dari hitam, 6 transisi efek (zoom ke dalam kepala, panel geser), **0 cross dissolve**.
> - Cut jatuh **median 0,22 dtk sebelum** frasa narasi berikutnya; 78% ≤ 0,5 dtk dari awal frasa.
> - Shot median **5,2 dtk** (p10 2,1 · p90 11,7) · 9,5 shot/menit · narasi **149 kata/menit**, jeda antarfrasa median 0,64 dtk.
> - Kartu teks: hitam, teks tulisan tangan putih **write-on huruf demi huruf** sinkron narasi; dipakai untuk 5 judul bab + punchline.
> - Audio master: −17,7 LUFS integrated, LRA 3,7 LU, true peak −0,4 dBFS.
>
> Standar di bawah menggabungkan data ini dengan [Standar industri] + [Rekomendasi].

---

## 1. Hierarki transisi
| Prioritas | Transisi | Kapan | Durasi |
|---|---|---|---|
| 1 | **Hard cut on beat** | default antar-shot dalam satu adegan | 0 |
| 2 | **Match cut** (bentuk/warna/posisi sama) | lompat waktu/tempat dengan kontinuitas visual (koin → matahari, gelembung → bola dunia) | 0 |
| 3 | **Object/motion wipe** (objek atau tokoh melintasi layar menutupi frame) | antar-adegan dalam bab yang sama | 8–14 f |
| 4 | **Zoom ke dalam objek** (layar TV, peta, mata) | masuk ke penjelasan detail | 10–16 f |
| 5 | **Panel/split slide** | perbandingan [Teramati: tri-split Epstein ≈9:25, diagonal Ozempic ≈9:31] | 8–12 f |
| 6 | **Whip pan** | energi, montase cepat | 4–6 f |
| 7 | **Dip to black / fade** | ganti bab besar, lompatan waktu besar, penutup | 12–24 f |
| 8 | **Cross dissolve** | hampir tidak dipakai; hanya mimpi/kenangan | 12–18 f |

Larangan: transisi preset NLE (cube spin, page curl, glitch generik) karena keluar dari gaya.

## 2. Pacing [Teramati + Rekomendasi]
- **Satu frasa narasi = satu shot.** Cut 0,1–0,3 dtk *sebelum* frasa dimulai (referensi: median 0,22 dtk).
- Durasi shot: referensi median **5,2 dtk**. Hook dan montase lebih cepat (1,5–3,6 dtk). Shot dialog/infografik boleh 8–12 dtk asal ada gerak kamera atau pop-in di dalamnya.
- **Aturan perubahan visual:** maksimal 6–8 detik tanpa perubahan visual bermakna (cut, aksi baru, pop-in, gerak kamera).
- **Bab:** setiap 2–4 menit ada *re-hook* visual (pertanyaan, angka mengejutkan, cliffhanger kecil).
- VO 130–150 kata/menit; jeda 0,3–0,6 detik setelah angka penting.

## 3. Sistem teks layar [Teramati]
| Jenis | Gaya | Posisi | Animasi |
|---|---|---|---|
| Dialog tokoh | Italic tulisan tangan, putih, stroke gelap 3–5 px | di atas/samping pembicara + tick pendek menunjuk kepala | pop/typewriter 4–6 f, hold ≥ 1 dtk/3 kata |
| Balon kata | Balon putih bulat/kotak, outline ink, teks gelap | dekat pembicara, ekor ke mulut | scale pop 6 f |
| Label objek | Kapital tulisan tangan di props | menempel pada objek | muncul bersama objek |
| Nama tokoh | Italic + panah melengkung ke tokoh | ruang kosong dekat tokoh | tulis/draw-on 8–12 f |
| Time card | Italic putih "X later..." | pojok kanan bawah (di atas safe area) | fade 6 f |
| Angka besar | Tulisan tangan besar, warna aksen (money/loss/gold) | tengah atau dekat objek | pop + overshoot |
| Stempel | Kapital tebal di kotak merah miring 8–15° | di atas tokoh/dokumen | slam scale 130→100% 3 f + shake |

**Font [Rekomendasi]:** gunakan font tulisan tangan yang berlisensi untuk penggunaan komersial (mis. keluarga *Patrick Hand*, *Kalam*, *Caveat* di Google Fonts, OFL) dan sans-serif tebal untuk thumbnail (*Montserrat Black*, *Anton*). Pilih 1 font dialog + 1 font judul, lalu kunci untuk seluruh seri.

## 4. Sound design [Standar industri + Rekomendasi]
| Elemen | Standar |
|---|---|
| Loudness master | −14 LUFS integrated (normalisasi YouTube), true peak ≤ −1 dBTP |
| VO | jernih, de-essed, kompresi ringan. VO adalah elemen terkeras di mix |
| Music bed | −18 s/d −24 dB di bawah VO, dengan ducking otomatis saat VO bicara. Ganti mood per bab |
| SFX karakter | pop (muncul), whoosh (gerak cepat/transisi), boing/squash (jatuh), cha-ching (uang), stamp, crowd murmur |
| Sinkron | SFX impact tepat pada frame kontak (±1 frame) |
| Stinger | hit musik pendek untuk reveal angka/twist |
| Ambience | ruang (kantor, kota, alam) pelan, agar dunia tidak "kosong" |
| Hening | 6–12 frame hening sebelum reveal besar (kontras) |

Semua musik dan SFX wajib berlisensi (library berbayar/royalty-free terdokumentasi).

## 5. Segmen sponsor
**[Teramati]** Pada 3 video, posisi ≈25% berisi visual foto-realistis berbeda gaya (iklan tool AI). Standar Crayon Verse:
- Bumper masuk: tokoh/maskot "membuka" segmen (mis. menarik tirai) 1–2 detik.
- Materi sponsor dibingkai di dalam objek dunia cerita (TV, papan, ponsel), atau di-full-screen dengan label "Sponsored".
- Bumper keluar kembali ke scene cerita dengan match cut.
- Dengan begitu perubahan gaya terbaca sebagai keputusan, bukan glitch.

## 6. Struktur editing video (template 15 menit) [Rekomendasi, selaras pola OutlierKit]
| Bagian | Durasi | Isi |
|---|---|---|
| Hook | 0:00–0:30 | klaim/angka/kontras paling mengejutkan + pertanyaan |
| Setup | 0:30–2:30 | dunia "sebelum", tokoh utama |
| Mekanisme (ELI5) | 2:30–7:00 | cara kerja loophole/strategi dengan metafora |
| Skala/eskalasi | 7:00–10:30 | puncak kekayaan/kekuasaan (montase) |
| Konsekuensi | 10:30–13:30 | kejatuhan/penegakan/hasil |
| Pelajaran + penutup | 13:30–15:00 | 1 pelajaran sederhana + CTA ringan |
