import streamlit as st
import pandas as pd
import plotly.express as px
import random

# データを初期読み込みする
# 変数としてデータフレームを宣言する
df34 = None
options34 = []  # 選択肢を保持するリスト

@st.cache
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
#　辞典
df4 = load_data("2sw.xlsx")

# 初期の7大国のGDPデータを定義する
gdp_data = {
    'Country': ['アメリカ合衆国', '中国', '日本', 'ドイツ', 'イギリス', 'フランス', 'インド'],
    'GDP': [21.43, 14.34, 5.08, 3.84, 2.83, 2.71, 2.87]
}

# sidebarにボタンを配置する
tab = st.sidebar.radio("選択してください", ['ホーム', '国検索', '国のGDP検索', '政治体制検索', '緯度クイズ','用語辞典'])

if tab == 'ホーム':
    st.title("世界検索")
    st.write(":blue[世界検索へようこそ！！]")
    st.write("ここでは様々な国を検索することができます")
    st.write("早速、左のタブから選択して楽しみましょう！！")

elif tab == '国検索':
    st.title("国検索")
    st.write("国名を入力してください（適用していない国もあります）")
    a = st.text_input("")

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
    selected_country = st.text_input('比較したい国を入力してください（例: USA, China, Japanなど）')

    selected_data = df3[df3['国名2'] == selected_country]

    # 大国のデータ（例としてアメリカ合衆国、中国、日本を指定）
    major_countries = ['アメリカ合衆国', '中国', '日本']

    # 新しく追加する国の入力する欄を表示する
    new_country = st.text_input('新しく追加する国名を入力してください（例: ドイツ）')
    st.write(":red[二つの国を必ず入力してください。]")

    # 新しく追加した国のGDPを取得する
    if new_country and selected_country:
        # 新旧の国を比較するグラフを描画する
        comparison_data = df3[df3['国名2'].isin([selected_country, new_country] + major_countries)]
        fig_comparison = px.bar(comparison_data, x='国名2', y='GDP3', color='国名2',
        labels={'GDP3': 'GDP (兆ドル)', '国名2': '国'})
        st.plotly_chart(fig_comparison)
    else:
        st.write(f"{new_country} のデータが見つかりません。")

elif tab == '政治体制検索':
    st.title("政治体制検索")
#　政治体制を選択する選択バーを表示する
    st.write("政治体制を選択してください")
    political_system = st.selectbox("", ["",
       "共和制", "多党制民主主義", "立憲君主制", "半大統領制", "議院内閣制", "絶対君主制", "準連邦制",
       "単一政党制", "軍事政権", "混合制", "大統領制"
    ])
    
    if political_system.strip() != "":
            selected_countries = countries_df2[countries_df2["体制"] == political_system.strip()]

            if not selected_countries.empty:
                st.subheader(f"{political_system} の国々")
                # 選択された政治体制に属する国の表を表示する
                st.write(selected_countries["国国"])

                # 地図を表示する
                st.subheader(f'{political_system} の地図')
                locations = pd.DataFrame({'lat': selected_countries["緯度2"], 'lon': selected_countries["経度2"]})
                st.map(locations, zoom=0.5)
            else:
                st.write("検索結果なし")

