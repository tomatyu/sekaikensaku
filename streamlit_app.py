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
    return pd.read_excel("countries_data.xlsx")

countries_df = load_data()

# システム的なもの

if any(countries_df["国名"] == a):
    selected_country = countries_df[countries_df["国名"] == a].iloc[0]
    st.write("国名:", selected_country["国名"])
    st.write("首都:", selected_country["首都"])
    st.write("座標:", selected_country["座標"])
    
    # st.map() を使用して座標を地図上に表示
    st.map(selected_country["座標"])
else:
    st.write("検索結果なし")
