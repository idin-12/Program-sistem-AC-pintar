# ac_pintar_streamlit.py
# Sistem AC Pintar dengan Streamlit (Desain UI Bagus)

import streamlit as st

def main():
    st.set_page_config(page_title="Sistem AC Pintar", page_icon="❄️")
    st.title("❄️ Sistem AC Pintar")
    st.markdown("---")

    st.write("""
    ✅ **Program ini menyalakan AC hanya jika semua kondisi berikut terpenuhi:**
    - Suhu panas
    - Jendela tertutup
    - Ada orang di rumah
    """)

    st.markdown("### 🔧 **Input Kondisi**")

    # Layout dengan columns untuk tampilan rapi
    col1, col2, col3 = st.columns(3)

    with col1:
        is_hot_input = st.radio("🌡️ Suhu Panas?", ("yes", "no"))
    with col2:
        window_closed_input = st.radio("🪟 Jendela Tertutup?", ("yes", "no"))
    with col3:
        someone_home_input = st.radio("🏠 Ada Orang di Rumah?", ("yes", "no"))

    # Konversi input menjadi boolean
    is_hot = is_hot_input == "yes"
    window_closed = window_closed_input == "yes"
    someone_home = someone_home_input == "yes"

    st.markdown("---")
    if st.button("💡 **Cek Status AC**"):
        if is_hot and window_closed and someone_home:
            st.success("✅ **AC MENYALA**\nSuhu panas, jendela tertutup, dan ada orang di rumah.")
        else:
            st.error("❌ **AC MATI**\nPastikan semua syarat terpenuhi.")

    st.markdown("---")
    st.caption("Dibuat oleh [Nama Kamu] | Sistem AC Pintar Streamlit")

if __name__ == "__main__":
    main()
