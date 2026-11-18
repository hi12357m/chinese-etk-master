import streamlit as st
import pandas as pd
import random

# sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>Menu</h2>", unsafe_allow_html=True)
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/vocabulary.py", label="Vocabulary", icon="🈶")
    st.page_link("pages/listening.py", label="Listening", icon="🎧")
    st.page_link("pages/sentences.py", label="Sentences", icon="📝")
    st.page_link("pages/structres.py", label="Structures", icon="🧩")

st.title("Fill in the blank ✏️")

# read csv
df = pd.read_csv("U2 Chinese Simplified Set 2.csv", skipinitialspace=True)

# setup the game
if "setup_done" not in st.session_state:
    st.session_state.chosen_words = []
    st.session_state.chosen_sents = []
    
    # grab 14 random rows
    random_rows = random.sample(range(len(df)), 14)
    
    for i in random_rows:
        st.session_state.chosen_words.append(df["CHARACTER"][i])
        st.session_state.chosen_sents.append(df["Sentence"][i])
        
    # make word bank
    st.session_state.my_bank = list(st.session_state.chosen_words)
    random.shuffle(st.session_state.my_bank)
    
    # create 14 empty spaces for the blanks
    st.session_state.blanks = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    st.session_state.selected_word = ""
    st.session_state.is_checked = False
    st.session_state.setup_done = True


# word bank section
st.subheader("Word bank")

# create 5 columns for the buttons
cols = st.columns(5)

for i in range(len(st.session_state.my_bank)):
    word = st.session_state.my_bank[i]
    
    # figure out which column to put the button in
    if i < 5:
        col = cols[0]
    elif i < 10:
        col = cols[1]
    elif i < 15:
        col = cols[2]
    else:
        col = cols[3]

    # button color
    if word == st.session_state.selected_word:
        button_style = "primary"
    else:
        button_style = "secondary"

    # disable if already used
    if word in st.session_state.blanks:
        cant_click = True
    elif st.session_state.is_checked == True:
        cant_click = True
    else:
        cant_click = False

    if col.button(word, key="w_btn_" + str(i), type=button_style, disabled=cant_click, use_container_width=True):
        st.session_state.selected_word = word
        st.rerun()

st.divider()

# sentences section
for i in range(14):
    sentence = st.session_state.chosen_sents[i]
    target_word = st.session_state.chosen_words[i]
    
    # split sentence into two parts
    parts = sentence.split(target_word)
    before = parts[0]
    
    # get the after part if it exists
    if len(parts) > 1:
        after = parts[1]
    else:
        after = ""

    # make columns for layout
    col1, col2, col3 = st.columns([4, 2, 4])
    
    col1.write(str(i + 1) + ". " + before)
    
    # check what to put in the blank button
    if st.session_state.blanks[i] == "":
        blank_text = "＿＿＿"
    else:
        blank_text = st.session_state.blanks[i]
        
    if col2.button(blank_text, key="b_btn_" + str(i), disabled=st.session_state.is_checked, use_container_width=True):
        # if blank is empty and we have a word selected, fill it
        if st.session_state.blanks[i] == "" and st.session_state.selected_word != "":
            st.session_state.blanks[i] = st.session_state.selected_word
            st.session_state.selected_word = ""
        # if blank has a word, empty it
        elif st.session_state.blanks[i] != "":
            st.session_state.blanks[i] = ""
        st.rerun()
        
    col3.write(after)

st.divider()

# check answers section
if st.session_state.is_checked == False:
    if st.button("Check answers"):
        st.session_state.is_checked = True
        st.rerun()
else:
    score = 0
    for i in range(14):
        if st.session_state.blanks[i] == st.session_state.chosen_words[i]:
            score = score + 1
            st.success(str(i + 1) + ". Correct!")
        else:
            st.error(str(i + 1) + ". The answer is " + st.session_state.chosen_words[i])
            
    st.write("Score: " + str(score) + " / 14")
    
    if st.button("Try again"):
        del st.session_state.setup_done
        st.rerun()