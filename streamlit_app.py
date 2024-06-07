import streamlit as st
st.title("$お試しだよ！$")
a = ["アメリカ合衆国"]
b = ["中華人民共和国"]
c = ["日本国"]
d = st.text_input("検索")
st.write("以下の中から検索してください")
st.write("一覧：アメリカ合衆国,中華人民共和国，日本国")

if d == a:
    st.write("自由の国！")
elif d == b:
    st.write("中華料理うまい")
elif d == c:
    st.write("我が国!")
else:
    st.write("検索結果なし")


