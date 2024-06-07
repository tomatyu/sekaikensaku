import streamlit as st
import plotly.graph_objects as go

def main():
    st.title("地図上に線を引く")

    # 線の始点と終点を指定
    start_lat, start_lon = 35.681236, 139.767125  # 東京駅の座標
    end_lat, end_lon = 35.682227, 139.767052       # 東京国際フォーラムの座標

    # 地図上に線を描画するためのデータ
    trace = go.Scattermapbox(
        mode="lines",
        lon=[start_lon, end_lon],
        lat=[start_lat, end_lat],
        marker=dict(size=10),
        line=dict(width=2, color='red')
    )

    # 地図のレイアウト設定
    layout = go.Layout(
        mapbox_style="carto-positron",
        mapbox_zoom=15,
        mapbox_center={"lat": start_lat, "lon": start_lon}
    )

    fig = go.Figure(data=[trace], layout=layout)

    # Plotlyの地図を表示
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
