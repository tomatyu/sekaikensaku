import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 日本語フォントの設定
plt.rcParams['font.family'] = 'IPAexGothic'

# 7大国のGDPデータを定義
gdp_data = {
    '国名': ['アメリカ', '中国', '日本', 'ドイツ', 'イギリス', 'インド', 'フランス'],
    'GDP': [23.5, 14.3, 5.1, 4.2, 2.9, 2.8, 2.7]
}

# GDPデータをDataFrameに変換
df = pd.DataFrame(gdp_data)

# Streamlitアプリケーションの作成
st.title('7大国のGDPをバーチャートで表示するアプリ')

# データフレームの表示（オプション）
if st.checkbox('生データを表示'):
    st.write(df)

# グラフの作成
st.subheader('7大国のGDPの比較')

# グラフをプロット
fig, ax = plt.subplots()
ax.bar(df['国名'], df['GDP'], color='blue')  # バープロットを使用する例（青色で表示）

# グラフの軸ラベルとタイトルの設定（日本語）
ax.set_xlabel('国名')
ax.set_ylabel('GDP（兆ドル）')
ax.set_title('主要国のGDP')

# x軸ラベルの回転
plt.xticks(rotation=45)

# グラフをStreamlitに表示
st.pyplot(fig)
