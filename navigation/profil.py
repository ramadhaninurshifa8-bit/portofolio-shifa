import streamlit as st

def tampilkan():
    st.title("👤 Profil Saya")
    st.write("Kenali saya lebih dekat.")

    kiri, kanan = st.columns([1, 2])

    with kiri:
        st.image(
            "pages/poto.cipa.jpeg",
            caption="Nur Shifa Ramadhani",
            width=220
        )

    with kanan:
        st.subheader("NUR SHIFA RAMADHANI")
        st.write("🎓 **Prodi:** Sistem Informasi")
        st.write("🏫 **Kampus:** Universitas Nurdin Hamzah")
        st.write("🍳 **Hobi:** Masak")
        st.write("🎮 **Hobi lainnya:** Scroll Tiktok")
        st.write(
            "✨ **Motto hidup:** Terus berusaha "
            "dan jangan mudah menyerah."
        )
        st.write(
            "💻 **Minat keilmuan:** Pemrograman, "
            "basis data, dan teknologi informasi."
        )

    st.divider()
    st.subheader("Tentang Saya")
    st.write(
        "Saya adalah mahasiswa Sistem Informasi yang "
        "sedang belajar mengembangkan kemampuan di bidang teknologi."
    )
