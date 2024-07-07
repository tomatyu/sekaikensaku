import streamlit as st
import pandas as pd
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

# 初期の7大国のGDPデータを定義する
gdp_data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'UK', 'France', 'India'],
    'GDP': [21.43, 14.34, 5.08, 3.84, 2.83, 2.71, 2.87]
}

# sidebarにボタンを配置
tab = st.sidebar.radio("選択してください", ['国検索', '国のGDP検索'])

if tab == '国検索':
    if st.button('国を表示'):
        if a.strip() != "":
            selected_country = countries_df[countries_df["国名"] == a]

            if not selected_country.empty:
                selected_country = selected_country.iloc[0]
                st.write("国名:", selected_country["国名"])
                st.write("首都:", selected_country["首都"])
                st.write("GDP:兆ドル", selected_country["GDP"])
                st.write("概要:", selected_country["概要"])
                st.write("英語表記:",selected_country["英語"])

                # 地図表示
                st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=2)

                # 選択された国のGDPデータをgdp_dataに追加する
                if selected_country["国名"] not in gdp_data['Country']:
                    gdp_data['Country'].append(selected_country["国名"])
                    gdp_data['GDP'].append(selected_country["GDP"])

                # session_stateに保存
                st.session_state['gdp_data'] = gdp_data
            else:
                st.write("検索結果なし")

elif tab == '国のGDP検索':
    if st.button('国のGDPを表示'):
        if 'gdp_data' in st.session_state:
            gdp_data = st.session_state['gdp_data']

            df = pd.DataFrame(gdp_data)

            # バーチャートのプロット
            st.subheader('7大国のGDPの比較')

            # 図と軸の作成
            fig, ax = plt.subplots()

            # バーチャートのプロット
            bars = ax.bar(df['Country'], df['GDP'], color=['red' if c != a else 'blue' for c in df['Country']])  # 赤色でバープロットする例

            # 軸ラベルとタイトルの設定
            ax.set_xlabel('Country')
            ax.set_ylabel('GDP (trillion dollars)')
            ax.set_title('GDP of Major Countries')

            # x軸ラベルの回転
            plt.xticks(rotation=45)

            # グラフをStreamlitに表示
            st.pyplot(fig)
            st.write("選択した国が青色で表示されています")
        else:
            st.write("国を検索してから、国のGDPデータを追加してください。")