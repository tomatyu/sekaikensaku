import streamlit as st
import pandas as pd

# タイトルと説明
st.title("世界検索")
a = st.text_input("国を検索(対応していない国もあります)")

# データをロードする
@st.cache
def load_data():
    return pd.read_excel("1234.xlsx")

words_df = load_data()

# システム的なもの
if any(words_df["国"] == a):
    st.write(words_df[words_df["国"] == a])
else:
    st.write("検索結果なし")
