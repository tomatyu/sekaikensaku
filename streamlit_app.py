import streamlit as st
from datetime import datetime
import pytz
import time

def main():
    st.title("現在時刻を表示するアプリ")
    st.wrie("じこーーーーーーーーーく")

    # 日本時間のタイムゾーンを設定
    japan_tz = pytz.timezone('Asia/Tokyo')

    while True:
        # 現在時刻を日本時間で取得
        now = datetime.now(japan_tz)
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")

        # 時刻を表示
        st.write("現在の日本時間は:", current_time)

        # 1秒ごとに更新
        time.sleep(1)

if __name__ == "__main__":
    main()
