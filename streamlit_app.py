import streamlit as st
from datetime import datetime

def main():
    st.title("現在時刻を表示するアプリ")

    # 現在時刻の取得
    now = datetime.now()
    current_time = now.strftime("%Y/%m/%d %H:%M:%S")

    st.write("現在の時刻は:", current_time)

if __name__ == "__main__":
    main()
