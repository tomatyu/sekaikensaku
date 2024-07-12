import streamlit as st
import pandas as pd
import pydeck as pdk

def load_data4():
    return pd.read_excel("30.xlsx")

# Excelファイルからデータを読み込む
data = load_data4()

# Streamlitアプリケーションの作成
st.title('Population Map')

# PyDeckを使用して地図を表示
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=50,
    ),
    layers=[
        # ScatterplotLayerで国の位置と人口を表示
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[経度, 緯度]',
            get_color='[200, 30, 0, 160]',
            get_radius='人口 / 1000000',  # 人口に応じてサイズを変更（例：百万人単位でサイズ調整）
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=10,
            radius_min_pixels=5,
            radius_max_pixels=30,
        ),
    ],
))
