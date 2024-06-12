import streamlit as st
import pandas as pd
import time

# タイトルと説明
st.title("世界検索")
st.write("好きな国家を検索して :red[知識] をつけましょう！")
a = st.text_input("国名を検索(入ってない国がある可能性があるので気をつけてください。)")

# データをロードする
@st.cache
def load_data():
    return pd.read_excel("2345.xlsx")

countries_df = load_data()

# システム的なもの
if any(countries_df["国名"] == a):
    with st.spinner("検索中....."):
     time.sleep(1)
    st.success('完了！')

    selected_country = countries_df[countries_df["国名"] == a].iloc[0]
    st.write("国名:", selected_country["国名"])
    st.write("首都:", selected_country["首都"])

    # st.map() を使用して座標を地図上に表示
    st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=1)
else:
    st.write("検索結果なし")
