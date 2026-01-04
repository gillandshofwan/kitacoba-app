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
    st.header("🧪 Kalkulator Pengenceran Larutan")

    A = st.number_input(
        "Konsentrasi larutan induk (A)",
        min_value=0.0,
        format="%.4f"
    )

    B = st.number_input(
        "Konsentrasi setelah pengenceran (B)",
        min_value=0.0,
        format="%.4f"
    )

    C = st.number_input(
        "Volume akhir setelah pengenceran (C) [mL]",
        min_value=0.0,
        format="%.2f"
    )

    if st.button("Hitung Volume Induk"):
        if A == 0:
            st.error("Konsentrasi larutan induk (A) tidak boleh nol.")
        else:
            D = (B * C) / A

            st.success(f"Volume larutan induk yang harus dipipet (D): **{D:.4f} mL**")

            st.info(
                f"Ambil **{D:.4f} mL** larutan induk, "
                f"kemudian tambahkan pelarut hingga volume akhir **{C:.2f} mL**."
            )

    st.markdown("---")
    if st.button("⬅️ Kembali ke Halaman Utama"):
        st.session_state.page = "home"
        st.rerun()



# ==============================
# KALKULATOR PENIMBANGAN
# ==============================
def kalkulator_penimbangan():
    st.header("⚖️ Kalkulator Penimbangan Larutan")

    A = st.number_input(
        "Konsentrasi yang diinginkan (A) [M]",
        min_value=0.0,
        format="%.4f"
    )

    B = st.number_input(
        "Volume larutan yang akan dibuat (B) [Liter]",
        min_value=0.0,
        format="%.3f"
    )

    C = st.number_input(
        "BM analit (C) [g/mol]",
        min_value=0.0,
        format="%.2f"
    )

    if st.button("Hitung Berat Analit"):
        if A == 0 or B == 0 or C == 0:
            st.error("Semua nilai harus lebih besar dari nol.")
        else:
            D = A * B * C

            st.success(
                f"Berat analit yang harus ditimbang (D): **{D:.4f} gram**"
            )

            st.info(
                f"Timbang **{D:.4f} g** analit, "
                f"larutkan dan encerkan hingga volume akhir **{B:.3f} L**."
            )

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



