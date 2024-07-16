import streamlit as st
import openai

# OpenAI APIの設定
openai.api_key = "YOUR_OPENAI_API_KEY"

# チャットインプットでユーザーからの入力を受け取る
prompt = st.text_area("Chat with ChatGPT", value="", height=150)

# ユーザーが入力した場合にのみ応答を生成する
if st.button("Send"):
    if prompt:
        # OpenAI APIを使用して応答を生成する
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50
        )
        
        # 応答を表示する
        st.text_area("ChatGPT's response", value=response.choices[0].text.strip(), height=150)
