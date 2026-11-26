# Workflow: Pre-production

Output akhir fase ini: **naskah final + VO, model sheet, BG key, storyboard, animatic terkunci, shot list lengkap.**
Gate: jangan masuk ke production sebelum animatic disetujui.

---

## 1. Brief dan pemilihan topik
**Input:** ide user, niche, durasi target.
**Langkah:**
1. Tulis logline satu kalimat: *"Bagaimana [tokoh/perusahaan/krisis] [melakukan hal mengejutkan], dijelaskan seperti untuk anak 5 tahun."*
2. Uji topik (minimal 3 dari 5 harus "ya"):
   - Topik sudah dikenal publik (pop-culture, berita, nama besar)?
   - Ada **satu mekanisme** yang bisa dijelaskan (loophole, strategi, cara kerja)?
   - Ada stakes besar (angka miliaran, kejatuhan, kekuasaan)?
   - Ada tokoh protagonis/antagonis yang jelas?
   - Bisa digambar dengan metafora konkret?
3. Pilih format judul (pola yang terbukti di audit: ELI5 unggul ±2,3× median likes):
   - `[Topik] Explained Like You're 5`
   - `How [Tokoh] Actually Built [X]`
   - `[Tokoh]: The First/Most [superlatif] (And How They Did It)`
   - `The [superlatif] [scam/company/crisis] Ever`
4. Sketsa konsep thumbnail sejak awal (wajah emosi + 1–3 kata + simbol).

**Output:** brief 1 halaman (format §7.1).

## 2. Riset dan naskah ELI5
1. Kumpulkan fakta dari minimal 3 sumber kredibel. Catat sumber setiap angka.
2. Struktur naskah (lihat `references/transition_and_editing.md` §6): Hook → Setup → Mekanisme → Skala → Konsekuensi → Pelajaran.
3. Aturan menulis ELI5:
   - Satu konsep per paragraf, satu metafora per konsep.
   - Ganti jargon dengan analogi sehari-hari ("short selling = meminjam mainan teman, menjualnya, berharap bisa membeli lagi lebih murah").
   - Kalimat pendek (≤ 20 kata). Angka dibulatkan dan dibandingkan dengan hal yang dikenal.
   - Tulis **[VISUAL: …]** di samping setiap kalimat sebagai ide gambar.
4. Target 130–150 kata per menit VO.
5. Fact-check, lalu kunci naskah (`naskah_final.md`).

## 3. Standar hook (0–30 detik) [Rekomendasi]
> Hook channel referensi tidak dapat diamati (lihat `references/crayon_capital_analysis.md` §1.3). Standar ini berasal dari praktik explainer dan retensi YouTube.

| Detik | Isi | Visual |
|---|---|---|
| 0–2 | Pernyataan/angka paling mengejutkan | CU tokoh utama dengan ekspresi kuat; pop-in angka |
| 2–5 | Kontras atau paradoks ("…tapi ia tidak pernah menjual apa pun") | Cut ke visual kontras (split-screen atau reaksi kerumunan) |
| 5–15 | Pertanyaan inti / curiosity gap | Maskot reaksi atau tokoh bingung + teks pertanyaan |
| 15–30 | Janji: apa yang akan dipahami penonton | Montase cepat 3–4 shot dari isi video (preview) |

Aturan hook:
- Frame pertama sudah berisi karakter dan emosi. Tidak ada logo/intro.
- Konteks dipahami dalam ≤ 5 detik (siapa + apa + kenapa penting).
- Visual hook harus selaras dengan thumbnail (penonton mengenali "janji" thumbnail).
- Cut setiap 1–2,5 detik di 15 detik pertama.

## 4. Script breakdown → shot list
1. Pecah naskah per kalimat atau frasa → 1 baris per shot (rata-rata 2,5–4 detik).
2. Untuk setiap shot tentukan: shot size, angle, kamera, karakter, aksi, ekspresi, teks layar, SFX, dan transisi (`references/cinematography_and_composition.md` §9).
3. Tandai **shot hero** (hook, reveal, klimaks): animasi penuh. Shot lain: animasi standar (moving hold + 1 aksi).
4. Buat breakdown aset: daftar tokoh, BG/lokasi (dengan hue), props, FX, dan teks.
5. Cek variasi: jangan ada lebih dari 3 shot berturut-turut dengan size + angle yang sama.

