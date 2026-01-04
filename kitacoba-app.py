import streamlit as st

st.write("Hello, *World!* :sunglasses:")

import streamlit as st

# ==============================
# FUNGSI PILIHAN 1
# ==============================
def kalkulator_pilihan_1():
    st.header("Kalkulator Pengenceran")
    st.write("Operasi: Penjumlahan & Pengurangan")

    a = st.number_input("Masukkan angka pertama", key="p1_a")
    b = st.number_input("Masukkan angka kedua", key="p1_b")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Tambah", key="btn_tambah"):
            hasil = a + b
            st.success(f"Hasil penjumlahan: {hasil}")

    with col2:
        if st.button("Kurang", key="btn_kurang"):
            hasil = a - b
            st.success(f"Hasil pengurangan: {hasil}")


# ==============================
# FUNGSI PILIHAN 2
# ==============================
def kalkulator_pilihan_2():
    st.header("Kalkulator Penimbangan")
    st.write("Operasi: Perkalian & Pembagian")

    x = st.number_input("Masukkan angka pertama", key="p2_x")
    y = st.number_input("Masukkan angka kedua", key="p2_y")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Kali", key="btn_kali"):
            hasil = x * y
            st.success(f"Hasil perkalian: {hasil}")

    with col2:
        if st.button("Bagi", key="btn_bagi"):
            if y != 0:
                hasil = x / y
                st.success(f"Hasil pembagian: {hasil}")
            else:
                st.error("Tidak bisa dibagi dengan nol!")


# ==============================
# SIDEBAR NAVIGASI
# ==============================
st.sidebar.title("Menu Perhitungan")
menu = st.sidebar.radio(
    "Pilih perhitungan:",
    ["pengenceran", "penimbangan"]
)

# ==============================
# KONTEN UTAMA
# ==============================
st.title("Kalkulator larutan")

if menu == "pengenceran":
    kalkulator_pilihan_1()

elif menu == "penimbangan":
    kalkulator_pilihan_2()



