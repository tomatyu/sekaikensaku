import streamlit as st
import pandas as pd
import numpy as np

st.title("$お試しだよ！$")
a = st.text_input("検索",)
st.write("以下の中から検索して下さい")
st.write ("アメリカ合衆国", "中華人民共和国", "日本")
if any([f"{a}" == "アメリカ合衆国" for v in a]):
    st.write("国名:アメリカ合衆国")
    st.write("首都:ワシントンDC")
    df = pd.DataFrame({
    'lat': [38.5342],
    'lot': [77.0212]
    })
    st.map(df)
elif any([f"{a}" == "中華人民共和国" for v in a]):
    st.write("中華料理うまい")
elif any([f"{a}" == "日本" for v in a]):
    st.write("我が国!")
else:
    st.write("検索結果なし")


