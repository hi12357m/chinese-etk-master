import streamlit as st
import pandas as pd
import random

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

st.title("Fill in the blank ✏️")

# Read the words and sentences from the CSV
df = pd.read_csv("U2 Chinese Simplified Set 2.csv", skipinitialspace=True)

words = []
sentences = []
for i in range(len(df)):
    words.append(str(df["CHARACTER"][i]).strip())
    sentences.append(str(df["Sentence"][i]).strip())

# Set up the saved values the first time the page loads
if "sent_filled" not in st.session_state:
    # Pick 14 random words and remember them
    picks = random.sample(range(len(words)), 14)
    st.session_state.sent_words = []
    st.session_state.sent_sentences = []
    for i in picks:
        st.session_state.sent_words.append(words[i])
        st.session_state.sent_sentences.append(sentences[i])

    bank = st.session_state.sent_words.copy()
    random.shuffle(bank)
    st.session_state.sent_bank = bank
    st.session_state.sent_selected = None
    st.session_state.sent_filled = [None] * 14
    st.session_state.sent_checked = False

# From now on, use only the 14 saved words
words = st.session_state.sent_words
sentences = st.session_state.sent_sentences

bank = st.session_state.sent_bank
selected = st.session_state.sent_selected
filled = st.session_state.sent_filled
checked = st.session_state.sent_checked

# Word bank (5 buttons per row)
st.subheader("Word bank")
per_row = 5
for start in range(0, len(bank), per_row):
    bank_cols = st.columns(per_row)
    for j in range(per_row):
        i = start + j
        if i >= len(bank):
            break

        word = bank[i]

        # Colour the button if it is the selected word
        if word == selected:
            button_type = "primary"
        else:
            button_type = "secondary"

        clicked = bank_cols[j].button(
            word,
            key="bank_" + str(i),
            type=button_type,
            disabled=(word in filled or checked),   # greyed out once it is used
            use_container_width=True,
        )

        if clicked:
            st.session_state.sent_selected = word
            st.rerun()

st.divider()

# Sentences with blanks
for i in range(len(words)):
    # Split the sentence into the part before and after the word
    before, middle, after = sentences[i].partition(words[i])

    col1, col2, col3 = st.columns([4, 2, 4])
    col1.write(str(i + 1) + ". " + before)

    # The blank shows the word that was placed, or ＿＿＿ if empty
    if filled[i] is None:
        blank_label = "＿＿＿"
    else:
        blank_label = filled[i]

    clicked = col2.button(
        blank_label,
        key="blank_" + str(i),
        disabled=checked,
        use_container_width=True,
    )
    col3.write(after)

    if clicked:
        if filled[i] is None and selected is not None:
            # Put the selected word into this blank
            filled[i] = selected
            st.session_state.sent_selected = None
        elif filled[i] is not None:
            # Take the word back out of the blank
            filled[i] = None
        st.rerun()

st.divider()

# Check the answers
if not checked:
    if st.button("Check answers"):
        st.session_state.sent_checked = True
        st.rerun()
else:
    score = 0
    for i in range(len(words)):
        if filled[i] == words[i]:
            score = score + 1
            st.success(str(i + 1) + ". Correct!")
        else:
            st.error(str(i + 1) + ". The answer is " + words[i])

    st.write("Score: " + str(score) + " / " + str(len(words)))

    if st.button("Try again"):
        # Delete the saved values so the page picks 14 new words
        del st.session_state.sent_filled
        st.rerun()