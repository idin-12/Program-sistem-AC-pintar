# ac_pintar_streamlit.py
# Sistem AC Pintar dengan Streamlit

import streamlit as st

def main():
    st.title("Sistem AC Pintar")

    st.write("""
    Program ini menyalakan AC hanya jika:
    - Suhu panas
    - Jendela tertutup
    - Ada orang di rumah
    """)

    is_hot = st.radio("Apakah suhu panas?", ("yes", "no")) == "yes"
    window_closed = st.radio("Apakah jendela tertutup?", ("yes", "no")) == "yes"
    someone_home = st.radio("Apakah ada orang di rumah?", ("yes", "no")) == "yes"

    if st.button("Cek Status AC"):
        if is_hot and window_closed and someone_home:
            st.success("AC MENYALA")
        else:
            st.warning("AC MATI")

if __name__ == "__main__":
    main()
