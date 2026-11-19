import streamlit as st
import pandas as pd
import random

st.markdown("""
<style>)
/* Vocabulary button */
div.st-key-vocab button {
    background-color: #2E8B57 !important;
    color: white !important;
    border-color: #2E8B57 !important;
}

div.st-key-vocab button p {
    color: white !important;
}

/* General hover effect */
div[data-testid="stButton"] button:hover {
    background-color: #E6F9FC;
    border: 2px solid #06B6D4;
    color: #0891B2;
}

/* Vocabulary hover effect */
div.st-key-vocab button:hover {
    background-color: #246B45 !important;
    color: white !important;
    border-color: #246B45 !important;
}
</style>

""", unsafe_allow_html=True)

st.set_page_config(page_title="Vocabulary Master", page_icon="🈶", layout="wide")

# Sidebar menu
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>Menu</h2>", unsafe_allow_html=True)
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/vocabulary.py", label="Vocabulary", icon="🈶")
    st.page_link("pages/listening.py", label="Listening", icon="🎧")
    st.page_link("pages/structres.py", label="Structures", icon="🧩")

st.title("Vocabulary 🈶")

# Show the vocabulary table (row numbers start at 1)
df = pd.read_csv("U2 Chinese Simplified Set 1.csv")
df.index = df.index + 1
st.dataframe(df, use_container_width=True)


st.button("Ready for the test? Click here to go to practice writing vocabulary!", on_click=lambda: st.switch_page("pages/Vocabtest.py") )

