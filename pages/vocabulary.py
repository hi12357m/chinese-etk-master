import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Vocabulary Master", page_icon="🈶", layout="wide")

# Sidebar menu
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>Menu</h2>", unsafe_allow_html=True)
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/vocabulary.py", label="Vocabulary", icon="🈶")
    st.page_link("pages/listening.py", label="Listening", icon="🎧")

st.title("Vocabulary 🈶")

# Show the vocabulary table (row numbers start at 1)
df = pd.read_csv("U2 Chinese Simplified Set 1.csv")
df.index = df.index + 1
st.dataframe(df, use_container_width=True)

