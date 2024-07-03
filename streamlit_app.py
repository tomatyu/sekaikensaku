import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 7大国のGDPデータ（兆ドル）
gdp_data = {
    '国名': ['アメリカ', '中国', '日本', 'ドイツ', 'イギリス', 'インド', 'フランス'],
    'GDP（兆ドル）': [23.5, 14.3, 5.1, 4.2, 2.9, 2.8, 2.7]
}

# GDPデータをDataFrameに変換
df = pd.DataFrame(gdp_data)

# Streamlitアプリケーションの作成
st.title('7大国のGDPを比較するアプリ')

# 日本語翻訳ボタン
if st.button('全体を日本語に翻訳'):
    st.markdown('### 7大国のGDPの比較（棒グラフ）')
    st.write('以下は7大国のGDPを兆ドルで比較したグラフです。')
    st.write(df)

# グラフの作成
st.subheader('7 Major Countries GDP Comparison (Bar Chart)')

# グラフをプロット
fig, ax = plt.subplots()
ax.bar(df['国名'], df['GDP（兆ドル）'], color='blue')

# 軸ラベルとタイトルの設定
ax.set_xlabel('Country')
ax.set_ylabel('GDP (trillion $)')
ax.set_title('GDP of Major Countries')

# x軸ラベルの回転
plt.xticks(rotation=45)

# グラフを表示
st.pyplot(fig)
