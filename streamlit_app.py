import streamlit as st
import pandas as pd
import plotly.express as px
import random

# データを初期読み込みする
# 変数としてデータフレームを宣言する
df34 = None
options34 = []  # 選択肢を保持するリスト

@st.cache_data
def load_data(file_path):
    """Excelファイルからデータを読み込む"""
    return pd.read_excel(file_path)

# データフレームを読み込む（全て）
# 国の地図
countries_df = load_data("28.xlsx")
# 政治体制
countries_df2 = load_data("25.xlsx")
# GDP比較の表
df3 = load_data("27.xlsx")
# 辞典
df4 = load_data("2sw.xlsx")

# 初期の7大国のGDPデータを定義する
gdp_data = {
    'Country': ['アメリカ合衆国', '中国', '日本', 'ドイツ', 'イギリス', 'フランス', 'インド'],
    'GDP': [21.43, 14.34, 5.08, 3.84, 2.83, 2.71, 2.87]
}

# sidebarにボタンを配置する
tab = st.sidebar.radio("選択してください", ['ホーム', '国検索', '国のGDP検索', '政治体制検索', '緯度クイズ', '用語辞典'])

if tab == 'ホーム':
    st.title("世界検索")
    st.write(":blue[世界検索へようこそ！！]")
    st.write("ここでは様々な国の情報を検索し、知ることができます")
    st.write("国検索から政治体制の検索まで様々な検索を行うことができます")
    st.write("早速、左のタブから選択して楽しみましょう！！")

elif tab == '国検索':
    st.title("国検索")
    st.write("国名を入力してください（適用していない国もあります）")
    a = st.text_input("国名を入力")

    # 国を入力する欄を表示する   
    if a.strip() != "":
        selected_country = countries_df[countries_df["国名"] == a]
        if not selected_country.empty:
            selected_country = selected_country.iloc[0]
            st.write("国名:", selected_country["国名"])
            st.write("首都:", selected_country["首都"])
            st.write("英語表記:", selected_country["英語"])
            st.write("概要:", selected_country["概要"])

            # 地図表示
            st.subheader('国の地図')
            st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=2)

            # 選択された国のGDPデータをgdp_dataに追加する
            if selected_country["国名"] not in gdp_data['Country']:
                gdp_data['Country'].append(selected_country["国名"])
                gdp_data['GDP'].append(selected_country["GDP"])

            # 保存
            st.session_state['gdp_data'] = gdp_data
        else:
            st.write("検索結果なし")

elif tab == '国のGDP検索':
    st.title("GDP比較")
    st.write('データソース: IMF')
    st.write("単位は兆ドルとなっています")

    # データ（df3）から国のリストを取得
    countries_list = df3['国名2'].tolist()

    # 選択した国の入力する欄を表示する
    selected_country = st.text_input('比較したい国を入力してください（例: USA, China, Japanなど）', key='sel_country')

    selected_data = df3[df3['国名2'] == selected_country]

    # 大国のデータ（例としてアメリカ合衆国、中国、日本を指定）
    major_countries = ['アメリカ合衆国', '中国', '日本']

    # 新しく追加する国の入力する欄を表示する
    new_country = st.text_input('新しく追加する国名を入力してください（例: ドイツ）', key='new_country')
    st.write(":red[二つの国を必ず入力してください。]")

    # 新しく追加した国のGDPを取得する
    if new_country and selected_country:
        # 新旧の国を比較するグラフを描画する
        comparison_data = df3[df3['国名2'].isin([selected_country, new_country] + major_countries)]
        fig_comparison = px.bar(comparison_data, x='国名2', y='GDP3', color='国名2',
        labels={'GDP3': 'GDP (兆ドル)', '国名2': '国'})
        st.plotly_chart(fig_comparison)
    else:
        st.write("両方の国名を入力してください。")

elif tab == '政治体制検索':
    st.title("政治体制検索")
    # 政治体制を選択する選択バーを表示する
    st.write("政治体制を選択してください")
    political_system = st.selectbox("体制を選択", ["",
       "共和制", "多党制民主主義", "立憲君主制", "半大統領制", "議院内閣制", "絶対君主制", "準連邦制",
       "単一政党制", "軍事政権", "混合制", "大統領制"
    ], key='poli_sys')
    
    if political_system.strip() != "":
        selected_countries = countries_df2[countries_df2["体制"] == political_system.strip()]

        if not selected_countries.empty:
            st.subheader(f"{political_system} の国々")
            # 選択された政治体制に属する国の表を表示する
            st.write(selected_countries["国国"])

            # 地図を表示する
            st.subheader(f'{political_system