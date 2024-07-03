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
for country in gdp_data['国名']:
    if country in exchange_rate:
        idx = gdp_data['国名'].index(country)
        gdp_data['GDP'][idx] *= exchange_rate[country] * 10**12

# GDPデータをDataFrameに変換
df = pd.DataFrame(gdp_data)

# Streamlitアプリケーションの作成
st.title('7大国のGDPを円グラフで表示するアプリ')

# データフレームの表示（オプション）
if st.checkbox('生データを表示'):
    st.write(df)

# グラフの作成
st.subheader('7大国のGDPの比較（円グラフ）')

# ラベルとサイズを指定して円グラフをプロット
fig, ax = plt.subplots()
ax.pie(df['GDP'], labels=df['国名'], autopct='%1.1f%%', startangle=90, counterclock=False)

# グラフを中央に配置してアスペクト比を維持
ax.axis('equal')

# グラフをStreamlitに表示
st.pyplot(fig)
