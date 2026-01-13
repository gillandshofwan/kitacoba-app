import streamlit as st
import pandas as pd

st.title("Jadwal Kegiatan")

# Data awal tabel
df = pd.DataFrame({
    "Hari": ["Senin", "Senin", "Selasa"],
    "Waktu": ["08.00–10.00", "13.00–15.00", "09.00–11.00"],
    "Nama Kegiatan": ["Kuliah", "Belajar Mandiri", "Praktikum"]
})

# Tabel editable
jadwal = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True
)

st.subheader("Jadwal Tersimpan")
st.table(jadwal)