## 5. Design (karakter, lingkungan, props)
1. Daftar tokoh → kelas warna (hero/figuran/kerumunan) → Character Brief (`references/character_design_standards.md` §9).
2. Ambil dari bank aset dulu; desain baru hanya untuk tokoh atau props yang unik.
3. Model sheet untuk setiap tokoh hero (§6 di file tersebut).
4. BG key per lokasi: band warna, arah key light, overlay atmosfer (`references/lighting_and_color.md` §3).
5. Review dengan `checklists/character_consistency_checklist.md` §A.

## 6. Storyboard dan animatic
**Storyboard:**
- 1 panel per shot (tambah panel untuk aksi kompleks: key pose awal, ekstrem, akhir).
- Setiap panel memuat: Shot ID, framing, panah gerak karakter dan kamera, ekspresi, teks layar, catatan SFX.
- Uji keterbacaan: setiap panel harus "terbaca" tanpa teks VO.

**Animatic:**
1. Susun panel di timeline dengan VO final (atau scratch berkualitas).
2. Atur durasi panel mengikuti frasa VO; tambahkan panel antara untuk aksi.
3. Tambahkan gerak kamera kasar, teks layar placeholder, SFX kunci.
4. Review: pacing (lihat aturan 6–8 detik), kejelasan, variasi shot, hook.
5. **Kunci timing.** Setelah disetujui, durasi shot tidak berubah tanpa persetujuan director.

## 7. Format output

### 7.1 Konsep animasi (brief)
```markdown
# <Judul kerja>
- **Logline:** …
- **Format judul:** … (alternatif ×2)
- **Audiens & janji:** penonton akan memahami …
- **Durasi target:** __ menit (__ kata VO)
- **Struktur:** Hook (…) → Setup (…) → Mekanisme (…) → Skala (…) → Konsekuensi (…) → Pelajaran (…)
- **Metafora kunci:** 1) … 2) … 3) …
- **Tokoh:** [hero] …, [antagonis] …, [figuran] …, [maskot] …
- **Lokasi & hue:** kantor (biru netral), panggung (merah tua), …
- **Konsep thumbnail:** wajah …, teks "…", simbol …
- **Momen hero (animasi penuh):** 1) hook 2) reveal … 3) klimaks …
- **Risiko:** fakta sensitif / tokoh nyata / aset berlisensi …
```

### 7.2 Panel storyboard
```markdown
**SQ020_SH0030** | MS eye-level | 3s
[Gambar/deskripsi]: CEO di tengah balik meja, dua investor kepala putih di kiri-kanan menghadap kamera.
Aksi: CEO menyorongkan karung $ ke depan (arc) → investor mata sparkle.
Kamera: locked-off. Teks: "Guaranteed 20%!" (balon dari CEO). SFX: cha-ching.
Transisi: hard cut.
```

### 7.3 Shot list
| # | Shot ID | TC in | Dur | Size/Angle | Kamera | Karakter & aksi | Ekspresi | Teks layar | SFX/Musik | Transisi out |
|---|---|---|---|---|---|---|---|---|---|---|

Kolom wajib diisi lengkap. Gunakan "—" bila tidak ada.

## 8. Checklist keluar pre-production
- [ ] Naskah final terverifikasi, sumber tercatat
- [ ] VO final terekam (−14 LUFS master target)
- [ ] Semua tokoh hero punya model sheet lengkap
- [ ] Semua lokasi punya BG key + hue + arah cahaya
- [ ] Storyboard lengkap; setiap kalimat VO punya visual
- [ ] Animatic disetujui; timing terkunci
- [ ] Shot list lengkap; breakdown aset selesai
- [ ] Thumbnail konsep disetujui