elif tab == '緯度クイズ':
    st.title("緯度クイズ")
    def update_question():
        """問題を更新する"""
        global df34

        if df34 is None:
            df34 = load_data("28.xlsx")

        # 確認する
        if '国名' not in df34.columns or '緯度' not in df34.columns:
            st.write("データが正しく読み込まれていません。")
            return

        # データ（df34）から選択肢を設定
        unique_countries = df34['国名'].unique()
        
        # ランダムに4つの国を選ぶ
        selected_countries = random.sample(list(unique_countries), 4)
        
        # 4つの国の緯度情報を取得し、最も緯度が低い国を正解とする
        selected_df = df34[df34['国名'].isin(selected_countries)]
        min_latitude_country = selected_df.loc[selected_df['緯度'].idxmin(), '国名']

        # 選択肢をシャッフルして表示する
        options34 = selected_countries
        random.shuffle(options34)

        # 更新
        st.session_state.min_latitude_country = min_latitude_country
        st.session_state.options = options34
        st.session_state.message = "新しい問題が表示されています。"
        st.session_state.correct = None  # リセットする
        st.session_state.answer_submitted = False  # 回答状態のリセット

    def check_answer(answer):
        """ユーザーの回答をチェックする"""
        if st.session_state.answer_submitted:
            st.session_state.message = "すでに回答済みです。問題を更新してください。"
            return

        if answer == st.session_state.min_latitude_country:
            st.session_state.message = f"正解！正解は「{st.session_state.min_latitude_country}」です。"
            st.session_state.points += 10  # 正解で10ポイント追加
            st.session_state.correct = True
        else:
            st.session_state.message = f"不正解…「{answer}」は正しくありません。正解は「{st.session_state.min_latitude_country}」です。"
            st.session_state.points -= 10  # 不正解で10ポイント減算
            st.session_state.correct = False

        st.session_state.answer_submitted = True  # 回答済みフラグを設定

    def reset_points():
        """ポイントをリセットする"""
        st.session_state.points = 0
        st.session_state.message = "ポイントがリセットされました！"
        st.session_state.reset_done = True  # リセットが行われたフラグを設定

    def main2():
        """クイズのメイン関数"""
        global df34

        if df34 is None:
            df34 = load_data("28.xlsx")

       
        st.write("わからなかった国は上の検索で知ることができます！")

        # セッション状態の初期化
        if 'message' not in st.session_state:
            st.session_state.message = ''
        if 'correct' not in st.session_state:
            st.session_state.correct = None
        if 'min_latitude_country' not in st.session_state:
            st.session_state.min_latitude_country = None
        if 'options' not in st.session_state:
            st.session_state.options = []
        if 'points' not in st.session_state:
            st.session_state.points = 0  # 初期ポイントは0
        if 'answer_submitted' not in st.session_state:
            st.session_state.answer_submitted = False  # 回答状態の初期化
        if 'reset_done' not in st.session_state:
            st.session_state.reset_done = False  # リセット状態の初期化

        # サイドバーに現在のポイントとリセットボタンを表示
        st.sidebar.subheader('現在のポイント')
        st.sidebar.write(st.session_state.points)

        if st.sidebar.button('ポイントをリセット'):
            reset_points()

        # 問題更新のボタンを表示する
        if st.button("問題を更新"):
            update_question()

        if not st.session_state.options:
            update_question()

        # 問題文の表示を行う
        st.subheader('以下の国の中から、どれが最も緯度が低い国でしょう？')

        # ボタンを使って選択肢を表示する
        cols = st.columns(2)
        for i, option in enumerate(st.session_state.options):
            with cols[i % 2]:
                button_disabled = st.session_state.answer_submitted
                if st.button(option, disabled=button_disabled, key=f"option_{option}"):
                    check_answer(option)

        # メッセージを表示する
        if st.session_state.message:
            st.write(st.session_state.message)

    if tab == '緯度クイズ':
        main2()
elif tab == '用語辞典':
    st.title("用語辞典")
    st.subheader("このアプリでの用語を確認できます")

    # 選択肢を表示する
    political = st.selectbox("", [
       "共和制", "多党制民主主義", "立憲君主制", "半大統領制", "議院内閣制", "絶対君主制", "準連邦制",
       "単一政党制", "軍事政権", "混合制", "大統領制", "IMF", "兆ドル"
    ])
    
    # ボタンが押されたときの処理を行う
    
    if political.strip() != "":
            # データのフィルタリングを行う
            selected_countries2 = df4[df4["辞典"] == political.strip()]
            
            # 結果が空でない場合に処理を行う
            if not selected_countries2.empty:
                # 選択された政治体制に関する説明を表示する
                st.write(selected_countries2["意味１"].values[0])
            else:
                st.write("該当するデータが見つかりませんでした。")