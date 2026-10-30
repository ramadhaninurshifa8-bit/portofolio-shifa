import streamlit as st
import home 
import profil
import sosial_media
import kemampuan

st.set_page_config(
    page_title="Portofolio SHIFA",
    page_icon="💜",
    layout="wide"
)

st.sidebar.title("💜 SHIFA")
st.sidebar.caption("Personal Portfolio")

menu = st.sidebar.selectbox(
    "Menu Navigasi",
    ["Home", "Profil", "Sosial Media", "Kemampuan"]
)

if menu == "Home":
    home.tampilkan()
elif menu == "Profil":
    profil.tampilkan()
elif menu == "Sosial Media":
    sosial_media.tampilkan()
else:
    kemampuan.tampilkan()

st.sidebar.divider()
st.sidebar.caption("© 2026 | Portofolio Pribadi")