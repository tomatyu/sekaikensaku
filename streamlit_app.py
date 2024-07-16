import streamlit as st

past_prompts = []

while True:
    prompt = st.text_input("Say something", key=len(past_prompts))

    if prompt:
        past_prompts.append(prompt)

    for past_prompt in past_prompts:
        st.write(f"User has sent the following prompt: {past_prompt}")

    st.markdown("---")

    if not st.button("Continue"):
        break
