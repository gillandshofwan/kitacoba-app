import streamlit as st
import pandas as pd

st.title("Jadwal Kegiatan Mingguan")

df = pd.DataFrame({
    "Hari": ["Senin", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
    "Waktu": [
        "08.00–10.00",
        "13.00–15.00",
        "09.00–11.00",
        "10.00–12.00",
        "13.00–15.00",
        "08.00–10.00"
    ],
    "Nama Kegiatan": [
        "Kuliah",
        "Belajar Mandiri",
        "Praktikum",
        "Belajar",
        "Diskusi",
        "Review Materi"
    ]
})

st.dataframe(df, use_container_width=True)
