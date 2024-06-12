import streamlit as st
import pandas as pd
import numpy as np
import openpyxl

# タイトルと説明
st.title("国名、首都、座標検索")
a = st.text_input("国名を検索")

# データをロードする
@st.cache
def load_data():
    return pd.read_excel("1234.xlsx")

countries_df = load_data()

# システム的なもの
selected_country = countries_df[countries_df["国名"] == a].iloc[0]
usa_df = pd.DataFrame({
    'lat': [(selected_country["緯度"])],  # ワシントンDCの緯度
    'lon': [(selected_country["経度"])]  # ワシントンDCの経度
   })

if any(countries_df["国名"] == a):
    st.write("国名:", selected_country["国名"])
    st.write("首都:", selected_country["首都"])
    
    # st.map() を使用して座標を地図上に表示
    st.map(usa_df)
else:
    st.write("検索結果なし")
