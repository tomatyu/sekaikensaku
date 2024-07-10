import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データを読み込む
countries_df = pd.read_excel("21.xlsx")
countries_df2 = pd.read_excel("25.xlsx")

# Streamlitアプリケーションのセットアップ
st.title("世界検索")
st.write("好きな国を検索して、:red[知識] を見つけましょう！")

# gdp_dataの初期化
gdp_data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India'],  # 大国のデータを最初から入れておく
    'GDP': [21.43, 14.34, 5.08, 3.86, 2.87]  # トリリオンドル単位でのGDPデータ
}

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
            selected_country = countries_df[countries_df["国名"] == a.strip()]
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
                else:
                    idx = gdp_data['Country'].index(selected_country["国名"])
                    gdp_data['GDP'][idx] = selected_country["GDP"]

                # session_stateに保存
                st.session_state['gdp_data'] = gdp_data
            else:
                st.write("検索結果なし")

elif tab == '国のGDP検索':
    st.subheader('国のGDP検索')
    st.write("国名を入力してください（適用していない国もあります）")
    a = st.text_input("")
    if st.button('国のGDPを表示'):
        if 'gdp_data' in st.session_state:
            gdp_data = st.session_state['gdp_data']

            df = pd.DataFrame(gdp_data)

            # バーチャートのプロット
            st.subheader('大国のGDPの比較')

            # 図と軸の作成
            fig = plt.figure()
            ax = fig.add_subplot()

            # バーチャートのプロット
            bars = ax.bar(df['Country'], df['GDP'])

            # 選択した国を強調表示（太字）
            if a.strip() in df['Country'].values:
                idx = df['Country'].tolist().index(a.strip())
                bars[idx].set_linewidth(2.5)  # 太さを調整する例

                # 選択した国のGDPをグラフに追加
                selected_gdp = countries_df[countries_df["国名"] == a.strip()]["GDP"].iloc[0]
                ax.bar(a.strip(), selected_gdp, color='red', label=f'{a.strip()} GDP')

                # グラフのタイトルを更新
                ax.set_title('GDP of Major Countries including ' + a.strip())

            # 軸ラベルとタイトルの設定
            ax.set_xlabel('Country')
            ax.set_ylabel('GDP (trillion dollars)')
            
            # 凡例の表示
            ax.legend()

            # x軸ラベルの回転
            plt.xticks(rotation=45)

            # グラフをStreamlitに表示
            st.pyplot(fig)
            st.write(f"選択した国 {a} のGDPをグラフに追加しました。")

        else:
            st.write("国を検索してから、国のGDPデータを追加してください。")

elif tab == '政治体制検索':
    st.write("政治体制を選択してください")
    b = st.selectbox("", [
       "共和制", "多党制民主主義", "立憲君主制", "半大統領制", "議院内閣制", "絶対君主制", "準連邦制",
       "単一政党制", "軍事政権", "混合制","大統領制"
    ])
    if st.button('国を表示'):
        if b.strip() != "":
            selected_countries = countries_df2[countries_df2["体制"] == b.strip()]

            if not selected_countries.empty:
                st.subheader(f"{b} の国々")

                # 選択された政治体制に属する国の表を表示
                st.write(selected_countries[["国国", "緯度2", "経度2"]])

                # 地図表示
                st.subheader(f'{b} の地図')
                locations = pd.DataFrame({'lat': selected_countries["緯度2"], 'lon': selected_countries["経度2"]})
                st.map(locations, zoom=0.5)
            else:
                st.write("検索結果なし")
