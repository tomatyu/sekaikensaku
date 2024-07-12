import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# ダミーデータの生成 (本来はここに実際の人口データを読み込む)
# 例としてランダムな人口データを生成します
np.random.seed(0)
data_size = 1000
min_population = 1000
max_population = 100000
chart_data = pd.DataFrame({
    'lat': np.random.uniform(37.7, 37.8, size=data_size),
    'lon': np.random.uniform(-122.5, -122.3, size=data_size),
    'population': np.random.randint(min_population, max_population, size=data_size)
})

# Streamlitアプリケーションの作成
st.title('Population Density Map')

# PyDeckを使用して地図を表示
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        # HexagonLayerで人口密度を表示
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=50,
           elevation_range=[0, 3000],
           pickable=True,
           extruded=True,
        ),
        # ScatterplotLayerでポイントを表示
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius='population / 1000',  # 人口に応じてサイズを変更
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
