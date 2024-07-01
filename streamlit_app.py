import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Matplotlibのバックエンドを設定

import matplotlib.pyplot as plt

# 七大国のGDPデータ（2023年の予測値）
gdp_data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'UK', 'France', 'Italy'],
    'GDP (trillion USD)': [23.49, 18.47, 5.37, 4.90, 3.23, 3.08, 2.48]
}

# DataFrameを作成
df = pd.DataFrame(gdp_data)

# Streamlitアプリケーションの設定
st.title('七大国のGDP')

# テーブルを表示
st.write(df)

# グラフを表示
fig, ax = plt.subplots()
ax.bar(df['Country'], df['GDP (trillion USD)'], color='skyblue')
ax.set_xlabel('Country')
ax.set_ylabel('GDP (trillion USD)')
ax.set_title('七大国のGDP')

# グラフをStreamlitで表示
st.pyplot(fig)
