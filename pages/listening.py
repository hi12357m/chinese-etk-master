import streamlit as st
import pandas as pd

st.title("Under Maintenance 🛠️")

with st.sidebar:
    st.markdown("""
    <h2 style="text-align:center;">
         Menu
    </h2>
    """, unsafe_allow_html=True)

    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/vocabulary.py", label="Vocabulary", icon="🈶")
    st.page_link("pages/listening.py", label="Listening", icon="🎧")
    st.page_link("pages/sentences.py", label="Sentences", icon="📝")
