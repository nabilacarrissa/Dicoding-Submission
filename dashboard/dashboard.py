"""
========================================================
 DASHBOARD ANALISIS PELANGGAN E-COMMERCE BRAZIL (2017)
--------------------------------------------------------
 Nama   : Nabila Carrissa Dewi
 Email  : nabilacarrissa@gmail.com
 ID     : cdcc748d6x0297
========================================================
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
import os

warnings.filterwarnings("ignore")

# ── Konfigurasi halaman ─────────────────────────────────
st.set_page_config(
    page_title="E-Commerce Customers Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Warna ───────────────────────────────────────────────
BASE_COLOR = "#2E86AB"
HIGHLIGHT = "#F24236"


# ── Load data ───────────────────────────────────────────
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")
    if not os.path.exists(file_path):
        st.error(f"File 'main_data.csv' tidak ditemukan di: {file_path}")
        st.stop()
    df = pd.read_csv(file_path)
    df["customer_city"] = df["customer_city"].str.strip().str.lower()
    df_unique = df.drop_duplicates(
        subset="customer_unique_id", keep="first"
    ).reset_index(drop=True)
    return df_unique


df = load_data()

# ── Sidebar ─────────────────────────────────────────────
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2331/2331970.png", width=80)
    st.markdown("## 🛒 E-Commerce Brazil")
    st.markdown("**Analisis Distribusi Pelanggan Tahun 2017**")
    st.divider()

    all_states = sorted(df["customer_state"].unique())
    selected_states = st.multiselect(
        "📍 Filter Negara Bagian (State)",
        options=all_states,
        default=all_states,
    )

    top_n = st.slider("🏙️ Tampilkan Top-N Kota", 5, 20, 10)

    st.divider()
    st.caption("👩‍💻 Nabila Carrissa Dewi")
    st.caption("ID Dicoding: CDCC748D6X0297")

# ── Filter data ─────────────────────────────────────────
df_filtered = df[df["customer_state"].isin(selected_states)]

if df_filtered.empty:
    st.warning("⚠️ Tidak ada data untuk filter yang dipilih.")
    st.stop()

# ── Header ──────────────────────────────────────────────
st.title("🛒 Dashboard Analisis Pelanggan E-Commerce Brazil")
st.markdown(
    "Data merepresentasikan pelanggan terdaftar sepanjang tahun 2017 (berdasarkan asumsi dataset)."
)
st.divider()

# ── KPI ─────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

total_customers = df_filtered["customer_unique_id"].nunique()
total_cities = df_filtered["customer_city"].nunique()
total_states = df_filtered["customer_state"].nunique()

top_state = df_filtered["customer_state"].value_counts().idxmax()
top_state_count = df_filtered["customer_state"].value_counts().max()

col1.metric("👥 Total Pelanggan Unik", f"{total_customers:,}")
col2.metric("🏙️ Total Kota", f"{total_cities:,}")
col3.metric("🗺️ Negara Bagian", f"{total_states}")
col4.metric("🏆 State Terbanyak", top_state, delta=f"{top_state_count:,} pelanggan")

st.divider()

# ── Visualisasi 1: State ─────────────────────────────────
st.subheader("📊 Distribusi Pelanggan per Negara Bagian (Top 15)")

state_counts = (
    df_filtered.groupby("customer_state")["customer_unique_id"]
    .nunique()
    .sort_values(ascending=False)
    .reset_index()
    .rename(columns={"customer_unique_id": "jumlah_pelanggan"})
    .head(15)
)

state_counts["persentase"] = (
    state_counts["jumlah_pelanggan"] / state_counts["jumlah_pelanggan"].sum() * 100
).round(2)

colors_s = [
    HIGHLIGHT if s == top_state else BASE_COLOR for s in state_counts["customer_state"]
]

fig1, ax1 = plt.subplots(figsize=(10, 5))
bars = ax1.barh(
    state_counts["customer_state"][::-1],
    state_counts["jumlah_pelanggan"][::-1],
    color=colors_s[::-1],
)

for bar, val, pct in zip(
    bars,
    state_counts["jumlah_pelanggan"][::-1],
    state_counts["persentase"][::-1],
):
    ax1.text(
        bar.get_width() + state_counts["jumlah_pelanggan"].max() * 0.01,
        bar.get_y() + bar.get_height() / 2,
        f"{val:,} ({pct:.1f}%)",
        va="center",
        fontsize=8,
    )

ax1.set_title("Top 15 Negara Bagian (2017)", fontsize=11, fontweight="bold")
ax1.set_xlabel("Jumlah Pelanggan")
ax1.grid(axis="x", linestyle="--", alpha=0.3)

ax1.legend(
    handles=[
        mpatches.Patch(color=HIGHLIGHT, label="State terbanyak"),
        mpatches.Patch(color=BASE_COLOR, label="Lainnya"),
    ]
)

st.pyplot(fig1)

with st.expander("💡 Insight"):
    sp_pct = (
        df_filtered[df_filtered["customer_state"] == "SP"][
            "customer_unique_id"
        ].nunique()
        / total_customers
        * 100
    )
    st.markdown(
        f"""
- São Paulo mendominasi sekitar **{sp_pct:.1f}%** pelanggan
- Distribusi pelanggan terkonsentrasi di beberapa state utama
- Banyak state memiliki kontribusi lebih kecil
"""
    )

st.divider()

# ── Visualisasi 2: Kota ─────────────────────────────────
st.subheader(f"🏙️ Top {top_n} Kota")

city_counts = (
    df_filtered.groupby("customer_city")["customer_unique_id"]
    .nunique()
    .sort_values(ascending=False)
    .reset_index()
    .rename(columns={"customer_unique_id": "jumlah_pelanggan"})
    .head(top_n)
)

colors_c = [HIGHLIGHT if i < 2 else BASE_COLOR for i in range(len(city_counts))]

fig2, ax2 = plt.subplots(figsize=(11, 5))
bars2 = ax2.bar(
    city_counts["customer_city"].str.title(),
    city_counts["jumlah_pelanggan"],
    color=colors_c,
)

for bar, val in zip(bars2, city_counts["jumlah_pelanggan"]):
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{val:,}",
        ha="center",
        fontsize=8,
    )

ax2.set_title(f"Top {top_n} Kota (2017)", fontsize=11, fontweight="bold")
ax2.grid(axis="y", linestyle="--", alpha=0.3)
plt.xticks(rotation=30)

st.pyplot(fig2)

with st.expander("💡 Insight"):
    top_city = city_counts.iloc[0]["customer_city"].title()
    top_val = city_counts.iloc[0]["jumlah_pelanggan"]

    st.markdown(
        f"""
- Kota dengan pelanggan terbanyak adalah **{top_city}** ({top_val:,})
- Terdapat perbedaan signifikan antara kota teratas dan lainnya
- Distribusi pelanggan cenderung terpusat di kota besar
"""
    )

st.divider()

# ── Tabel ───────────────────────────────────────────────
st.subheader("📋 Ringkasan per State")

summary = (
    df_filtered.groupby("customer_state")
    .agg(
        Pelanggan=("customer_unique_id", "nunique"),
        Kota=("customer_city", "nunique"),
    )
    .sort_values("Pelanggan", ascending=False)
    .reset_index()
)

summary["Persentase"] = (summary["Pelanggan"] / summary["Pelanggan"].sum() * 100).round(
    2
)

st.dataframe(summary, use_container_width=True)

st.caption("Data merupakan representasi pelanggan tahun 2017 (asumsi dataset).")
