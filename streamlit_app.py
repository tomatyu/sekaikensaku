import streamlit as st
import pandas as pd
import numpy as np

st.title("$お試しだよ！$")
a = st.text_input("検索(現在は国連常任理事国＋日本しか対応していません)",)

st.write("_検索結果_") 
if any([f"{a}" == "アメリカ合衆国" for v in a]):
    # 国名と首都の表示
   st.write("国名: アメリカ合衆国")
   st.write("首都: ワシントンDC")

    # データフレームの作成
   usa_df = pd.DataFrame({
    'lat': [38.8977],  # ワシントンDCの緯度
    'lon': [-77.0365]  # ワシントンDCの経度
   })
   # 地図へのピンの表示
   st.map(usa_df,zoom = 1)
elif any([f"{a}" == "中国" for v in a]):
     # 国名と首都の表示
   st.write("国名: 中華人民共和国")
   st.write("首都: 北京")

    # データフレームの作成
   cha_df = pd.DataFrame({
    'lat': [39.9042],  # 北京の緯度
    'lon': [116.4074]  # 北京の経度
   })
 
     
    # 地図へのピンの表示
   st.map(cha_df,zoom = 1)
elif any([f"{a}" == "日本" for v in a]):
     # 国名と首都の表示
   st.write("国名: 日本国")
   st.write("首都: 東京")

    # データフレームの作成
   jap_df = pd.DataFrame({
    'lat': [38.8977],  # 東京の緯度
    'lon': [-77.0365]  # 東京の経度
   })
 
     
    # 地図へのピンの表示
   st.map(jap_df)
else:
    st.write("検索結果なし")


