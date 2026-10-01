# Practical Statistics for Data Scientists

Reproduksi kode dan pembahasan Chapter 1-4 buku **Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python**, edisi kedua, karya Peter Bruce, Andrew Bruce, dan Peter Gedeck (O'Reilly, 2020).

## Identitas

| Keterangan | Isi |
| --- | --- |
| Nama | `GHAVIND AZZARYA` |
| NIM | `101032300012` |
| Kelas | `TK-47-03` |
| Mata kuliah | `PEMBELAJARAN MESIN` |

## Tujuan

Mempelajari dasar statistik untuk data science melalui reproduksi contoh kode, penjelasan teori, dan interpretasi hasil. Setiap notebook berisi konsep dalam bahasa Indonesia, kode Python, output dan grafik, pemeriksaan konsistensi, ringkasan, serta pembahasan hasil.

Kode dasar diadaptasi dari notebook penulis. Atribusi sumber dan perubahan dari contoh asli dicantumkan agar asal kode dapat ditelusuri.

## Materi

| Bab | Notebook | Pembahasan |
| --- | --- | --- |
| 1 | [Exploratory Data Analysis](notebooks/chapter_01_exploratory_data_analysis.ipynb) | Jenis data; mean, median, trimmed mean, dan pembobotan; SD, IQR, dan MAD; persentil; distribusi; korelasi; tabel kontingensi; visualisasi multivariat; mode, expected value, dan probability; struktur non-tabular. |
| 2 | [Data and Sampling Distributions](notebooks/chapter_02_data_and_sampling_distributions.ipynb) | Sampling bias; distribusi sampling; central limit theorem; standard error; bootstrap; confidence interval; QQ-plot; binomial, Poisson, eksponensial, dan Weibull; distribusi t, chi-square, F; estimasi failure rate. |
| 3 | [Statistical Experiments and Significance Testing](notebooks/chapter_03_statistical_experiments_and_significance_testing.ipynb) | Desain A/B; hipotesis; permutation test; p-value; Welch t-test; ANOVA; chi-square; Fisher exact; multiple testing; power; ukuran sampel; multi-arm bandit (epsilon-greedy dan Thompson sampling). |
| 4 | [Regression and Prediction](notebooks/chapter_04_regression_and_prediction.ipynb) | Regresi sederhana dan berganda; residual; RMSE dan R2; AIC dan stepwise; weighted regression; dummy variables; confounding dan interaksi; diagnostics; polynomial, spline, GAM; faktor ordinal; confidence/prediction intervals; holdout dan cross-validation. |

Pemetaan **119 topik/subtopik dan ringkasan** dari daftar isi buku ke notebook tersedia pada [Cakupan Materi](docs/CAKUPAN_MATERI.md). Bagian tanpa contoh kode pada notebook penulis juga dijelaskan; beberapa dilengkapi ilustrasi sintetis yang diberi label sebagai contoh tambahan.

Repo ini mencakup Chapter 1-4 sesuai lingkup tugas. Chapter 5-7 dan tambahan regularisasi yang ditandai *not in book* pada notebook sumber berada di luar cakupan.

## Ringkasan Bab

### Chapter 1: Exploratory Data Analysis

Bab ini mempelajari cara mengenali struktur, pusat, sebaran, dan hubungan dalam data sebelum membuat model. Contoh populasi negara bagian membandingkan mean dan median; data pinjaman, maskapai, dan rumah memperlihatkan cara memilih tabel serta grafik sesuai jenis variabel. Kesimpulan utamanya: beberapa angka ringkasan perlu dibaca bersama visualisasi, dan korelasi tidak membuktikan sebab-akibat.

### Chapter 2: Data and Sampling Distributions

Bab ini menghubungkan sampel dengan populasi dan menjelaskan ketidakpastian estimasi. Simulasi pendapatan memperlihatkan bahwa distribusi nilai individual berbeda dari distribusi mean sampel, sementara bootstrap dan confidence interval membantu mengukur variasi statistik. Distribusi probabilitas dipilih sesuai proses yang dimodelkan; sampel besar tidak otomatis menghilangkan bias.

### Chapter 3: Statistical Experiments and Significance Testing

Bab ini membahas desain eksperimen dan cara menilai apakah perbedaan yang diamati dapat dijelaskan oleh variasi acak. Contoh halaman web dan conversion rate dipelajari menggunakan permutation test, t-test, ANOVA, serta uji kategori. P-value harus dibaca bersama besar efek, asumsi, dan desain; contoh multi-arm bandit memperkenalkan alokasi adaptif untuk mengoptimalkan reward selama pengujian.

### Chapter 4: Regression and Prediction

Bab ini mempelajari prediksi respons numerik, interpretasi koefisien, serta pemeriksaan model regresi. Contoh harga rumah menghubungkan fitur dengan harga, membandingkan performa training/test, dan menunjukkan peran kategori, interaksi, serta hubungan nonlinier. Diagnostik, cross-validation, dan prediction interval membantu menilai kualitas serta ketidakpastian prediksi untuk pengamatan baru.

## Struktur repo

```text
Practical-Statistics-for-Data-Scientists/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── .gitattributes
├── notebooks/
│   ├── chapter_01_exploratory_data_analysis.ipynb
│   ├── chapter_02_data_and_sampling_distributions.ipynb
│   ├── chapter_03_statistical_experiments_and_significance_testing.ipynb
│   └── chapter_04_regression_and_prediction.ipynb
├── data/
│   ├── SOURCES.json
│   └── ... dataset contoh buku
├── scripts/
│   └── verify_notebooks.py
└── docs/
    └── CAKUPAN_MATERI.md
```

## Menjalankan notebook

Output sudah tersimpan sehingga notebook dapat dibaca langsung di GitHub. Untuk menjalankan ulang, gunakan **Python 3.12**. Dari root repo pada PowerShell:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m ensurepip
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe scripts/verify_notebooks.py
```

Script menjalankan keempat notebook dari kernel baru, memeriksa checksum dataset, dan menyimpan output. Eksekusi berhenti jika terjadi error. Untuk menjalankan satu bab:

```powershell
.venv/Scripts/python.exe scripts/verify_notebooks.py --chapter 3
```

Untuk menjalankan sel secara interaktif, buka notebook di editor yang mendukung Jupyter dan pilih `.venv/Scripts/python.exe` sebagai kernel. Jalankan dari root repo atau folder `notebooks`, lalu pilih **Restart Kernel** dan **Run All**. Semua dataset tersedia lokal di `data/`.

<details>
<summary><strong>Detail data, adaptasi kode, dan validasi</strong></summary>

## Data dan reproduksibilitas

[SOURCES.json](data/SOURCES.json) mencatat sumber, commit, ukuran, dan SHA-256 seluruh 14 dataset. Seed simulasi ditetapkan; versi dependency yang digunakan dicatat pada [requirements.txt](requirements.txt). Perbedaan platform dapat menghasilkan perbedaan numerik kecil.

`.gitattributes` mempertahankan byte dataset saat checkout, termasuk pada Windows. Lingkungan Python, cache, dan file sementara berada di folder proyek dan diabaikan Git. Buku PDF dan daftar mahasiswa dari dokumen tugas tidak disertakan.

## Adaptasi dari kode sumber

- **Chapter 1:** memakai `pd.crosstab` dengan denominator proporsi yang eksplisit, seed tetap untuk sampel KDE, dan penjelasan scaling MAD pada statsmodels.
- **Chapter 2:** memakai garis fit untuk QQ-plot NFLX. Transformasi selisih log perubahan harga positif dari sumber dipertahankan untuk ilustrasi distribusi, dengan penjelasan bahwa hasilnya bukan log-return harga saham.
- **Chapter 3:** memperbaiki pembagian F dan p-value ANOVA dengan dua; menetapkan arah Welch t-test; menyelaraskan selisih conversion dan permutation; memakai koreksi +1 pada p-value Monte Carlo; memperbaiki sampling dengan pengembalian; menjalankan Fisher 2x2; memakai `NormalIndPower` untuk contoh dua proporsi.
- **Chapter 4:** menambahkan holdout 80/20 dan baseline mean training pada fitur numerik; menjelaskan risiko target leakage dari ZipGroup; menghilangkan redundansi term linear dan spline pada GLMGam serta memeriksa rank matriks desain.

## Validasi dan batas interpretasi

Keempat notebook telah dijalankan dengan Python 3.12.14: **144 sel kode dan 42 output grafik, tanpa error**. Checksum semua dataset terverifikasi. Pemeriksaan tambahan mencakup jumlah proporsi per grade, cakupan interval 90% dalam interval 95%, kecocokan ANOVA SciPy/statsmodels, pemisahan indeks train/test, rank matriks GLMGam, mode/expected value, kuantil distribusi t, parameter failure rate, jumlah alokasi bandit, encoding ordinal, lebar prediction interval, dan skor cross-validation. Sampel grafik dari setiap bab juga diperiksa secara visual.

Peringatan library tentang p-value pyGAM tetap ditampilkan dan dijelaskan; angka tersebut tidak digunakan untuk menyimpulkan signifikansi. Pemeriksaan kode tidak membuktikan seluruh asumsi statistik atau representativitas data. Evaluasi harga rumah menggunakan holdout acak, sehingga belum merupakan validasi prediksi transaksi masa depan. Asosiasi yang diamati tidak otomatis menunjukkan sebab-akibat.

</details>

## Referensi dan lisensi

1. Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python* (2nd ed.). O'Reilly Media. ISBN 978-1492072942.
2. [Repo kode penulis](https://github.com/gedeck/practical-statistics-for-data-scientists), commit `8a6d3bb6468e979c861d4b37215e1413702dfdfa`.
3. [Notebook sumber](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/8a6d3bb6468e979c861d4b37215e1413702dfdfa/python/notebooks).
4. [Contoh format pengumpulan](https://github.com/farrelrassya/Practical-Statistics-for-Data-Scientist-Books) dari dokumen tugas. Kode repo ini berasal dari notebook penulis, bukan pekerjaan mahasiswa contoh.
5. Fungsi plot elips Chapter 1 mempertahankan atribusi [Stack Overflow](https://stackoverflow.com/a/34558488) pada notebook penulis.

Kode dasar: copyright (c) 2019 Peter C. Bruce, Andrew Bruce, Peter Gedeck. Adaptasi dan catatan tambahan: 2026. Lisensi GPL-3.0 dari repo sumber disertakan pada [LICENSE](LICENSE). Dataset disertakan untuk reproduksi contoh pembelajaran; asal setiap file dicatat pada manifest sumber.
