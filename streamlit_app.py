import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.graph_objects as go

# データを初期読み込みする
@st.cache
def load_data():
    return pd.read_excel("18.xlsx")

# GeoPandasの世界地図データを読み込む
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

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

# 横に並べて表示するための列を作成
col1, col2 = st.columns(2)

# 国検索ボタン
with col1:
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
                fig = go.Figure()

                # 選択された国の境界線を赤で表示するための処理
                for feature in world[world['name'] == selected_country["国名"]]['geometry']:
                    if feature.geom_type == 'Polygon':
                        x, y = feature.exterior.xy
                        fig.add_trace(go.Scattergeo(
                            lon=x,
                            lat=y,
                            mode='lines',
                            line=dict(width=2, color='red'),
                            hoverinfo='skip'
                        ))
                    elif feature.geom_type == 'MultiPolygon':
                        for polygon in feature:
                            x, y = polygon.exterior.xy
                            fig.add_trace(go.Scattergeo(
                                lon=x,
                                lat=y,
                                mode='lines',
                                line=dict(width=2, color='red'),
                                hoverinfo='skip'
                            ))

                # 全体の地図の設定
                fig.update_geos(
                    showcountries=True,  # 国境線を表示
                    showcoastlines=True,  # 海岸線を表示
                    showland=True,  # 陸地を表示
                    showocean=True,  # 海洋を表示
                    coastlinecolor='black',  # 海岸線の色
                    oceancolor='#e0f7fa',  # 海洋の色
                    projection_type='natural earth',  # 地図の投影方法
                )

                fig.update_layout(
                    title=f'国境強調地図: {selected_country["国名"]}',
                    margin=dict(l=0, r=0, t=30, b=0),  # レイアウトのマージン
                    height=600  # 地図の高さ
                )

                # 地図をStreamlitアプリに表示
                st.plotly_chart(fig)

                # 選択された国のGDPデータをgdp_dataに追加する
                if selected_country["国名"] not in gdp_data['Country']:
                    gdp_data['Country'].append(selected_country["国名"])
                    gdp_data['GDP'].append(selected_country["GDP"])

                # session_stateに保存
                st.session_state['gdp_data'] = gdp_data
            else:
                st.write("検索結果なし")

# 国のGDP検索ボタン
with col2:
    if st.button('国のGDP検索'):
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
