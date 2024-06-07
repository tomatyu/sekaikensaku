import streamlit as st
import pandas as pd


# フランスの座標
a = {"lat": 46.603354, "lon": 1.888334}

# ヴァルミーの座標
b = {"lat": 49.0136, "lon": 4.9544}

# 座標追加
df = pd.DataFrame([a,b]) 

# 線の始点と終点を指定
start_point = (35.681236, 139.767125)  # 東京駅の座標
end_point = (35.682227, 139.767052)     # 東京国際フォーラムの座標

# 線を描画
st.line(locations=[start_point, end_point], color='red').add_to(df)


