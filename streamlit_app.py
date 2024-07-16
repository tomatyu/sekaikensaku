import streamlit as st

# チャットインプットでユーザーからの入力を受け取る
prompt = st.text_area("Chat with ChatGPT", value="", height=150)

# ユーザーが入力した場合にのみ応答を生成する
if st.button("Send"):
    if prompt:
        # ここでは簡単に応答を設定しますが、実際のチャットボットロジックに置き換えてください
        response = f"User has sent the following prompt: {prompt}"
        
        # 応答を表示する
        st.text_area("ChatGPT's response", value=response, height=150)
