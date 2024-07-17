import streamlit as st
import time
from datetime import datetime

def main():
    st.title("リアルタイム時刻表示アプリ")

    # 初期の時刻表示用の空のコンポーネントを作成
    time_placeholder = st.empty()

    while True:
        # 現在時刻を取得
        now = datetime.now()
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")

        # 時刻を更新
        time_placeholder.text(f"現在の時刻は: {current_time}")

        # 1秒待つ
        time.sleep(1)

if __name__ == "__main__":
    main()
