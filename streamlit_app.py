import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 7大国のGDPデータを定義
gdp_data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'UK', 'India', 'France'],
    'GDP': [23.5, 14.3, 5.1, 4.2, 2.9, 2.8, 2.7]
}

# GDPデータをDataFrameに変換
df = pd.DataFrame(gdp_data)

# Streamlitアプリケーションの作成
st.title('7大国のGDPをバーチャートで表示するアプリ')

# データフレームの表示（オプション）
if st.checkbox('Show raw data'):
    st.write(df)

# グラフの作成
st.subheader('7大国のGDPの比較')

# グラフをプロット
fig, ax = plt.subplots()
ax.bar(df['Country'], df['GDP'], color='blue')  # バープロットを使用する例（青色で表示）

# グラフの軸ラベルとタイトルの設定
ax.set_xlabel('Country')
ax.set_ylabel('GDP (in trillion $)')
ax.set_title('GDP of Major Countries')

# x軸ラベルの回転
plt.xticks(rotation=45)

# グラフをStreamlitに表示
st.pyplot(fig)
