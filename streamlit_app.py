import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

# 7大国のGDPデータを定義
gdp_data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'UK', 'India', 'France'],
    'GDP': [23.5, 14.3, 5.1, 4.2, 2.9, 2.8, 2.7]
}

# タイトルと説明
st.title("世界検索")
st.write("好きな国を検索して、:red[知識] を見つけましょう！")
a = st.text_input("国名を入力してください（適用していない国もあります）")
col1, col2 = st.beta_columns(2)

# 左側のカラムにボタン1を配置
if col1.button('国検索'):
    # データをロードする
 st.cache
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

# 右側のカラムにボタン2を配置
if col2.button('国のGDP検索'):
    # GDPデータをDataFrameに変換
df = pd.DataFrame(gdp_data)

# Streamlitアプリケーションの作成
st.title('7大国のGDPをバーチャートで表示するアプリ')

# データフレームの表示（オプション）
if st.checkbox('Show raw data'):
    st.write(df)

# グラフの作成
st.subheader('7大国のGDPの比較')

# グラフをプロット
fig, ax = plt.subplots()
ax.bar(df['Country'], df['GDP'], color='blue')  # バープロットを使用する例（青色で表示）

# グラフの軸ラベルとタイトルの設定
ax.set_xlabel('Country')
ax.set_ylabel('GDP (in trillion $)')
ax.set_title('GDP of Major Countries')

# x軸ラベルの回転
plt.xticks(rotation=45)

# グラフをStreamlitに表示
st.pyplot(fig)


