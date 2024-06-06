import streamlit as st
import pandas as pd

# 世界遺産の位置情報
world_heritage_data = pd.DataFrame({
    '名前': ['キリマンジャロ', 'エーゲ海の島々', 'クスコ歴史地区', 'タージ・マハル', 'グランドキャニオン国立公園', 'メキシコシティ歴史地区', 'クスコ歴史地区', 'モンテ・サン・ミシェル', 'シルクロード', 'イエローストーン国立公園'],
    'lat': [-3.0674, 37.3635, -13.5183, 27.1751, 36.1069, 19.4326, -13.1631, 48.6361, 38.8610, 44.4279],
    '経度': [37.3556, 25.2757, -71.9789, 78.0421, -112.1129, -99.1332, -72.5450, -1.5107, 66.1667, -110.5885]
})

def main():
    st.title("世界遺産地図")

    # 経度の列名を 'longitude' に変更
    world_heritage_data.rename(columns={'経度': 'lon'}, inplace=True)

    # 地図上に世界遺産のピンを表示
    st.map(world_heritage_data)

if __name__ == "__main__":
    main()