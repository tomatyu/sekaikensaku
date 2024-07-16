import streamlit as st
import pandas as pd
import plotly.express as px

def key(selected_country):
    bubble_style = '''
        <style>
            .bubble {
                position: relative;
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                text-align: right;
                margin: 10px 0;
                width: fit-content;
            }
            .bubble::after {
                content: '';
                position: absolute;
                top: 50%;
                left: -10px;
                border-style: solid;
                border-width: 10px 10px 10px 0;
                border-color: transparent #f0f0f0 transparent transparent;
                transform: translateY(-50%);
            }
        </style>
    '''
    bubble_html = f'''
        <div class="bubble">
            <div style="text-align: left;">
                <b>国名:</b> {selected_country["国名"]} <br>
                <b>首都:</b> {selected_country["首都"]} <br>
                <b>GDP:</b> {selected_country["GDP"]} <br>
                <b>概要:</b> {selected_country["概要"]} <br>
            </div>
        </div>
    '''
    st.markdown(bubble_style, unsafe_allow_html=True)
    st.markdown(bubble_html, unsafe_allow_html=True)

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
    key(":blue[世界検索へようこそ！！]")
    key("ここでは様々な国を検索することができます")
    key("早速、左のメニューから選択して楽しみましょう！！")

elif option == '国の詳細検索':
    country_name = st.chat_input("国を検索してください")
    if country_name.strip() != "国を検索してください":
            selected_country = countries_df[countries_df["国名"] == country_name]
            selected_country = {
    "国名": "日本",
    "首都": "東京",
    "GDP": "5兆ドル",
    "概要": "日本はアジアの島国で、先進的な経済と文化があります。"
}

    if selected_country:  # selected_countryが空でない場合のみ吹き出しを表示
            key(selected_country)
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

