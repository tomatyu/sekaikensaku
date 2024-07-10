import streamlit as st
import pandas as pd
import plotly.express as px

# Excelファイルからデータを読み込む関数
def load_data3():
    return pd.read_excel("26.xlsx")

# Streamlitアプリケーションの設定
st.title('Major Countries GDP Visualization')
st.write('Data Source: IMF')

# データを読み込む
df = load_data3()

# データフレームから国のリストを取得
countries = df['国名2'].tolist()

# ユーザーが選択した国を取得
selected_country = st.selectbox('Select a country', countries)

# 選択した国のデータをフィルタリング
selected_data = df[df['国名2'] == selected_country]

# グラフの描画
fig = px.bar(selected_data, x='国名2', y='GDP (trillion $)', color='GDP3',
             labels={'GDP (trillion $)': 'GDP (trillion $)', 'Country': 'GDP3'})
st.plotly_chart(fig)
