import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Matplotlibの設定を変更
matplotlib.use('Agg')  # 非対話モードに設定

# 七大国のGDPデータ（2023年の予測値）
gdp_data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'UK', 'France', 'Italy'],
    'GDP (trillion USD)': [23.49, 18.47, 5.37, 4.90, 3.23, 3.08, 2.48]
}

# DataFrameを作成
df = pd.DataFrame(gdp_data)

# Streamlitアプリケーションの設定
st.title('七大国のGDP')

# テーブルを表示import streamlit as st
import pandas as pd
import time

# タイトルと説明
st.title("世界検索")
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
    st.write("GDP:", selected_country["GDP"])
    st.write("概要:", selected_country["概要"])

    # st.map() を使用して座標を地図上に表示
    st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=2)
else:
    st.write("検索結果なし")

st.write(df)

# グラフを表示
fig, ax = plt.subplots()
ax.bar(df['Country'], df['GDP (trillion USD)'], color='skyblue')
ax.set_xlabel('Country')
ax.set_ylabel('GDP (trillion USD)')
ax.set_title('七大国のGDP')

# グラフをStreamlitで表示
st.pyplot(fig)

