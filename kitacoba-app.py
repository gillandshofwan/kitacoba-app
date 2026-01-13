import streamlit as st
import pandas as pd

# Data jadwal harian
data = {
    "Waktu": ["06.00–07.00", "08.00–10.00", "12.00–13.00", "14.00–16.00", "19.00–21.00"],
    "Kegiatan": [
        "Olahraga & persiapan",
        "Kuliah",
        "Istirahat",
        "Belajar / Tugas",
        "Waktu pribadi"
    ]
}

df = pd.DataFrame(data)

st.title("Jadwal Harian")
st.table(df)
