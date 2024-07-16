import streamlit as st

# 過去の入力を保持するリスト
past_prompts = []

while True:
    # チャットインプットでユーザーからの入力を受け取る
    prompt = st.text_input("Say something")

    # 入力があれば過去の入力リストに追加
    if prompt:
        past_prompts.append(prompt)

    # 過去の入力を段落ごとに表示
    for past_prompt in past_prompts:
        st.write(f"User has sent the following prompt: {past_prompt}")

    # 改行を挿入して区切りをつける
    st.markdown("---")

    # ブレーク条件
    if not st.button("Continue"):
        break
