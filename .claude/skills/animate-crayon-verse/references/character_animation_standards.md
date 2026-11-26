# Character Animation Standards: Crayon Verse

Kanvas 1920×1080, **24 fps**. Label: [Teramati] / [Inferensi] / [Standar industri] / [Rekomendasi].

---

## 1. Teknik produksi yang direkomendasikan

| Kebutuhan | Teknik | Tools contoh |
|---|---|---|
| Badan, kepala, posisi | Rig cut-out (bone/parenting) | Moho Pro, Toon Boom Harmony, After Effects + Duik Angela |
| Lengan & kaki garis | Rubber-hose (path dengan 2–3 titik, panjang dijaga) | AE Rubberhose 3, Moho smart bones, Harmony deformer |
| Mata, alis, mulut | Swap drawing (switch layer / drawing substitution) | Moho Switch Layer, Harmony drawing substitution |
| Aksi cepat (lari, jatuh, ayunan) | Smear/multiples digambar 1–2 frame | frame-by-frame di atas rig |
| Efek (asap, api, confetti) | Straight-ahead atau partikel | AE (CC Particle World/Trapcode), Harmony FX |

**[Inferensi]** Referensi kemungkinan memakai rig + rubber-hose: bentuk identik antar-shot, tungkai garis yang menekuk mulus, multiples pada lari (Wolf ≈8:16), motion blur komposit (Great Depression ≈8:14). Tool pastinya tidak dapat diverifikasi.

## 2. Frame rate dan exposure
- Akting karakter **on twos** (setiap pose ditahan 2 frame). Hasilnya rasa "kartun" dan hemat.
- **On ones** untuk: gerak kamera, pop-in grafis, aksi sangat cepat, partikel.
- Jangan mencampur on ones dan on twos *pada karakter yang sama di shot yang sama*, kecuali untuk aksi cepat yang disengaja.
- Rig yang interpolasinya halus tetap bisa di-*step* ke on twos (Moho "step", AE posterize time 12) agar konsisten dengan gaya.

## 3. Moving hold (anti "karakter mati")
Setiap karakter yang terlihat dan tidak beraksi wajib punya:
| Elemen | Nilai |
|---|---|
| Napas | skala Y badan 100→101,5% → 100, siklus 48–72 frame, offset acak antarkarakter |
| Kedip | 4–6 frame, interval acak 48–120 frame |
| Mikro-alis | geser 1–2 frame setiap 3–6 detik bila karakter mendengarkan |
| Kerumunan | minimal kedip + napas. Boleh 30% kerumunan berupa still bila di latar jauh |

## 4. Kosakata gerak inti

### 4.1 Jalan (on twos, 12 frame per langkah)
- Kontak (f1) → down (f3–4, badan turun 3–5 px) → passing (f7, badan naik) → up → kontak berikut.
- Kaki garis: kaki depan lurus saat kontak, kaki yang melangkah melengkung saat passing.
- Lengan garis berayun berlawanan dengan kaki, mengikuti arc, offset 1–2 frame (overlap).
- Kepala sedikit tertinggal (overlap 1–2 frame) dari naik-turun badan.

### 4.2 Lari (6–8 frame per langkah)
- Badan condong 10–15° ke depan.
- Fase melayang 1–2 frame dengan **multiples/smear** kaki (3–4 garis kaki tumpang) + speed lines horizontal. [Teramati: Wolf ≈8:16]
- Debu atau asap kecil saat mulai (antisipasi) dan berhenti.

### 4.3 Take (kaget)
1. Antisipasi: kepala turun 5–10 px, mata menyipit (3–4f).
2. Ekstrem: kepala naik, alis naik tinggi, mata sparkle/titik, mulut "O"/kotak (2f), ditambah garis `!!` atau rambut berdiri.
3. Settle: overshoot kecil lalu tahan pose kaget (6–10f + hold sesuai VO).

