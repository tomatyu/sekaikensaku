import streamlit as st
import pandas as pd
import numpy as np

#　タイトルと説明
st.title("世界検索")
a = st.text_input("国を検索(対応していない国もあります)")

# データをロードする
@st.cache
def load_data():
    return pd.read_excel()

words_df = load_data()

#システム的なもの

if any([f"{a}" == load_data for v in a]):
    st.write(load_data)
else:
    st.write("検索結果なし")