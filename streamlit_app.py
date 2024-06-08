import streamlit as st
st.title("$お試しだよ！$")
a = st.selectbox(
    "検索",
    ("アメリカ合衆国", "中華人民共和国", "日本"))
st.write("以下の中から検索して下さい")
st.write ("アメリカ合衆国", "中華人民共和国", "日本")
st.write(f"{a}です")
if any([f"{a}" == "アメリカ合衆国" for v in a]):
    st.write("自由の国！")
elif any([f"{a}" == "中華人民共和国" for v in a]):
    st.write("中華料理うまい")
elif any([f"{a}" == "日本" for v in a]):
    st.write("我が国!")
else:
    st.write("検索結果なし")


