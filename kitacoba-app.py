import streamlit as st
import pandas as pd

st.title("Jadwal Kegiatan Mingguan (Senin–Jumat)")

# Data awal jadwal
df = pd.DataFrame({
    "Hari": [
        "Senin", "Senin",
        "Selasa", "Selasa",
        "Rabu",
        "Kamis",
        "Jumat"
    ],
    "Waktu": [
        "08.00–10.00", "13.00–15.00",
        "09.00–11.00", "14.00–16.00",
        "08.00–10.00",
        "10.00–12.00",
        "13.00–15.00"
    ],
    "Nama Kegiatan": [
        "Kuliah",
        "Belajar Mandiri",
        "Praktikum",
        "Diskusi Kelompok",
        "Kuliah",
        "Belajar",
        "Review Materi"
    ]
})

# Tabel jadwal editable
jadwal = st.data_editor(
    df,
    column_config={
        "Hari": st.column_config.SelectboxColumn(
            "Hari",
            options=["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
        )
    },
    num_rows="dynamic",
    use_container_width=True
)

st.subheader("Jadwal Tersimpan")
st.table(jadwal)
