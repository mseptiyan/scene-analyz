# Character Design Standards: Crayon Verse

Label: **[Teramati]** = terlihat di referensi Crayon Capital, **[Standar industri]**, **[Rekomendasi]** = keputusan skill ini.
Ukuran piksel mengacu pada kanvas **1920×1080**.

> **Orisinalitas.** Aturan di bawah adalah *sistem bentuk*. Setiap proyek wajib membuat tokoh, maskot, dan palet sendiri. Jangan mereplikasi tokoh tertentu dari channel referensi, termasuk maskot berkacamata dengan dasi kupu-kupu merah.

---

## 1. Anatomi dasar

```
          ┌───────────┐
         ╱             ╲        KEPALA: lingkaran sempurna
        │   ◖‿   ‿◗     │        Ø = 28–32% tinggi total
        │    ●     ●     │        mata di garis tengah horizontal
        │       ▬        │        mulut ±70% ke bawah
         ╲             ╱
          └─────┬─────┘          tanpa leher
           ╭────┴────╮
          │  ╲  ▼  ╱  │          BADAN BEAN = pakaian
     ────╯│   │ ▼ │   │╰────     lebar 0,9–1,1 × Ø kepala
  (lengan)│   │   │   │(lengan)  tinggi 35–40% total
          │   ╰───╯   │          lengan = 1 garis dari sisi badan
           ╰────┬────╯
              │   │              KAKI: 2 garis, ±30% tinggi
              │   │
             ─┘   └─             telapak opsional
```

| Bagian | Spesifikasi | Label |
|---|---|---|
| Tinggi total | 3–3,5 × diameter kepala | [Teramati, estimasi visual] |
| Kepala | Lingkaran sempurna. Boleh oval **hanya** untuk karikatur yang disengaja | [Teramati] |
| Leher | Tidak ada. Badan menempel di bawah kepala, sedikit tertutup kepala | [Teramati] |
| Badan | Bean/telur, bagian bawah membulat | [Teramati] |
| Lengan | Garis tunggal, tebal = outline, lentur seperti selang (rubber-hose) | [Teramati] |
| Tangan | Default tanpa tangan. Close-up/pegang objek: mitten oval putih atau 4 jari sederhana | [Teramati] |
| Kaki | 2 garis lurus, jarak ±40% lebar badan, berdiri tegak | [Teramati] |
| Varian anak | Tinggi 2,5 × Ø kepala, kepala 0,8× dewasa | [Rekomendasi] |
| Varian gemuk | Badan bean 1,4–1,6× lebar | [Teramati: tokoh gemuk di Ozempic] |

## 2. Wajah dan ekspresi

### 2.1 Komponen
| Komponen | Default | Variasi |
|---|---|---|
| Mata | Oval vertikal hitam, tinggi ±9% Ø kepala, jarak antar-pusat ±30% Ø | sparkle (2 titik putih), `> <` (meringis), garis (tidur/puas), titik kecil (shock), lingkaran besar + pupil kecil (panik) |
| Alis | Stroke melengkung pendek, ±20% Ø, mengambang ±6% Ø di atas mata | naik (kaget/sedih), turun-dalam (marah), satu naik (curiga), miring keluar (khawatir) |
| Mulut | Garis pendek ±12% Ø | "O", senyum lengkung, seringai lebar dengan gigi, kotak teriak, gigi kertak, gelombang (mual/gugup) |
| Interior mulut | Merah tua `#7A1E25`-ish + gigi atas putih | lidah opsional `#C4505A` |
| Pipi | Tidak ada, kecuali blush (malu/mabuk) | — |
| Keringat | Tetes biru muda ber-outline di sisi kepala | 1–3 tetes |

### 2.2 Library ekspresi minimum (wajib dibuat per tokoh utama)
1. Netral
2. Senang/puas
3. Tertawa
4. Kaget ringan
5. Shock (mata sparkle/titik, mulut "O" besar)
6. Marah
7. Sedih
8. Khawatir/gugup (+keringat)
9. Takut (gigi kertak)
10. Licik/seringai (penjahat)
11. Berpikir (mata ke atas, mulut miring)
12. Teriak (mulut kotak)

Setiap ekspresi = kombinasi **alis + mata + mulut** dari bank swap. Alis adalah pembeda utama; uji tiap ekspresi dengan menutup mulut, karena alis + mata saja harus tetap terbaca.

## 3. Outline dan shading

