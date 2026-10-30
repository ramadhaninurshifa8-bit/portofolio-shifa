import streamlit as st

def tampilkan():
    st.title("🚀 Kemampuan Saya")
    st.write("Perkembangan kemampuan yang sedang saya pelajari.")

    kemampuan = {
        "Python": 70,
        "Microsoft Word": 85,
        "Microsoft Excel": 85,
        "Database": 80,
        "Problem Solving": 70
    }

    for nama, nilai in kemampuan.items():
        st.write(f"**{nama}** — {nilai}%")
        st.progress(nilai)

    st.info(
        "Kemampuan ini akan terus berkembang "
        "seiring dengan proses belajar dan latihan."
    )