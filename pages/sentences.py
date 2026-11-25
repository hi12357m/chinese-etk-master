import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO


st.set_option("client.showSidebarNavigation", False)

st.markdown("""
<style>
/* All buttons */
div[data-testid="stButton"] button {
    width: 100%;
    height: 180px;
    border-radius: 24px;
    background-color: white;
    color: #26324B;
    border: 2px solid #DCE5F1;
    font-size: 32px !important;
    font-weight: bold;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.08);
}

/* Button text */
div[data-testid="stButton"] button p {
    font-size: 32px !important;
    font-weight: 700 !important;
}

/* Simplified button */
div.st-key-simplified button {
    background-color: #4dfffc !important;
    color: white !important;
    border-color: #4dfffc !important;
}

div.st-key-simplified button p {
    color: white !important;
}

/* General hover effect */
div[data-testid="stButton"] button:hover {
    background-color: #E6F9FC;
    border: 2px solid #06B6D4;
    color: #0891B2;
}

/* Simplified hover effect */
div.st-key-simplified button:hover {
    background-color: #44c2c0 !important;
    color: white !important;
    border-color: #44c2c0 !important;
}

div.st-key-simplified button:hover p {
    color: white !important;
}

/* Traditional button */
div.st-key-traditional button {
    background-color: #f7367d !important;
    color: white !important;
    border-color: #f7367d !important;
}

div.st-key-traditional button p {
    color: white !important;
}


/* Traditional hover effect */
div.st-key-traditional button:hover {
    background-color: #c92a61 !important;
    color: white !important;
    border-color: #c92a61 !important;
}

div.st-key-traditional button:hover p {
    color: white !important;
}


</style>



""", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>Menu</h2>", unsafe_allow_html=True)
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/vocabulary.py", label="Vocabulary", icon="🈶")
    st.page_link("pages/sentences.py", label="Sentences", icon="📝")
    st.page_link("pages/structres.py", label="Structures", icon="🧩")

st.title("Sentences ")



with st.container(border=True):
    st.subheader("Choose your preferred option to access sentences page")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        if st.button("Traditional", key="vocab", width="stretch"):
            st.switch_page("pages/sentencestraditional.py")

    with col2:
        if st.button("Simplified", key="simplified", width="stretch", use_container_width=True):
            st.switch_page("pages/sentencessimplified.py")