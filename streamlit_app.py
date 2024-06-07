import streamlit as st
a = ["アメリカ合衆国"]
b = ["中華人民共和国"]
c = ["日本国"]
st.title("$お試しだよ！$")
kensaku = st.text_input("検索")
st.write("以下の中から検索してください")
st.write("一覧：アメリカ合衆国,中華人民共和国，日本国")

if a:
    st.write("自由の国！")
if b:
    st.write("中国料理うまい！")
if c:
    st.write("我が国！")