| Elemen | Spesifikasi |
|---|---|
| Warna outline | `#1A1617` (hampir hitam, hangat). **Bukan** `#000000` murni [Teramati: sampel #171415, #18131C] |
| Tebal outline karakter | 8–10 px di 1080p [Teramati: median 5–6 px di 720p] |
| Tebal tungkai (garis lengan/kaki) | sama dengan outline atau +1–2 px |
| Tebal outline props | 6–8 px |
| Tebal outline BG jauh | 3–5 px atau tanpa outline + desaturasi |
| Ujung garis | round cap & round join |
| Fill | flat, tanpa gradien |
| Shadow | 1 tone, bentuk sabit keras di sisi yang jauh dari key light, lebar 15–25% Ø kepala |
| Warna shadow | fill × 0,75–0,85 kecerahan, hue bergeser 5–15° ke biru/ungu |
| Highlight rambut | 1 band terang (fill × 1,15) di sisi cahaya |
| Rim/bounce | opsional, warna sumber cahaya, lebar 3–6 px di tepi kepala |
| Bayangan kontak | elips hitam 25–40% opacity, blur 4–8 px, di bawah kaki |

## 4. Kelas karakter dan warna

| Kelas | Kulit kepala | Pakaian | Saturasi | Fungsi |
|---|---|---|---|---|
| **Hero/tokoh bernama** | Warna kulit sesuai tokoh (mis. `#F0D2AF` terang, `#C68E62` sedang, `#8A5A3C` gelap) | warna khas | penuh | fokus cerita |
| **Figuran aktif** | Putih `#FDFDFD` + shadow `#C8C8CC` | warna sesuai peran | sedang | reaksi/dialog |
| **Kerumunan** | Abu `#BDBDBD`–`#8C8C8C` | abu | 0–30% | konteks |
| **Siluet/misteri** | Hitam/abu gelap | — | 0% | rahasia, ancaman |
| **Maskot reaksi** (milik sendiri) | Desain unik | 1 aksen warna signature | penuh | brand anchor di hook & thumbnail |

**Aturan:** dalam satu shot, maksimal **2–3 tokoh berwarna penuh**. Sisanya putih atau abu.

## 5. Identitas tokoh (siluet + props)

Tokoh nyata dan historis dikenali lewat **2 elemen saja**:
1. **Siluet kepala:** gaya rambut, kebotakan, topi, sorban, helm.
2. **1 props/aksen:** kacamata, kumis/janggut, warna jas/dasi, lencana, seragam.

Tes: tutup semua kecuali siluet hitam kepala + badan. Tokoh harus bisa dibedakan dari tokoh lain di video yang sama. Untuk tokoh publik nyata, gunakan karikatur *ringan* (ciri khas umum seperti rambut atau kacamata). Hindari penghinaan fisik, dan jangan memakai foto.

## 6. Model sheet (deliverable wajib per tokoh utama)

Isi minimal:
1. **Turnaround:** depan, ¾ depan, samping, ¾ belakang, belakang. Wajah bergeser ke arah hadap; badan bean tetap. [Standar industri]
2. **Construction sheet:** lingkaran kepala + guide garis tengah, proporsi dengan garis bantu tinggi.
3. **Color callout:** HEX untuk kulit, rambut (base/shadow/highlight), pakaian (base/shadow), aksen.
4. **Expression sheet:** 12 ekspresi (§2.2).
5. **Mouth chart:** 6–9 bentuk (lihat `character_animation_standards.md` §5).
6. **Pose sheet:** berdiri, duduk, jalan (kontak dan passing), lari (smear), menunjuk, memegang objek, kaget.
7. **Do/Don't:** contoh off-model yang dilarang.
8. **Ukuran relatif:** tokoh berdampingan dengan tokoh lain dan props standar (meja, pintu).

## 7. Konsistensi lintas shot (aturan keras)

- Diameter kepala tokoh yang sama, pada jarak kamera yang sama, tidak boleh bergeser lebih dari ±3%.
- Warna HEX harus identik, kecuali dimodifikasi oleh lighting pass terdokumentasi.
- Props identitas (kacamata, kumis) **tidak boleh hilang**, kecuali sebagai bagian dari cerita.
- Ketebalan outline tetap sama walau skala karakter berubah. Untuk zoom/scale di compositing, kompensasi stroke atau render ulang pada resolusi yang sesuai.
- Thumbnail boleh memakai render premium (tangan berjari, tekstur, lighting volumetrik), tapi siluet, warna, dan props harus sama dengan model di video. [Teramati: Wolf thumbnail vs isi]

## 8. Panduan untuk generator gambar AI

1. Selalu sertakan **model sheet** sebagai referensi gambar bila tool mendukung.
2. Kunci kata-kata wajib di prompt: `perfectly round head`, `bean-shaped body`, `single line limbs`, `no neck`, `thick uniform dark outline`, `flat colors`, `one hard cel shadow`.
3. Larangan negatif: `no gradients on characters, no realistic hands, no nose, no detailed anatomy, no thin sketchy lines`.
4. Periksa hasil dengan `checklists/character_consistency_checklist.md`. Masalah tersering: jumlah jari, outline menipis, kepala oval, munculnya leher, dan warna kulit bergeser.

## 9. Format Character Design Brief (output standar)

```markdown
## Character Brief: <NAMA>
- **Peran naratif:** (protagonis / antagonis / figuran / maskot) + fungsi di cerita
- **Kelas warna:** hero / figuran / kerumunan
- **Siluet kepala:** <rambut/topi/kebotakan>
- **Props identitas:** <1–2 item>
- **Palet:** kulit #____ (shadow #____), rambut #____/#____/#____, pakaian #____ (shadow #____), aksen #____
- **Proporsi:** tinggi __ × Ø kepala; badan lebar __ × Ø
- **Kepribadian visual:** 3 kata sifat → bagaimana tampil di pose & gerak
- **Ekspresi khas:** (2–3 dari library) + kapan dipakai
- **Gaya gerak:** (tempo, berat, kebiasaan: mis. "selalu merapikan dasi")
- **Do / Don't:** …
- **Kebutuhan model sheet:** turnaround ✓ ekspresi ✓ mouth chart ✓ pose ✓
```
