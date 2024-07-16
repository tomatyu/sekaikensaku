import streamlit as st
import pandas as pd
import plotly.express as px

# データを初期読み込みする
@st.cache
def load_data():
    return pd.read_excel("28.xlsx")

@st.cache
def load_data2():
    return pd.read_excel("25.xlsx")

@st.cache
def load_data3():
    return pd.read_excel("27.xlsx")

# Streamlitアプリケーションのセットアップ
st.title("世界検索")
st.write("好きな国を検索して、:red[知識] を見つけましょう！")

# データフレームを読み込む
countries_df = load_data()
df2 = load_data2()
df3 = load_data3()

# 初期の7大国のGDPデータを定義する
gdp_data = {
    'Country': ['アメリカ合衆国', '中国', '日本', 'ドイツ', 'イギリス', 'フランス', 'インド'],
    'GDP': [21.43, 14.34, 5.08, 3.84, 2.83, 2.71, 2.87]
}

# メインメニューの選択
option = st.sidebar.selectbox(
    "メニューを選択してください",
    ['ホーム', '国の詳細検索', '国のGDP検索']
)

# メインメニューの条件分岐
if option == 'ホーム':
    st.write(":blue[世界検索へようこそ！！]")
    st.write("ここでは様々な国を検索することができます")
    st.write("早速、左のメニューから選択して楽しみましょう！！")

elif option == '国の詳細検索':
    st.write("国名を入力してください（適用していない国もあります）")
    a = st.chat_input("国を検索してください")
    if a.strip() != "国を検索してください":
            selected_country = countries_df[countries_df["国名"] == country_name]
            if not selected_country.empty:
                selected_country = selected_country.iloc[0]
                st.write("国名:", selected_country["国名"])
                st.write("首都:", selected_country["首都"])
                st.write("GDP:", selected_country["GDP"])
                st.write("概要:", selected_country["概要"])

                # 地図表示
                st.subheader('国の地図')
                st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=2)

                # 選択された国のGDPデータをgdp_dataに追加する
                if selected_country["国名"] not in gdp_data['Country']:
                    gdp_data['Country'].append(selected_country["国名"])
                    gdp_data['GDP'].append(selected_country["GDP"])

                st.session_state['gdp_data'] = gdp_data
            else:
                st.write("検索結果なし")

elif option == '国のGDP検索':
    st.write('データソース: IMF')

    # データフレームから国のリストを取得
    countries_list = df3['国名2'].tolist()

    # 選択した国の入力
    selected_country = st.text_input('比較したい国を入力してください（例: USA, China, Japanなど）')

    selected_data = df3[df3['国名2'] == selected_country]

    # 大国のリスト（例として米国、中国、日本を指定）
    major_countries = ['アメリカ合衆国', '中国', '日本']

    # 新しく追加する国の入力
    new_country = st.text_input('新しく追加する国名を入力してください（例: ドイツ）')
    if new_country:
        st.write(":red[二つの国を必ず入力してください。]")

    # 新しく追加した国のGDPを取得
    if new_country:
        # 新旧の国を比較するグラフを描画
        comparison_data = df3[df3['国名2'].isin([selected_country, new_country] + major_countries)]
        fig_comparison = px.bar(comparison_data, x='国名2', y='GDP3', color='国名2',
                                labels={'GDP3': 'GDP (兆ドル)', '国名2': '国'})
        st.plotly_chart(fig_comparison)
    else:
        st.write("新しい国のデータが見つかりません。")
