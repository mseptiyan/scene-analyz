# Animation Fundamentals: 12 Prinsip untuk Crayon Verse

**Sumber utama:** Frank Thomas & Ollie Johnston, *The Illusion of Life: Disney Animation* (1981). Pendukung: Richard Williams, *The Animator's Survival Kit* (2001); Preston Blair, *Cartoon Animation* (1994); ringkasan Adobe Creative Cloud "Principles of animation", StudioBinder "12 principles of animation", NYFA. Contoh dan angka spesifik di file ini adalah **[Rekomendasi]** untuk gaya Crayon Verse, kecuali diberi label lain.

Prinsip-prinsip ini awalnya untuk animasi tangan, tetapi tetap berlaku di animasi digital dan rig. Tujuannya membuat karakter terasa tunduk pada hukum fisika dan punya emosi.

> **Catatan gaya.** Karakter Crayon Verse sangat sederhana (lingkaran + bean + garis). Kesederhanaan ini membuat setiap prinsip **lebih** terlihat, bukan kurang. Kesalahan timing yang tersamarkan pada karakter detail akan sangat mencolok di sini.

---

## 1. Squash and Stretch
**Definisi:** perubahan bentuk untuk memberi kesan berat dan elastisitas, dengan **volume konstan**.
**Penerapan:**
- Badan bean: saat mendarat atau jatuh, squash ke lebar 110–120% dan tinggi 85–90% selama 2–3 frame, lalu stretch 105% saat memantul, lalu settle.
- Kepala lingkaran: squash hanya untuk impact ekstrem (dipukul, jatuh). Untuk akting biasa kepala **tetap bulat sempurna**, karena kepala bulat adalah identitas gaya.
- Objek props (koin, karung uang): squash saat jatuh di meja.
**Larangan:** mengubah volume (squash tanpa melebar), atau stretch pada wajah saat dialog normal.

## 2. Anticipation
**Definisi:** gerak persiapan berlawanan arah sebelum aksi utama, agar penonton siap.
**Penerapan:**
- Lari: badan condong ke belakang 2–4 frame, lalu lari.
- Kaget (*take*): kepala turun sedikit dan mata menyipit (3–4f) → mata melebar dan alis naik (pose ekstrem, tahan 2f) → settle (6–10f).
- Pop-in objek: skala 100→90% (2f) sebelum masuk ke 110% → 100%. Untuk teks bisa dilewati.
**Proporsi:** semakin besar aksi, semakin panjang antisipasinya (aturan Williams).

## 3. Staging
**Definisi:** penyajian ide sehingga tidak bisa disalahpahami. Satu ide per momen.
**Penerapan (paling penting untuk explainer):**
- Setiap shot harus terbaca dalam ≤1 detik tanpa suara. Uji dengan **silhouette test**: isi semua karakter hitam; aksi harus tetap terbaca.
- Hanya tokoh yang sedang "berbicara" atau dirujuk narasi yang bergerak signifikan. Yang lain melakukan *moving hold*.
- Karakter frontal atau ¾ menghadap kamera (gaya lineup). Hindari profil penuh kecuali ada dua karakter yang berhadapan.
- Pakai warna (berwarna vs abu), cahaya (spotlight), dan posisi (tengah/sepertiga) untuk menunjuk subjek.

## 4. Straight Ahead vs Pose to Pose
- **Pose to pose** (key → breakdown → in-between) untuk semua akting karakter rig. Ini memungkinkan kontrol timing terhadap VO.
- **Straight ahead** untuk efek yang chaotic: api, asap, confetti (atau partikel), air, rambut tertiup.
- Alur: key pose (storytelling) → extremes → breakdown (menentukan arc dan karakter gerak) → in-between/spline.

## 5. Follow Through and Overlapping Action
**Definisi:** bagian tubuh atau aksesori berhenti pada waktu berbeda. Bagian yang lepas terus bergerak setelah tubuh utama berhenti.
**Penerapan:** dasi, rambut panjang, ekor jas, rok, kertas di tangan, topi. Offset 2–4 frame dari gerak badan, overshoot lalu settle dalam 6–12 frame.
**Bukti referensi:** dasi berkibar saat tokoh jatuh (Great Depression ≈8:14) **[Teramati]**.

## 6. Slow In and Slow Out (Easing)
**Definisi:** lebih banyak drawing atau frame di dekat key pose, sehingga gerak mempercepat dan memperlambat.
**Penerapan:**
- Default easing untuk karakter: ease-in-out (kurva bezier ±33%/33%).
- Untuk pop-in grafis: ease-out kuat (cepat masuk, pelan berhenti) + overshoot.
- Kamera: ease-in-out untuk gerak bermakna (push-in penekanan, whip, zoom transisi). **Drift zoom lambat** (2–8%/dtk) di sepanjang shot dibuat **kecepatan konstan**, sesuai pengukuran video referensi (rasio kecepatan awal/tengah/akhir 0,92/1/0,91).
- *Spacing chart* wajib ditulis di blocking untuk aksi penting.

