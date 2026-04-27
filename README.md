# Analisis Data Pelanggan E-Commerce Brazil

## Identitas

**Nama:** Nabila Carrissa Dewi

**Email:** nabilacarrissa@gmail.com

**ID Dicoding:** cdcc748d6x0297

---

## Deskripsi Proyek

Proyek ini merupakan analisis data end-to-end terhadap dataset pelanggan platform e-commerce Brazil (Olist). Analisis mencakup proses **Business Understanding**, **Data Wrangling**, **Exploratory Data Analysis (EDA)**, **Visualisasi Data**, serta pembuatan **Dashboard Interaktif** menggunakan Streamlit.

### Asumsi Periode Waktu

Dataset tidak memiliki kolom waktu (timestamp/date). Oleh karena itu, data diasumsikan merepresentasikan **kumulatif pelanggan sepanjang tahun 2017** untuk memenuhi aspek _Time-bound_ dalam analisis.

### Batasan Analisis

Analisis ini berfokus pada distribusi pelanggan berdasarkan lokasi geografis (state dan kota), tanpa mempertimbangkan faktor eksternal seperti populasi atau kondisi ekonomi wilayah.

---

## Struktur Folder

```
submission/
├── dashboard/
│   ├── main_data.csv       # Dataset bersih untuk dashboard
│   └── dashboard.py        # Script Streamlit dashboard
├── data/
│   └── dataset.csv         # Dataset original
├── notebook.ipynb          # Jupyter Notebook analisis lengkap
├── README.md               # Dokumentasi proyek (file ini)
├── requirements.txt        # Dependensi Python
└── url.txt                 # URL deployment dashboard (opsional)
```

---

## Pertanyaan Bisnis

1. **Di antara seluruh negara bagian di Brazil, 5 negara bagian manakah yang memiliki jumlah pelanggan terbanyak pada tahun 2017, dan berapa persentase kontribusi masing-masing terhadap total pelanggan nasional?**

2. **Seberapa besar kontribusi 10 kota dengan jumlah pelanggan terbanyak terhadap total pelanggan di Brazil pada tahun 2017, dan apakah distribusi pelanggan terkonsentrasi pada kota-kota tertentu?**

---

## Cara Menjalankan

### 1. Clone / Download Proyek

```bash
git clone <repo-url>
cd submission
```

### 2. Install Dependensi

```bash
pip install -r requirements.txt
```

### 3. Jalankan Notebook

Buka dan jalankan file `notebook.ipynb` menggunakan Jupyter Notebook atau Jupyter Lab:

```bash
jupyter notebook notebook.ipynb
```

### 4. Jalankan Dashboard Streamlit

```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka di browser pada `http://localhost:8501`.

---

## Fitur Dashboard

- **Filter Negara Bagian**: Pilih satu atau lebih state untuk memfilter data
- **Slider Top-N Kota**: Tampilkan top 5–20 kota berdasarkan jumlah pelanggan
- **KPI Cards**: Ringkasan metrik utama (total pelanggan, kota, state, state terbanyak)
- **Grafik Batang Horizontal**: Distribusi pelanggan per negara bagian (Top 15)
- **Grafik Batang Vertikal**: Distribusi pelanggan per kota (Top N)
- **Tabel Ringkasan**: Detail per state dengan highlight nilai tertinggi
- **Insight Ekspansi**: Penjelasan analisis di setiap visualisasi

---

## Temuan Utama

1. **São Paulo (SP)** mendominasi dengan ~43% dari total pelanggan nasional
2. Lima negara bagian teratas menyumbang **>75%** dari total pelanggan
3. **Sao Paulo** (kota) memiliki 15.000+ pelanggan, jauh melampaui kota lainnya
4. Kawasan **Utara Brazil** memiliki penetrasi e-commerce yang sangat rendah → peluang ekspansi

---

## Dataset

- **Sumber**: Customer Dataset
- **Jumlah baris**: 99.441 entri
- **Kolom**: `customer_id`, `customer_unique_id`, `customer_zip_code_prefix`, `customer_city`, `customer_state`
- **Pelanggan unik**: 96.096

---

## Lisensi

Proyek ini dibuat untuk keperluan submission Dicoding. Dataset bersumber dari Olist dan tersedia secara publik di Kaggle.
