import streamlit as st
from datetime import datetime
import time

# JavaScriptを埋め込むためのHTMLテンプレート
def html_template():
    return """
    <head>
    <meta http-equiv="refresh" content="1">
    </head>
    """

def main():
    st.title("リアルタイム時刻表示アプリ")

    # JavaScriptを埋め込む
    st.markdown(html_template(), unsafe_allow_html=True)

    # 現在時刻を表示するループ
    while True:
        now = datetime.now()
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")
        st.write("現在の時刻は:", current_time)
        time.sleep(1)  # 1秒ごとに更新する

if __name__ == "__main__":
    main()
