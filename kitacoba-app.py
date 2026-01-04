import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.title("Halaman Utama")
st.write("Ini konten utama")

st.sidebar.title("Mau_Hitung_Apa_Hari_Ini?")
Mau_Hitung_Apa_Hari_Ini? = st.sidebar.selectbox(
    "Pilih Menu:",
    ["Pilihan 1", "Pilihan 2"]
)

st.title(Mau_Hitung_Apa_Hari_Ini?)

if Mau_Hitung_Apa_Hari_Ini? == "Pilihan 1":
    st.write("Konten Pilihan 1")

elif Mau_Hitung_Apa_Hari_Ini? == "Pilihan 2":
    st.write("Konten Pilihan 2")

