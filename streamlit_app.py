import streamlit as st
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt

# タイトルと説明
st.title("世界検索")

countries = ["USA", "Japan", "China", "Russia", "UK"]
gdp_data = pd.DataFrame(np.random.rand(5, 1) * 1000, columns=["GDP"], index=countries)

col1, col2, col3 = st.columns(3)

if col1.button("国を検索する"):
 st.title("国検索")
 

if col2.button("go"):
    





# グラフの作成
 plt.figure(figsize=(10, 6))
 plt.bar(gdp_data.index, gdp_data["GDP"], color=['blue', 'green', 'red', 'purple', 'orange'])
 plt.title('GDP of Countries')
 plt.xlabel('Country')
 plt.ylabel('GDP (Billion $)')
 plt.grid(True)
 plt.show()


if col3.button("hy"):
    st.write("ey")



st.write("好きな国を検索して、:red[知識] を見つけましょう！")
a = st.text_input("国名を検索してください（適用していない国もあります）")

# データをロードする
@st.cache
def load_data():
    return pd.read_excel("17.xlsx")

countries_df = load_data()

# システム的なもの
if any(countries_df["国名"] == a):
    with st.spinner("検索中....."):
        time.sleep(1)

    selected_country = countries_df[countries_df["国名"] == a].iloc[0]
    st.write("国名:", selected_country["国名"])
    st.write("首都:", selected_country["首都"])
    st.write("概要:", selected_country["概要"])
    st.write("GDP:", selected_country["GDP"])

    # st.map() を使用して座標を地図上に表示
    st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=2)

else:
    st.write("検索結果なし")
