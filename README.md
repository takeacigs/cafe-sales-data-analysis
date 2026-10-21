# Analisis Dirty Cafe Sales

## Deskripsi Proyek
Proyek ini merupakan analisis data penjualan kafe menggunakan Python. Analisis dilakukan untuk memahami pola transaksi, mengidentifikasi produk dengan total penjualan tertinggi, mengetahui metode pembayaran yang paling banyak digunakan, serta mengevaluasi kualitas data sebelum dilakukan analisis lebih lanjut.

Proyek ini juga dilengkapi dengan dashboard interaktif menggunakan Streamlit untuk menyajikan hasil analisis secara lebih mudah dipahami.

## Tujuan Analisis
1. Mengetahui produk dengan total penjualan tertinggi.
2. Mengidentifikasi tren jumlah transaksi setiap bulan selama tahun 2023.
3. Mengetahui metode pembayaran yang paling banyak digunakan berdasarkan data yang tersedia.
4. Mengevaluasi dan mempersiapkan kualitas data penjualan sebelum analisis.

## Pertanyaan Bisnis
1. Produk apa yang memiliki total penjualan tertinggi?
2. Bagaimana tren jumlah transaksi setiap bulan selama tahun 2023?
3. Metode pembayaran apa yang paling banyak digunakan berdasarkan data yang tersedia?

## Dataset
- **Nama:** Dirty Cafe Sales
- **Format:** CSV
- **Jumlah data:** 10.000 baris dan 8 kolom
- **Sumber:** [Cafe Sales - Dirty Data for Cleaning Training](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training)
- **File dataset asli:** `data/dirty_cafe_sales.csv`
- **File dataset hasil persiapan:** `data/processed/cafe_sales_clean.csv`

Dataset berisi catatan transaksi penjualan kafe, meliputi ID transaksi, produk, kuantitas, harga per unit, total pengeluaran, metode pembayaran, lokasi transaksi, dan tanggal transaksi.

## Tools dan Teknologi
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Visual Studio Code
- Streamlit
- Git dan GitHub

## Tahapan Pengerjaan
1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Exploratory Data Analysis (EDA)
5. Business Insights dan Rekomendasi
6. Pembuatan Dashboard Interaktif

## Hasil Analisis
Berdasarkan data yang tersedia:
- **Produk dengan total penjualan tertinggi:** Salad, sebesar 17.320.
- **Bulan dengan jumlah transaksi tertinggi:** Oktober 2023, sebanyak 838 transaksi.
- **Bulan dengan jumlah transaksi terendah:** Februari 2023, sebanyak 727 transaksi.
- **Metode pembayaran yang paling banyak tercatat:** Digital Wallet, sebanyak 2.291 transaksi.

Hasil tersebut didasarkan pada data yang tersedia setelah pemeriksaan dan persiapan data. Nilai yang kosong dapat memengaruhi hasil analisis pada kolom tertentu.

## Struktur Repository
```text
cafe-sales-data-analysis/
├── data/
│   ├── dirty_cafe_sales.csv
│   └── processed/
│       └── cafe_sales_clean.csv
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preparation.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   └── 04_business_insights.ipynb
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

**Sumber:** [Cantumkan tautan sumber dataset asli]

## Cara Menjalankan Dashboard
1. Pastikan Python sudah terpasang.
2. Buka terminal pada folder utama proyek.
3. Instal dependensi dengan perintah:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan dashboard dengan perintah:

   ```bash
   streamlit run app.py
   ```
