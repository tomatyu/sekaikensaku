import streamlit as st

from streamlit_keydown import keydown

st.set_page_config(page_title="ハート移動", layout="centered")
st.title("♥ を矢印キーで動かそう！")
# セッションステートで位置管理
if "x" not in st.session_state:
   st.session_state.x = 0
if "y" not in st.session_state:
   st.session_state.y = 0
# キー入力を取得
key = keydown("矢印キーで操作してください")
# キーに応じて位置を更新
if key == "ArrowUp":
   st.session_state.y -= 1
elif key == "ArrowDown":
   st.session_state.y += 1
elif key == "ArrowLeft":
   st.session_state.x -= 1
elif key == "ArrowRight":
   st.session_state.x += 1
# 描画（空白で位置調整）
for y in range(-5, 6):
   line = ""
   for x in range(-10, 11):
       if x == st.session_state.x and y == st.session_state.y:
           line += "♥"
       else:
           line += " "
   st.text(line)