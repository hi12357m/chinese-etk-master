import streamlit as st
from openai import OpenAI
import threading
import queue
import pandas as pd

st.set_option("client.showSidebarNavigation", False)

with st.sidebar:
    st.markdown("""
    <h2 style="text-align:center;">
         Menu
    </h2>
    """, unsafe_allow_html=True)

    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/vocabulary.py", label="Vocabulary", icon="🈶")
    st.page_link("pages/sentences.py", label="Sentences", icon="📝")
    st.page_link("pages/structres.py", label="Structures", icon="🧩")

st.title("Sentence Structures 🗣️")

st.caption("This page is still in development. For any problems regarding the AI feedback, please contact 310406@hkis.edu.hk")
st.caption("This page is powered by AI systems that may be unstable with high user counts. Please use the system responsibly and avoid using the AI for no Chinese academic reason.")
st.caption("We recommend using a word from the vocabulary list at the bottom to train yourself for the ETK test.")

# API setup
BASE_URL = "https://integrate.api.nvidia.com/v1"
MODELS = [
    "google/gemma-4-31b-it",
    "nvidia/nemotron-3.5-bolt-e4b"
]

structures = {
    "之所以……是因為……": "之所以我遲到，是因為下雨了。",
    "此外": "我喜歡吃蘋果，此外我也喜歡吃香蕉。",
    "根據": "根據天氣預報，明天會下雨。",
    "不光……還……": "這家餐廳不光好吃，還很便宜。",
}

choice = st.selectbox("Choose a sentence structure", list(structures.keys()))
st.write("Example: " + structures[choice])
sentence = st.text_area("Write your own sentence using this structure:")

# Ask the AI in the background
def ask_ai(prompt, q):
    # 15-second timeout per model (good for cloud cold starts)
    client = OpenAI(
        base_url=BASE_URL, 
        api_key=st.secrets["NVIDIA_API_KEY"],
        timeout=15.0, 
        max_retries=0 
    )
    
    for model in MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                stream=True
            )
            q.put(response)
            return
        except Exception as e:
            print(f"Model {model} failed or timed out: {e}")
            continue
            
    q.put("ERROR")

# button logic
if st.button("Check my sentence"):
    if sentence.strip() == "":
        st.warning("Please write a sentence first.")
    else:
        prompt = (
            "You are a friendly Chinese teacher. The student must use the structure " + choice + ". "
            "Their sentence is: " + sentence + "\n\n"
            "Reply in English:\n"
            "1. Did they use the structure correctly?\n"
            "2. Any grammar mistakes\n"
            "3. Corrected version in Traditional Chinese\n"
            "4. One short tip. Also make sure all responses are constructive feedback."
        )

        q = queue.Queue()
        t = threading.Thread(target=ask_ai, args=(prompt, q))
        t.start()

        with st.spinner("Asking the smart teacher... This may take a few moments."):
            try:
                # Wait max 12 seconds for the background thread to finish
                stream = q.get(timeout=30)
                
                if stream == "ERROR":
                    st.error("The AI models are currently unavailable. Please try again later.")
                else:
                    full_text = ""
                    placeholder = st.empty()
                    
                    for chunk in stream:
                        if chunk.choices and chunk.choices[0].delta.content:
                            full_text += chunk.choices[0].delta.content
                            placeholder.markdown(full_text)
                            
                    st.subheader("Teacher feedback")
                    st.write(full_text)

            except queue.Empty:
                st.warning("⚠️ The AI is taking too long to respond. Please try again.")
st.caption("Simplified")
df = pd.read_csv("U2 Chinese Simplified Set 1.csv")
df.index = df.index + 1
st.dataframe(df, use_container_width=True)

st.write("")
st.caption("Traditional")

df = pd.read_csv("U2 Chinese Traditional Set 1.csv")
df.index = df.index + 1
st.dataframe(df, use_container_width=True)
