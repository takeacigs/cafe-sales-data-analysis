import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Cafe Sales Dashboard",
    page_icon="☕",
    layout="wide"
)

# Judul dashboard
st.title("Cafe Sales Dashboard")
st.write(
    "Dashboard untuk menganalisis penjualan, "
    "tren transaksi bulanan, dan metode pembayaran."
)

# Memuat dataset yang sudah dibersihkan
@st.cache_data
def load_data():
    data = pd.read_csv("data/processed/cafe_sales_clean.csv")
    data["Transaction Date"] = pd.to_datetime(
        data["Transaction Date"], errors="coerce"
    )
    return data

df = load_data()


# Menghitung KPI
total_penjualan = df["Total Spent"].sum()

total_transaksi = df["Transaction ID"].nunique()

penjualan_produk = (
    df.dropna(subset=["Item", "Total Spent"])
      .groupby("Item")["Total Spent"]
      .sum()
      .sort_values(ascending=False)
)

produk_terlaris = penjualan_produk.index[0]

# Menampilkan KPI
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Penjualan",
    f"{total_penjualan:,.1f}"
)

col2.metric(
    "Total Transaksi",
    f"{total_transaksi:,}"
)

col3.metric(
    "Produk dengan Penjualan Tertinggi",
    produk_terlaris
)


st.divider()
st.header("Analisis Penjualan Produk")

# Filter produk
daftar_produk = sorted(df["Item"].dropna().unique())

produk_dipilih = st.multiselect(
    "Pilih produk",
    options=daftar_produk,
    default=daftar_produk
)

# Filter data berdasarkan produk
df_filter = df[df["Item"].isin(produk_dipilih)]

# Menghitung total penjualan setiap produk
penjualan_produk = (
    df_filter.dropna(subset=["Item", "Total Spent"])
    .groupby("Item")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

# Menampilkan grafik
fig, ax = plt.subplots(figsize=(9, 5))
penjualan_produk.plot(kind="bar", ax=ax)

ax.set_title("Total Penjualan Berdasarkan Produk")
ax.set_xlabel("Produk")
ax.set_ylabel("Total Penjualan")
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)


st.divider()
st.header("Tren Transaksi Bulanan")

# Mengambil data yang memiliki tanggal transaksi
df_tanggal = df.dropna(subset=["Transaction Date"]).copy()

# Mengelompokkan transaksi berdasarkan bulan
transaksi_bulanan = (
    df_tanggal.groupby(
        df_tanggal["Transaction Date"].dt.to_period("M")
    )
    .size()
)

# Mengubah periode menjadi teks agar mudah ditampilkan
transaksi_bulanan.index = transaksi_bulanan.index.astype(str)

# Membuat grafik garis
fig, ax = plt.subplots(figsize=(10, 5))

transaksi_bulanan.plot(
    kind="line",
    marker="o",
    ax=ax
)

ax.set_title("Tren Jumlah Transaksi per Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Transaksi")
ax.tick_params(axis="x", rotation=45)
ax.grid(True, alpha=0.3)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)


st.divider()
st.header("Analisis Metode Pembayaran")

# Menghitung transaksi berdasarkan metode pembayaran
pembayaran = (
    df.dropna(subset=["Payment Method"])
      ["Payment Method"]
      .value_counts()
)

# Membuat grafik batang
fig, ax = plt.subplots(figsize=(9, 5))

pembayaran.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Jumlah Transaksi Berdasarkan Metode Pembayaran")
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Jumlah Transaksi")
ax.tick_params(axis="x", rotation=0)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)


st.divider()
st.header("Business Insights")

# Insight produk dengan total penjualan tertinggi
if not penjualan_produk.empty:
    produk_tertinggi = penjualan_produk.idxmax()
    total_tertinggi = penjualan_produk.max()

    st.markdown("### 1. Produk dengan Total Penjualan Tertinggi")
    st.write(
        f"{produk_tertinggi} memiliki total penjualan "
        f"sebesar {total_tertinggi:,.1f}."
    )

# Insight bulan dengan transaksi terbanyak
if not transaksi_bulanan.empty:
    bulan_tertinggi = transaksi_bulanan.idxmax()
    jumlah_tertinggi = transaksi_bulanan.max()

    st.markdown("### 2. Tren Transaksi Bulanan")
    st.write(
        f"Jumlah transaksi tertinggi terjadi pada "
        f"{bulan_tertinggi}, sebanyak {jumlah_tertinggi} transaksi."
    )

# Insight metode pembayaran
if not pembayaran.empty:
    metode_tertinggi = pembayaran.idxmax()
    jumlah_metode = pembayaran.max()

    st.markdown("### 3. Metode Pembayaran Terbanyak")
    st.write(
        f"{metode_tertinggi} merupakan metode pembayaran "
        f"yang paling banyak tercatat, sebanyak "
        f"{jumlah_metode} transaksi."
    )

st.caption(
    "Catatan: insight didasarkan pada data yang tersedia. "
    "Nilai kosong dapat memengaruhi hasil analisis."
)

st.success("Dataset berhasil dimuat.")

st.write("Ukuran dataset:", df.shape)
st.dataframe(df.head())