import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

# データを初期読み込みする
@st.cache
def load_data():
    return pd.read_excel("18.xlsx")

# 国のデータを読み込む
countries_df = load_data()

# Streamlitアプリケーションのセットアップ
st.title("世界検索")
st.write("好きな国を検索して、:red[知識] を見つけましょう！")
a = st.text_input("国名を入力してください（適用していない国もあります）")
selected_country = countries_df[countries_df["国名"] == a].iloc[0]
# 初期の7大国のGDPデータを定義する
gdp_data = {
    'Country': [selected_country["国名"]],
    'GDP': [selected_country["GDP"]]
}

# 国検索ボタン
if st.button('国検索'):
    if any(countries_df["国名"] == a):
        with st.spinner("検索中....."):
            time.sleep(1)

        selected_country = countries_df[countries_df["国名"] == a].iloc[0]
        st.write("国名:", selected_country["国名"])
        st.write("首都:", selected_country["首都"])
        st.write("GDP:", selected_country["GDP"])
        st.write("概要:", selected_country["概要"])

        # 選択された国のGDPデータをgdp_dataに追加する
        if selected_country["国名"] not in gdp_data['Country']:
            gdp_data['Country'].append(selected_country["国名"])
            gdp_data['GDP'].append(selected_country["GDP"])

        # 地図表示
        st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=2)
    else:
        st.write("検索結果なし")

# 国のGDP検索ボタン
if st.button('国のGDP検索'):
    # gdp_dataをDataFrameに変換する
    df = pd.DataFrame(gdp_data)

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

    # 選択された国を異なる色でハイライトする
    if a.strip() != "" and a in df['Country'].values:
        idx = df.index[df['Country'] == a][0]
        ax.bar(df['Country'][idx], df['GDP'][idx], color='blue')  # 選択された国を青でハイライト

    # 軸ラベルとタイトルの設定
    ax.set_xlabel('国')
    ax.set_ylabel('GDP（兆ドル単位）')
    ax.set_title('主要国のGDP')

    # x軸ラベルの回転
    plt.xticks(rotation=45)

    # グラフをStreamlitに表示
    st.pyplot(fig)
