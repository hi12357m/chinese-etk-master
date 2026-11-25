import streamlit as st
import pandas as pd
import random

st.set_option("client.showSidebarNavigation", False)

df = pd.read_csv("U2 Chinese Traditional Set 1.csv")

df.columns = df.columns.str.strip()

all_pinyin = df["Pinyin"].tolist()



df.columns = df.columns.str.strip()

if "random_pinyin" not in st.session_state:
    st.session_state.random_pinyin = random.choice(all_pinyin) 


with st.container(border=True):
    st.write("Here is your Pinyin Word, write it down and check it by clicking the button below:")
    st.header(st.session_state.random_pinyin)

if st.button("Get another word"):
        st.session_state.random_pinyin = random.choice(all_pinyin)
        st.rerun()


if st.button("Check my answer"):
    # Get the corresponding Chinese character for the random Pinyin
    correct_character = df.loc[df["Pinyin"] == st.session_state.random_pinyin, "CHARACTER"].values[0]
    #fetch -> locate -> stay with session state -> get the first value of character csv
    st.write(f"Correct answer: {correct_character}")

st.button("Leave", on_click=lambda: st.switch_page("pages/vocabulary.py") )
    


