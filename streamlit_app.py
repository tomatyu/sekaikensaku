import streamlit as st
import pandas as pd
import numpy as np

#　タイトルと説明
st.title("世界検索")
a = st.text_input("国を検索(対応していない国もあります)")

# データをロードする
@st.cache
def b():
    return pd.read_excel("1234.xlsx")

words_df = b()

#システム的なもの

if any([f"{a}" == b for v in a]):
    st.write(b)
else:
    st.write("検索結果なし")