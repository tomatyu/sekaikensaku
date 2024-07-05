import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

# データを初期読み込みする
@st.cache
def load_data():
    return pd.read_excel("18.xlsx")

# Streamlitアプリケーションのセットアップ
st.title("世界検索")
st.write("好きな国を検索して、:red[知識] を見つけましょう！")

# データフレームを読み込む
countries_df = load_data()

# 入力された国名を取得
a = st.text_input("国名を入力してください（適用していない国もあります）")

# 国検索ボタン
if st.button('国検索'):
    if a.strip() != "":
        selected_country = countries_df[countries_df["国名"] == a]

        if not selected_country.empty:
            selected_country = selected_country.iloc[0]
            st.write("国名:", selected_country["国名"])
            st.write("首都:", selected_country["首都"])
            st.write("GDP:", selected_country["GDP"])
            st.write("概要:", selected_country["概要"])

            # 地図表示
            st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=2)

            # GDPデータを更新
            gdp_data = {
                'Country': [],
                'GDP': []
            }

            if 'Country' in st.session_state:
                gdp_data['Country'] = st.session_state['Country']
                gdp_data['GDP'] = st.session_state['GDP']

            if selected_country["国名"] not in gdp_data['Country']:
                gdp_data['Country'].append(selected_country["国名"])
                gdp_data['GDP'].append(selected_country["GDP"])

            st.session_state['Country'] = gdp_data['Country']
            st.session_state['GDP'] = gdp_data['GDP']
        else:
            st.write("検索結果なし")

# 国のGDP検索ボタン
if st.button('国のGDP検索'):
    if 'Country' in st.session_state and len(st.session_state['Country']) > 0:
        df = pd.DataFrame({
            'Country': st.session_state['Country'],
            'GDP': st.session_state['GDP']
        })

        # GDPの比較用のStreamlitアプリケーションのセットアップ
        st.title('7大国のGDPをバーチャートで表示するアプリ')

        # 生データ表示（オプション）
        if st.checkbox('生データを表示する'):
            st.write(df)

        # バーチャートのプロット
        st.subheader('7大国のGDPの比較')

        # 図と軸の作成
        fig, ax = plt.subplots()

        # バーチャートのプロット
        ax.bar(df['Country'], df['GDP'], color='red')  # 青色でバープロットする例

        # 軸ラベルとタイトルの設定
        ax.set_xlabel('Country')
        ax.set_ylabel('GDP (trillion dollars)')
        ax.set_title('GDP of Major Countries')

        # x軸ラベルの回転
        plt.xticks(rotation=45)

        # グラフをStreamlitに表示
        st.pyplot(fig)
    else:
        st.write("GDPデータがありません。国検索ボタンを使用して国のデータを追加してください。")
