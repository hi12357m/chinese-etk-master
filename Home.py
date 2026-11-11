import streamlit as st

st.set_page_config(
    page_title="Chinese ETK Master",
    page_icon="🐉",
    layout="wide"
)

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

div.st-key-vocab button:hover p {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

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


st.markdown("""
<h1 style="text-align:center;">
🐉 Chinese ETK Master
</h1>
""", unsafe_allow_html=True)


st.write("")

# Learning activities
with st.container(border=True):
    st.subheader("Choose a learning activity")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        if st.button("📚 Vocabulary", key="vocab", width="stretch"):
            st.switch_page("pages/vocabulary.py")

    with col2:
        if st.button("📝 Sentence", key="sentences", width="stretch", use_container_width=True):
            st.switch_page("pages/sentences.py")

    col3, col4 = st.columns(2, gap="medium")