**Cara menulis spacing chart (notasi Williams):**
```
Key A ─┬──┬───┬────┬──────┬────────┬─ Key B        (slow out dari A, cepat di tengah, slow in ke B)
       1  3   5    7      9       11

Key A ─┬────────┬──────┬────┬───┬──┬─ Key B        (fast out, slow in: pop-in objek / lemparan mendarat)
       1        3      5    7   9  11
```
- Angka = nomor frame (on twos: 1, 3, 5…). Jarak antar tick = jarak tempuh per drawing.
- **Breakdown** ditempatkan di tengah *waktu*, tapi tidak harus di tengah *jarak*. Posisinya menentukan karakter gerak: dekat A = berat atau lambat mulai, dekat B = cepat lalu mengerem.
- Rasio praktis: *ease* ringan = in-between ⅓–½; *ease* kuat = ¼–⅛ (Williams: "favor the key").
- Di software rig, spacing = bentuk kurva di graph editor. Cocokkan: tick rapat = kurva landai, tick renggang = kurva curam.
- Tulis chart di catatan shot untuk aksi hero (take, jatuh, lempar, pop-in angka besar).

## 7. Arcs
**Definisi:** gerak alami mengikuti lintasan melengkung.
**Penerapan:** ujung lengan-garis saat melambai, lintasan kepala saat menoleh atau mengangguk, lintasan koin yang dilempar (parabola). Periksa dengan *onion skin* atau trail: titik ujung tangan harus membentuk busur halus tanpa patah.

## 8. Secondary Action
**Definisi:** aksi tambahan yang memperkaya aksi utama **tanpa mengalihkan perhatian**.
**Penerapan:** tetes keringat saat gugup, kedip saat berpikir, jari mengetuk meja, confetti setelah sukses, asap cerutu. Secondary action berjalan *setelah* atau *di bawah* aksi utama, jangan bersamaan dengan puncak aksi utama.

## 9. Timing
**Definisi:** jumlah frame untuk suatu aksi, yang menentukan berat, mood, dan kejelasan.
**Tabel timing Crayon Verse (24 fps):**
| Aksi | Frame | Catatan |
|---|---|---|
| Kedip | 4–6 (tutup 2, buka 2–4) | interval 2–5 detik, jangan sinkron antarkarakter |
| Toleh kepala | 6–10 | dengan antisipasi kecil |
| Kaget (take) | 3–4 antisipasi + 2 ekstrem + 6–10 settle | ditambah garis `!!` |
| Langkah jalan | 12 per langkah (on twos) | badan naik-turun 3–5 px |
| Langkah lari | 6–8 per langkah | ditambah smear/multiples 1–2f |
| Pop-in objek | 6–8 | overshoot 105–110% |
| Teks dialog muncul | 4–6 (fade/typewriter/scale) | hold min. 1 detik per 3 kata |
| Hold baca (shot) | min. 1,5 detik | atau durasi frasa VO |
| Camera push-in emphasis | 72–144 (3–6 detik) | skala 100→105–110% |
| Camera shake impact | 4–8 | amplitudo 6–12 px, decay |

## 10. Exaggeration
**Definisi:** dorong pose, ekspresi, dan aksi melampaui realisme demi kejelasan dan humor.
**Penerapan:** mata sparkle saat melihat uang, rambut berdiri saat panik, rahang jatuh, mulut kotak saat berteriak, gigi kertak saat takut, badan gemetar dengan garis getar. Exaggeration **disesuaikan dengan konteks**: skandal atau tragedi nyata (perang, perbudakan) memakai exaggeration yang lebih kecil dan ekspresi lebih tenang dan serius.

## 11. Solid Drawing
**Definisi:** bentuk punya volume, berat, dan keseimbangan yang meyakinkan.
**Penerapan:**
- Lingkaran kepala harus benar-benar bulat (pakai shape tool, bukan freehand).
- Ketebalan outline konsisten (lihat `character_design_standards.md`).
- Props dan latar memakai perspektif yang benar (1 atau 2 titik hilang). Meja dan gedung pada referensi memakai perspektif sederhana yang konsisten **[Teramati]**.
- Bayangan kontak (elips) di bawah kaki agar karakter "menapak".

## 12. Appeal
**Definisi:** karakter menarik untuk ditonton, baik pahlawan maupun penjahat.
**Penerapan:** bentuk sederhana dan bulat, kontras ukuran (kepala besar, tungkai tipis), wajah minimal yang tetap jelas emosinya, satu ciri khas per tokoh. Penjahat dibuat "menarik dibenci" lewat seringai dan alis tajam, bukan lewat desain yang menjijikkan.

---

## Kombinasi prinsip yang paling sering dipakai
| Momen naratif | Kombinasi |
|---|---|
| Tokoh diperkenalkan | Staging (tengah/spotlight) + appeal + pop-in dengan anticipation & overshoot |
| Angka besar diungkap | Anticipation (hening ½ detik) + pop-in angka + exaggeration reaksi + secondary (koin/confetti) |
| Kejatuhan/krisis | Squash/stretch + smear + follow-through (dasi/kertas) + camera shake |
| Dialog | Staging (1 pembicara bergerak), timing sinkron VO, secondary (kedip/alis) |
| Montase waktu | Timing cepat (hold pendek), match cut, arcs pada transisi |
