import streamlit as st
import pandas as pd

st.title("Jadwal Kegiatan (Editable oleh Pengguna)")

# Data awal
df = pd.DataFrame({
    "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
    "Waktu": ["08.00–10.00", "09.00–11.00", "10.00–12.00", "13.00–15.00", "08.00–10.00"],
    "Nama Kegiatan": ["Kuliah", "Praktikum", "Belajar", "Diskusi", "Review Materi"]
})

# Tabel editable
jadwal = st.data_editor(
    df,
    num_rows="dynamic",              # bisa tambah & hapus baris
    use_container_width=True,
    column_config={
        "Hari": st.column_config.SelectboxColumn(
            "Hari",
            options=["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
        )
    }
)

st.subheader("Hasil Edit Jadwal")
st.table(jadwal)
