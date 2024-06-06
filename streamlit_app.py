import streamlit as st
import pandas as pd

# フランスの座標
france_coords = {'lat': 46.603354, 'lon': 1.888334}

# ヴァルミーの座標
valmy_coords = {'lat': 49.0136, 'lon': 4.9544}

# データフレームにフランスとヴァルミーの座標を追加
df = pd.DataFrame([france_coords, valmy_coords])

# 地図上にピンを表示
st.map(df)
