import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 日本語フォントの設定
plt.rcParams['font.family'] = 'IPAexGothic'

# 為替レート（2024年7月時点の目安）
exchange_rate = {
    'アメリカ': 110,   # 1ドル = 110円
    '中国': 16,        # 1元 = 16円
    '日本': 1,         # 1円 = 1円（基準）
    'ドイツ': 130,     # 1ユーロ = 130円
    'イギリス': 150,   # 1ポンド = 150円
    'インド': 1.5,     # 1ルピー = 1.5円
    'フランス': 120    # 1ユーロ = 120円
}

# 7大国のGDPデータを定義（兆円単位で設定）
gdp_data = {
    '国名': ['アメリカ', '中国', '日本', 'ドイツ', 'イギリス', 'インド', 'フランス'],
    'GDP': [23.5, 14.3, 5.1, 4.2, 2.9, 2.8, 2.7]
}

# GDPを日本円に換算
gdp_in_yen = [g * exchange_rate.get(country, 1) * 10**12 for country, g in zip(gdp_data['国名'], gdp_data['GDP'])]

# 新しいDataFrameに変換
df = pd.DataFrame({'国名': gdp_data['国名'], 'GDP(日本円)': gdp_in_yen})

# Streamlitアプリケーションの作成
st.title('7大国のGDPを棒グラフで表示するアプリ')

# データフレームの表示（オプション）
if st.checkbox('生データを表示'):
    st.write(df)

# グラフの作成
st.subheader('7大国のGDPの比較（棒グラフ）')

# プロット
fig, ax = plt.subplots()
ax.bar(df['国名'], df['GDP(日本円)'], color='blue')

# 軸ラベルとタイトルの設定（日本語）
ax.set_xlabel('国名')
ax.set_ylabel('GDP（日本円）')
ax.set_title('主要国のGDP')

# x軸ラベルの回転
plt.xticks(rotation=45)

# グラフを表示
st.pyplot(fig)
