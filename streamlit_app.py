import streamlit as st

prompt = st.chat_input("Say something")

if prompt:
    paragraphs = prompt.split("\n")  # 改行文字でテキストを分割する
    for paragraph in paragraphs:
        st.write(f"User has sent the following prompt: {paragraph}")  # 各段落を新しい段落として表示する
