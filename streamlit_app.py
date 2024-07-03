import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# GDPデータの読み込み
@st.cache  # データをキャッシュし、再読み込みを高速化する
def load_data():
    # CSVファイルの読み込み（適切なファイルパスを指定）
   # CSVファイルの読み込み（ファイルパスを適切に変更）
   # CSVファイルの読み込み（相対パスを使用する例）
    df = pd.read_csv('gdp_data.csv')  # streamlit_app.pyと同じディレクトリにファイルがある場合


    return df

# メインのStreamlitアプリケーション
def main():
    st.title('大国のGDPを表示するアプリ')

    # GDPデータを読み込む
    df = load_data()

    # データフレームの表示（オプション）
    if st.checkbox('Show raw data'):
        st.write(df)

    # グラフの作成
    st.subheader('GDPのグラフ')

    # グラフをプロット
    fig, ax = plt.subplots()
    ax.bar(df['Country'], df['GDP'])  # バープロットを使用する例

    # グラフをStreamlitに表示
    st.pyplot(fig)

if __name__ == '__main__':
    main()
