import streamlit as st

def right_aligned_bubble(text):
    bubble_style = '''
        <style>
            .bubble {
                position: relative;
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                text-align: right;
                margin: 10px 0;
            }
            .bubble::after {
                content: '';
                position: absolute;
                top: 50%;
                right: -10px;
                border-style: solid;
                border-width: 10px 0 10px 10px;
                border-color: transparent transparent transparent #f0f0f0;
                transform: translateY(-50%);
            }
        </style>
    '''
    bubble_html = f'''
        <div class="bubble">
            {text}
        </div>
    '''
    st.markdown(bubble_style, unsafe_allow_html=True)
    st.markdown(bubble_html, unsafe_allow_html=True)

# 使用例
right_aligned_bubble("ここに吹き出しの内容が入ります。")
