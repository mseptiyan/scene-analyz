# Lighting & Color: Crayon Verse

Data terukur dari 108 frame referensi ada di `crayon_capital_analysis.md` §3.2 dan §3.6. Palet di bawah adalah **palet orisinal Crayon Verse** [Rekomendasi]. Nilai-nilainya dikalibrasi agar *mirip secara fungsi* (nilai, saturasi) dengan referensi, tetapi bukan salinan identitas warna channel referensi.

---

## 1. Prinsip
1. **Flat + satu shadow.** Karakter dan props memakai fill datar, satu tone shadow keras, dan opsional satu highlight/rim. Cahaya "realistis" dibangun di *latar* dan *overlay*, bukan di karakter.
2. **Satu key light per scene, arah konsisten.** Semua shadow sabit di scene menghadap sisi yang sama.
3. **Hue lokasi = orientasi + mood.** Setiap lokasi punya satu hue dominan yang konsisten setiap kali kembali ke lokasi itu.
4. **Karakter putih harus "pop".** Latar di rentang nilai menengah (luminance 0,35–0,65) agar kepala putih dan outline gelap terbaca. [Teramati: luminance median 0,50]
5. **Saturasi terkendali.** Saturasi median frame 0,25–0,35. Aksen jenuh (uang hijau, grafik merah, emas) dipakai hemat untuk menunjuk informasi. [Teramati: 0,26–0,32]

## 2. Token warna dasar [Rekomendasi]

| Token | HEX | Pemakaian |
|---|---|---|
| `ink` | `#1A1617` | outline, tungkai, mata |
| `paper` | `#FDFDFB` | kepala figuran, balon teks |
| `paper-shade` | `#C9CAD0` | shadow kepala putih |
| `crowd` | `#A9A9AD` | kerumunan |
| `skin-1` / shade | `#F2D3B0` / `#D9AE8A` | kulit terang |
| `skin-2` / shade | `#C98F63` / `#A8704A` | kulit sedang |
| `skin-3` / shade | `#8C5B3E` / `#6E432C` | kulit gelap |
| `money` | `#4FAE5A` (shade `#2F7C3B`) | uang, profit, naik |
| `loss` | `#D9363E` | grafik turun, bahaya, stempel |
| `gold` | `#F2B630` (shade `#C98A12`) | emas, kekayaan, highlight judul |
| `mouth` | `#7A1E25` | interior mulut |
| `sweat` | `#9ED8F0` | keringat, air mata |
| `text-stroke` | `#1A1617` | stroke teks dialog putih |

## 3. Hue lokasi (mood map)

| Lokasi/mood | Band latar (gelap → terang) | Key light | Aksen |
|---|---|---|---|
| Kantor/edukatif netral | `#3F8FB5` → `#5BAAC8` → `#86C3D6` | putih dari atas-kiri | money/gold |
| Ruang direksi malam | `#1F2A3F` → `#2C3A55` + jendela `#E8C66A` | sorotan diagonal 15% putih | gold |
| Panggung/glamor | `#4A1012` → `#5E1E1D` → `#8C2A27` | 2 spotlight kerucut 20% | confetti multi |
| Krisis/skandal | `#2A2A2C` → `#3E3E40` → `#58585B` | top-light keras | loss |
| Kekayaan/kerajaan | `#B8860B` → `#E0A82E` → `#F5CF6B` | hangat, glow | gold |
| Sejarah/padang | `#C9B98A` → `#DCCFA4` + langit `#BFE0EA` | matahari kuning | — |
| Teknologi/data | `#0F2233` → `#16344A` + glow `#3FD0E0` | rim cyan | money/loss |
| Perang/militer | `#5C6B3A` → `#7D8A55`, langit `#A9C9D6` | siang datar | loss |

Aturan: lokasi yang sama selalu kembali ke band yang sama. Lompatan waktu (siang → malam) harus dimotivasi naratif.

## 4. Resep shading karakter
1. **Shadow sabit:** duplikat bentuk kepala, geser 15–25% Ø menjauhi key light, *intersect* dengan kepala, lalu isi dengan warna shade.
2. **Rambut:** base + shade (sisi bawah/belakang) + 1 band highlight.
3. **Badan bean:** shade di sisi yang sama dengan kepala, 20–30% lebar badan.
4. **Rim berwarna (opsional):** stroke dalam 3–6 px warna sumber cahaya di sisi berlawanan dengan shadow. [Teramati: rim biru dari jendela di Palantir ≈7:40]
5. **Color cast lingkungan:** untuk adegan dengan cahaya berwarna kuat (lampu hijau, api), tambahkan layer *multiply/overlay* 15–35% warna sumber di atas karakter. [Teramati: wajah hijau di Petrodollar ≈8:30]

## 5. Cahaya atmosferik (overlay)
| Efek | Cara | Opacity |
|---|---|---|
| Sorotan jendela/searchlight | poligon diagonal putih, blend *add/screen*, ujung blur | 10–20% |
| Spotlight panggung | kerucut dari atas, blur tepi 20–40 px | 15–25% |
| Glow objek (emas, layar, lilin) | lingkaran radial blur, *screen* | 30–60% |
| Vignette | radial gelap di tepi | 10–25% |
| Depth blur latar | Gaussian 4–12 px pada layer BG jauh/FG | — |
| Desaturasi kerumunan | saturasi -60 s/d -100% | — |

## 6. Color grading per sekuens
- Grade di tingkat sekuens, bukan per shot, agar kontinu.
- Flashback/sejarah jauh: tambahkan *warm sepia overlay* 10–15% atau desaturasi 20%.
- Krisis: turunkan saturasi 15–25% dan naikkan kontras.
- Akhir positif: naikkan nilai dan saturasi sedikit (+5–10%).
- Target luminance median per frame 0,40–0,55. Hindari frame dengan luminance median < 0,25 lebih dari 3 detik, kecuali disengaja (misteri).

## 7. Aksesibilitas warna
- Jangan hanya mengandalkan merah vs hijau untuk naik/turun. Selalu sertakan arah panah dan label teks.
- Kontras teks dialog: putih + stroke gelap 3–5 px. Rasio kontras ≥ 4,5:1 terhadap latar lokal.
