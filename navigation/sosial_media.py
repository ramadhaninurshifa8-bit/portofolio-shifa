import streamlit as st

def tampilkan():
    st.title("📱 Sosial Media")
    st.write("Temukan saya di Instagram.")

    username = st.text_input(
        "Username Instagram",
        value="username_kamu"
    )

    if username.strip() and username != "username_kamu":
        username = username.strip().lstrip("@")

        st.link_button(
            "📸 Kunjungi Instagram Saya",
            f"https://www.instagram.com/nur_shifa16?srtk=MTByajNrdHh5ODFwdQ=="
        )