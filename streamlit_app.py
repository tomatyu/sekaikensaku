import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む関数
@st.cache
def load_data():
    # Excelファイルからデータを読み込む（ファイルパスを適宜変更する）
    return pd.read_excel("17.xlsx")

# 7大国のGDPデータを読み込む
gdp_data = load_data()

# タイトルと説明
st.title("世界検索")
st.write("好きな国を検索して、:red[知識] を見つけましょう！")
a = st.text_input("国名を入力してください（適用していない国もあります）")

# 左側のカラムに「国検索」ボタンを配置
if st.button('国検索'):
    if any(gdp_data["国名"] == a):
        with st.spinner("検索中....."):
            time.sleep(1)

        selected_country = gdp_data[gdp_data["国名"] == a].iloc[0]
        st.write("国名:", selected_country["国名"])
        st.write("GDP:", selected_country["GDP"])
    else:
        st.write("検索結果なし")

# 右側のカラムに「国のGDP検索」ボタンを配置
if st.button('国のGDP検索'):
    # Streamlitアプリケーションの作成
    st.title('7大国のGDPをバーチャートで表示するアプリ')

    # データフレームの表示（オプション）
    if st.checkbox('生データを表示する'):
        st.write(gdp_data)

    # グラフの作成
    st.subheader('7大国のGDPの比較')

    # グラフをプロット
    fig, ax = plt.subplots()
    ax.bar(gdp_data['国名'], gdp_data['GDP'], color='blue')  # バープロットを使用する例（青色で表示）

    # グラフの軸ラベルとタイトルの設定
    ax.set_xlabel('Country')
    ax.set_ylabel('GDP (in trillion $)')
    ax.set_title('GDP of Major Countries')

    # x軸ラベルの回転
    plt.xticks(rotation=45)

    # グラフをStreamlitに表示
    st.pyplot(fig)
