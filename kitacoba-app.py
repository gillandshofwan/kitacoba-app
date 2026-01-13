import streamlit as st
import pandas as pd

st.title("Jadwal Laboratorium")

# =========================
# Data jadwal tiap lab
# =========================
jadwal_lab = {
    "Lab Organik": pd.DataFrame({
        "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "Jam": ["07:30 - 17:30", "", "", "12:30 - 17:30", ""],
        "Kegiatan": ["Praktik kelas 1G", "", "", "Praktik kelas 2A", ""]
    }),

    "Lab Analitik": pd.DataFrame({
        "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "Jam": ["", "07:30 - 17:30", "", "", "07:30 - 12:30"],
        "Kegiatan": ["", "Praktik kelas 2E1", "", "", "Praktik kelas 2F"]
    }),

    "Lab Lingkungan": pd.DataFrame({
        "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "Jam": ["07:30 - 17:30", "", "07:30 - 12:30", "12:30 - 17:30", ""],
        "Kegiatan": [
            "Praktik kelas 1D",
            "",
            "Praktik kelas 2F",
            "Praktik kelas 2A",
            ""
        ]
    }),

    "Lab Instrumen": pd.DataFrame({
        "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "Jam": ["07:30 - 17:30", "", "", "12:30 - 17:30", "07:30 - 17:30"],
        "Kegiatan": [
            "Praktik kelas 1G",
            "",
            "",
            "Praktik kelas 2G",
            "Praktik kelas 1B"
        ]
    }),

    "Lab Mikro": pd.DataFrame({
        "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "Jam": ["", "", "07:30 - 17:30", "12:30 - 17:30", ""],
        "Kegiatan": ["", "", "Praktik kelas 1E", "Praktik kelas 2A", ""]
    }),

    "Lab Fisika": pd.DataFrame({
        "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "Jam": [
            "07:30 - 17:30",
            "07:30 - 17:30",
            "07:30 - 17:30",
            "12:30 - 17:30",
            ""
        ],
        "Kegiatan": [
            "Praktik kelas 1G",
            "Praktik kelas 2C",
            "Praktik kelas 1D",
            "Praktik kelas 2A",
            ""
        ]
    }),

    "Lab Teknologi": pd.DataFrame({
        "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
        "Jam": ["", "07:30 - 17:30", "", "07:30 - 17:30", ""],
        "Kegiatan": ["", "Praktik kelas 1G", "", "Praktik kelas 2C", ""]
    })
}

# =========================
# Pilih lab
# =========================
lab_dipilih = st.selectbox(
    "Pilih Laboratorium",
    options=list(jadwal_lab.keys())
)

# =========================
# Tampilkan jadwal (read-only)
# =========================
st.subheader(f"Jadwal {lab_dipilih}")
st.dataframe(
    jadwal_lab[lab_dipilih],
    use_container_width=True
)
