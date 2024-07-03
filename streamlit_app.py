import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 7大国のGDPデータを定義
gdp_data = {
    'Country': ['アメリカ', '中国', '日本', 'ドイツ', 'イギリス', 'インド', 'フランス'],
     'GDP': [23500, 14300, 5100, 4200, 2900, 2800, 2700]  # 兆円（1兆ドル ≈ 100兆円）
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
ax.set_xlabel('国名')
ax.set_ylabel('GDP (兆ドル)')
ax.set_title('国名')

# x軸ラベルの回転
plt.xticks(rotation=45)

# グラフをStreamlitに表示
st.pyplot(fig)
