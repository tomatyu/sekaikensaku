import streamlit as st
from datetime import datetime, timedelta
import pytz
import time

def main():
    st.title("3時間前の時刻を表示するアプリ")

    # 日本時間のタイムゾーンを設定
    japan_tz = pytz.timezone('Asia/Tokyo')

    while True:
        # 現在時刻を日本時間で取得
        now = datetime.now(japan_tz)

        # 3時間前の時刻を計算
        time_3hours_ago = now - timedelta(hours=3)
        
        # 時刻をフォーマットして表示
        current_time = time_3hours_ago.strftime("%Y/%m/%d %H:%M:%S")
        st.write("3時間前の日本時間は:", current_time)

        # 1秒ごとに更新
        time.sleep(1)

if __name__ == "__main__":
    main()
