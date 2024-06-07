import streamlit as st
import folium

def main():
    st.title("地図上に線を引く")

    # 地図の初期位置を指定
    map_center = [35.681236, 139.767125]  # 東京駅の座標

    # 地図を描画
    my_map = folium.Map(location=map_center, zoom_start=15)

    # 線の始点と終点を指定
    start_point = (35.681236, 139.767125)  # 東京駅の座標
    end_point = (35.682227, 139.767052)     # 東京国際フォーラムの座標

    # 線を描画
    folium.PolyLine(locations=[start_point, end_point], color='red').add_to(my_map)

    # Streamlitに地図を表示
    folium_static(my_map)

if __name__ == "__main__":
    main()
