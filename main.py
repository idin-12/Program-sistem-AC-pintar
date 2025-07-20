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
    window_closed = st.radio("Apakah jendela tertutup?_
