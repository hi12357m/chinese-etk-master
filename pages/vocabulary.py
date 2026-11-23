import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO


st.set_option("client.showSidebarNavigation", False)

# Set page config must be the first Streamlit command
st.set_page_config(page_title="Vocabulary Master", page_icon="🈶", layout="wide")

st.markdown("""
<style>
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

# Sidebar menu
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>Menu</h2>", unsafe_allow_html=True)
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/vocabulary.py", label="Vocabulary", icon="🈶")
    st.page_link("pages/listening.py", label="Listening", icon="🎧")
    st.page_link("pages/sentences.py", label="Sentences", icon="📝")
    st.page_link("pages/structres.py", label="Structures", icon="🧩")

st.title("Vocabulary 🈶")

# Load the CSV
df = pd.read_csv("U2 Chinese Simplified Set 1.csv")
df.columns = df.columns.str.strip() 

# Create a display version of the table with row numbers starting at 1
df_display = df.copy()
df_display.index = df_display.index + 1
st.dataframe(df_display, use_container_width=True)

st.divider()
st.subheader("🔊 Listen to Pronunciation")

# Create a list of words like "饮食 (yǐn shí)" for the dropdown
word_options = []

# We loop through the ORIGINAL df (which has 0-based indexing) to avoid the KeyError
for char, pinyin in zip(df["CHARACTER"], df["Pinyin"]):
    word_text = str(char) + " (" + str(pinyin) + ")"
    word_options.append(word_text)

# Dropdown menu for user to pick a word
selected_option = st.selectbox("Choose a word to hear:", word_options)

if st.button("Play Audio"):
    # Extract just the Chinese characters (before the space)
    text_to_speak = selected_option.split(" ")[0]

    try:
        # Generate audio (zh-tw is Mandarin, zh-yue is Cantonese)
        tts = gTTS(text=text_to_speak, lang='zh-tw')
        
        # Save audio to memory
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        
        # Display the audio player
        st.audio(audio_bytes, format="audio/mp3")
        
    except Exception as e:
        st.error("Could not load audio. Check your internet connection.")

st.divider()

st.button("Ready for the test? Click here to go to practice writing vocabulary!", on_click=lambda: st.switch_page("pages/Vocabtest.py"))