import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.title("Halaman Utama")
st.write("Ini konten utama")

st.sidebar.title("Mau_Hitung_Apa_Hari_Ini?")
menu = st.sidebar.selectbox(
    "Pilih Menu:",
    ["Pilihan 1", "Pilihan 2"]
)

st.title(menu)

if menu == "Pilihan 1":
    st.write("Konten Pilihan 1")

elif menu == "Pilihan 2":
    st.write("Konten Pilihan 2")

