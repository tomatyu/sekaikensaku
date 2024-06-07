import streamlit as st
st.title("$お試しだよ！$")
a = st.text_input("以下の国を検索してね")
st.write("例：アメリカ合衆国,中華人民共和国，日本国")

if st.write("日本国"):
    st.write("我が国！")
