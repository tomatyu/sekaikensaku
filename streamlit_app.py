import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# GeoPandasの世界地図データを読み込む
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Streamlitアプリケーションの設定
st.title('国を選択して地図を表示')

# 国の選択肢を作成
selected_country = st.selectbox('国を選択してください', world['name'])

# 選択された国の地図データを取得
country_data = world[world['name'] == selected_country]

# Plotlyの地図を準備
fig = go.Figure()

# 選択された国の境界線を赤で表示するための処理
for feature in country_data['geometry']:
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
    title=f'国境強調地図: {selected_country}',
    margin=dict(l=0, r=0, t=30, b=0),  # レイアウトのマージン
    height=600  # 地図の高さ
)

# 地図をStreamlitアプリに表示
st.plotly_chart(fig)
