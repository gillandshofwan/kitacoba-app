import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.image("Methylene Blue dengan UV tanpa ZnO.png", caption="Sunrise by the mountains")

with st.sidebar:
    with st.button() :
          if st.button("Say hello"):
            st.write("Why hello there")
      
