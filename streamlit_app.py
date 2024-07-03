import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# GDPデータの読み込み
@st.cache  # データをキャッシュし、再読み込みを高速化する
def load_data():
    # CSVファイルの読み込み（ファイルオブジェクトを使用する例）
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        st.warning('Upload CSV file')

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
