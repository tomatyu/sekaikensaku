import streamlit as st
import time

# 初期化
if 'x' not in st.session_state:
    st.session_state.x = 200
if 'y' not in st.session_state:
    st.session_state.y = 200

# 矢印キーに基づく点の移動
def move_point():
    if 'key' in st.session_state:
        if st.session_state.key == 'ArrowUp':
            st.session_state.y -= 10
        elif st.session_state.key == 'ArrowDown':
            st.session_state.y += 10
        elif st.session_state.key == 'ArrowLeft':
            st.session_state.x -= 10
        elif st.session_state.key == 'ArrowRight':
            st.session_state.x += 10

# キー入力の監視
st.title('キーボードの矢印キーで点を移動')

key = st.text_input('矢印キーで点を動かしてください', value='', max_chars=1)
if key:
    st.session_state.key = key
else:
    st.session_state.key = None

move_point()

# 点の表示
st.write(f"点の位置: ({st.session_state.x}, {st.session_state.y})")

# 点の描画（簡単な描画）
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(st.session_state.x, st.session_state.y, 'ro')  # 赤い点
ax.set_xlim(0, 400)
ax.set_ylim(0, 400)
plt.gca().invert_yaxis()  # Streamlitはy軸が逆なので補正
st.pyplot(fig)

time.sleep(0.2)
