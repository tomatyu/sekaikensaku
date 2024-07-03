import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# GDPデータの読み込み
@st.cache  # データをキャッシュし、再読み込みを高速化する
def load_data():
    # CSVファイルの読み込み
    df = pd.read_excel('17.xlsx')
    return df

# メインのStreamlitアプリケーション
def main():
    st.title('7大国のGDPをバーチャートで表示するアプリ')

    # GDPデータを読み込む
    df = load_data()

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

if __name__ == '__main__':
    main()