### 4.4 Jatuh / kalah
Squash badan saat menghantam, smear atau motion blur ringan saat jatuh, follow-through dasi atau kertas, retakan lantai sebagai FX, lalu camera shake 4–8f. **Batasi motion blur pada area wajah** (lihat QC #1 di `crayon_capital_analysis.md`).

### 4.5 Menunjuk / presentasi
Lengan garis terangkat dengan arc (6–8f), overshoot 1 frame, tahan. Objek yang ditunjuk melakukan pop-in atau highlight saat lengan mencapai ekstrem.

### 4.6 Memegang objek
Objek di-*parent* ke ujung lengan. Tambahkan mitten atau tangan sederhana saat memegang benda penting (uang, telepon, gelas). Tangan tidak boleh menembus objek; urutan layer: tangan di depan objek di sisi kamera.

## 5. Lip sync dan dialog

**[Teramati]** Dialog di referensi sering disajikan sebagai **teks tulisan tangan di dekat tokoh**, dengan mulut berbentuk ekspresi (bukan bentuk fonem). Narasi utama adalah VO narator yang tidak tampil.

**Standar Crayon Verse [Rekomendasi]:**
| Situasi | Perlakuan mulut |
|---|---|
| Narator VO (tokoh tidak bicara) | Mulut ekspresi, moving hold |
| Dialog pendek dengan teks layar | Flap sederhana 3 bentuk (tutup, setengah, buka) on twos selama teks muncul |
| Dialog tokoh penting tanpa teks layar | Mouth chart 6–9 bentuk, versi sederhana Preston Blair: **MBP, AI, E, O, U, FV, L, WQ, rest** |

Aturan lip sync [Standar industri]:
- Bentuk mulut mendahului suara 1–2 frame (bunyi terdengar sedikit setelah bentuk terlihat).
- Jangan animasikan setiap huruf; pertahankan bentuk vokal dominan dan konsonan bibir (M/B/P, F/V).
- Tutup mulut pada jeda lebih dari 6 frame.
- Penamaan layer mengikuti konvensi Preston Blair bila memakai auto lip-sync (mis. Rhubarb/Moho/Papagayo), karena tool tersebut mencocokkan nama layer.

## 6. Akting dan kepribadian lewat gerak
| Tipe tokoh | Tempo | Pose khas |
|---|---|---|
| Tycoon/penipu percaya diri | lambat, hold panjang | dada membusung, tangan terlipat, alis datar, senyum tipis |
| Korban/orang biasa | cepat, gelisah | bahu turun, kedip sering, keringat |
| Otoritas (regulator, polisi) | kaku, minim gerak | frontal, simetris |
| Jenius/inovator | burst cepat lalu diam | menunjuk, mata berbinar |
| Kerumunan | sinkron tapi offset | sorak dengan lengan naik bergantian |

## 7. Timing terhadap narasi
- **Kata kunci VO = frame aksi.** Ekstrem aksi atau pop-in jatuh 0–2 frame sebelum kata kunci terdengar.
- **Angka besar:** jeda visual 6–12 frame sebelum angka muncul (efek *beat*).
- **Akhir kalimat:** karakter mencapai pose akhir lalu tahan minimal 12 frame sebelum cut.
- **Lelucon visual:** setup di kalimat → punchline visual di jeda setelah kalimat.

## 8. Format Animation Direction per shot (output standar)

```markdown
### SQ010_SH0040 (00:01:12:05 – 00:01:16:10, 4s 05f)
- **VO:** "...and in just three years, his firm was worth **$100 million**."
- **Staging:** MS frontal, tokoh tengah di balik meja; uang di sepertiga bawah.
- **Key poses:**
  1. f0: netral, tangan di meja (moving hold)
  2. f30: antisipasi—tubuh turun 6px, mata menyipit
  3. f34: TAKE—mata sparkle, mulut "O", alis naik (kata "$100 million")
  4. f44–100: hold take + napas cepat
- **Secondary:** tumpukan uang pop-in on ones f32–40 (overshoot 108%), koin jatuh straight-ahead.
- **Timing:** akting on twos; uang & koin on ones.
- **Kamera:** push-in 100→106% f30–100 ease-in-out.
- **Teks layar:** "$100,000,000" handwritten, pop f34, hold sampai cut.
- **SFX:** whoosh (f30), cash register "cha-ching" (f34), koin berdenting (f36–60).
- **Transisi keluar:** hard cut on beat ke SH0050.
- **QC fokus:** volume squash, overshoot uang tidak menembus meja, outline konsisten saat push-in.
```
