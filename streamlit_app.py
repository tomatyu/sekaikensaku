import streamlit as st
import pandas as pd
import plotly.express as px

# Excelファイルからデータを読み込む関数
def load_data3():
    return pd.read_excel("26.xlsx")

# Streamlitアプリケーションの設定
st.title('主要国のGDP比較')
st.write('データソース: IMF')

# データを読み込む
df = load_data3()

# データフレームから国のリストを取得
countries = df['国名2'].tolist()

# 選択した国の入力
selected_country = st.text_input('比較したい国を入力してください（例: USA, China, Japanなど）')

# 選択した国のデータをフィルタリング
selected_data = df[df['国名2'] == selected_country]

# 大国のリスト（例として米国、中国、日本を指定）
major_countries = ['USA', 'China', 'Japan']

# 新しく追加する国の入力
new_country = st.text_input('新しく追加する国名を入力してください（例: Germany）')

# 新しく追加した国のGDPを取得
if new_country:
    new_data = df[df['国名2'] == new_country]
    if not new_data.empty:
        st.subheader(f'{new_country} のGDP情報')
        st.write(new_data)
        
        # 新旧の国を比較するグラフを描画
        comparison_data = df[df['国名2'].isin([selected_country, new_country] + major_countries)]
        fig_comparison = px.bar(comparison_data, x='国名2', y='GDP (trillion $)', color='国名2',
                                labels={'GDP (trillion $)': 'GDP (兆ドル)', '国名2': '国'})
        st.plotly_chart(fig_comparison)
    else:
        st.write(f"{new_country} のデータが見つかりません。")

# 選択した国のGDPを表示
if selected_country:
    if not selected_data.empty:
        st.subheader(f'{selected_country} のGDP情報')
        st.write(selected_data)
    else:
        st.write(f"{selected_country} のデータが見つかりません。")
else:
    st.write("国名を入力してください。")
