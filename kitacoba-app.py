import streamlit as st

st.write("Hello, *World!* :sunglasses:")

import streamlit as st

import streamlit as st

# ==============================
# INISIALISASI STATE HALAMAN
# ==============================
if "page" not in st.session_state:
    st.session_state.page = "home"


# ==============================
# HALAMAN UTAMA / PEMBUKA
# ==============================
def halaman_utama():
    st.title("👋 Selamat Datang")
    st.write(
        """
        Selamat datang di **Website Kalkulator Laboratorium**.  
        Silakan buka **sidebar** dan pilih menu kalkulator
        yang ingin digunakan.
        """
    )
    st.info("Gunakan menu di sidebar untuk memulai.")


# ==============================
# KALKULATOR PENGENCERAN
# ==============================
def kalkulator_pengenceran():
    st.header("Kalkulator Pengenceran")
    st.write("Contoh operasi sederhana")

    a = st.number_input("Masukkan angka pertama", key="p1_a")
    b = st.number_input("Masukkan angka kedua", key="p1_b")

    if st.button("Hitung Penjumlahan"):
        st.success(f"Hasil: {a + b}")

    st.markdown("---")
    if st.button("⬅️ Kembali ke Halaman Utama"):
        st.session_state.page = "home"
        st.rerun()


# ==============================
# KALKULATOR PENIMBANGAN
# ==============================
def kalkulator_penimbangan():
    st.header("Kalkulator Penimbangan")
    st.write("Contoh operasi sederhana")

    x = st.number_input("Masukkan angka pertama", key="p2_x")
    y = st.number_input("Masukkan angka kedua", key="p2_y")

    if st.button("Hitung Perkalian"):
        st.success(f"Hasil: {x * y}")

    st.markdown("---")
    if st.button("⬅️ Kembali ke Halaman Utama"):
        st.session_state.page = "home"
        st.rerun()


# ==============================
# SIDEBAR NAVIGASI
# ==============================
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Halaman Utama", "Pengenceran", "Penimbangan"]
)

if menu == "Halaman Utama":
    st.session_state.page = "home"
elif menu == "Pengenceran":
    st.session_state.page = "pengenceran"
elif menu == "Penimbangan":
    st.session_state.page = "penimbangan"


# ==============================
# ROUTING HALAMAN
# ==============================
if st.session_state.page == "home":
    halaman_utama()

elif st.session_state.page == "pengenceran":
    kalkulator_pengenceran()

elif st.session_state.page == "penimbangan":
    kalkulator_penimbangan()



