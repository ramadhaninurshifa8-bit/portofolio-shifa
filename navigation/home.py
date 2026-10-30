import streamlit as st

def tampilkan():
    st.markdown(
        "<h1 style='color:#8B5CF6;'>HELLO, I'M SHIFA!</h1>",
        unsafe_allow_html=True
    )

    st.subheader("Mahasiswa Sistem Informasi")
    st.write("Universitas Nurdin Hamzah")

    st.write(
        "Selamat datang di website portofolio saya. "
        "Di sini kamu bisa mengenal profil, media sosial, "
        "dan kemampuan yang sedang saya kembangkan."
    )

    st.divider()

    kiri, kanan = st.columns(2)

    with kiri:
        st.markdown("### 🎯 Tentang Portofolio")
        st.write(
            "Website ini dibuat sebagai tempat untuk "
            "menampilkan identitas dan perkembangan "
            "kemampuan saya."
        )

    with kanan:
        st.markdown("### 🌱 Tujuan Saya")
        st.write(
            "Terus belajar, menambah pengalaman, "
            "dan mengembangkan kemampuan di bidang teknologi."
        )