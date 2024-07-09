import streamlit as st
import pandas as pd

# データを初期読み込みする
@st.cache
def load_data():
    return pd.read_excel("21.xlsx")

@st.cache
def load_data2():
    return pd.read_excel("24.xlsx")

# Streamlitアプリケーションのセットアップ
st.title("世界検索")
st.write("好きな国を検索して、:red[知識] を見つけましょう！")

# データフレームを読み込む
countries_df = load_data()
countries_df2 = load_data2()

# sidebarにボタンを配置
tab = st.sidebar.radio("選択してください", ['ホーム', '国検索', '国のGDP検索', '政治体制検索'])

if tab == 'ホーム':
    st.subheader("世界検索へようこそ！！")
    st.write("ここでは様々な国を検索することができます")

elif tab == '国検索':
    st.write("国名を入力してください（適用していない国もあります）")
    a = st.text_input("")
    if st.button('国を表示'):
        if a.strip() != "":
            selected_country = countries_df[countries_df["国名"] == a]
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

                # session_stateに保存
                st.session_state['gdp_data'] = gdp_data
            else:
                st.write("検索結果なし")

elif tab == '国のGDP検索':
    st.write("国名を入力してください（適用していない国もあります）")
    a = st.text_input("")
    if st.button('国のGDPを表示'):
        if 'gdp_data' in st.session_state:
            gdp_data = st.session_state['gdp_data']

            df = pd.DataFrame(gdp_data)

            # バーチャートのプロット
            st.subheader('7大国のGDPの比較')

            # 図と軸の作成
            fig, ax = plt.subplots()

            # バーチャートのプロット
            bars = ax.bar(df['Country'], df['GDP'])

            # 選択した国を強調表示（太字）
            if a in df['Country'].values:
                idx = df['Country'].tolist().index(a)
                bars[idx].set_linewidth(2.5)  # 太さを調整する例

            # 軸ラベルとタイトルの設定
            ax.set_xlabel('Country')
            ax.set_ylabel('GDP (trillion dollars)')
            ax.set_title('GDP of Major Countries')

            # x軸ラベルの回転
            plt.xticks(rotation=45)

            # グラフをStreamlitに表示
            st.pyplot(fig)
            st.write(f"選択した国 {a} を一番右に表示しています。")
        else:
            st.write("国を検索してから、国のGDPデータを追加してください。")

elif tab == '政治体制検索':
    st.write("政治体制を選択してください")
    b = st.selectbox("政治体制を選択してください", [
        "共和制", "立憲君主制", "半大統領制", "連邦立憲君主制", "大統領制",
        "単一党制共和制", "半大統領制", "絶対君主制", "一党制社会主義共和国", "議院内閣制",
        "軍事政権", "多民族国家共和国", "連邦制共和国", "連邦共和制", "軍事政権",
        "イスラム共和国", "一党制社会主義共和国", "君主制連邦国家"
    ])
    if st.button('国を表示'):
        if b.strip() != "":
            selected_countries = countries_df2[countries_df2["体制"] == b]

            if not selected_countries.empty:
                st.subheader(f"{b} の国々")

                # 地図表示
                st.subheader(f'{b} の地図')
                locations = pd.DataFrame({'lat': selected_countries["緯度2"], 'lon': selected_countries["経度2"]})
                st.map(locations, zoom=2)
            else:
                st.write("検索結果なし")
