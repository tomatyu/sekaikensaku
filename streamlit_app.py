import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data4():
    return pd.read_excel("30.xlsx")

# Excelファイルからデータを読み込む
data = load_data4()

# Streamlitアプリケーションの作成
st.title('Population Trends')

# データフレームの先頭部分を表示（確認用）
st.write(data.head())

# グラフの描画
country = st.selectbox('国名を選択してください', data['国名'].unique())
filtered_data = data[data['国名'] == country]

if not filtered_data.empty:
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data.index, filtered_data['人口'], marker='o')  # indexを使って時系列の順序でプロット
    plt.xlabel('データポイント')
    plt.ylabel('人口')
    plt.title(f'{country} の人口推移')
    st.pyplot(plt)
else:
    st.write(f'{country} に関するデータはありません。')
