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
                width: fit-content;
            }
            .bubble::after {
                content: '';
                position: absolute;
                top: 50%;
                left: -10px;
                border-style: solid;
                border-width: 10px 10px 10px 0;
                border-color: transparent #f0f0f0 transparent transparent;
                transform: translateY(-50%);
            }
        </style>
    '''
    bubble_html = f'''
        <div class="bubble">
            <div style="text-align: left;">
                {text}
            </div>
        </div>
    '''
    st.markdown(bubble_style, unsafe_allow_html=True)
    st.markdown(bubble_html, unsafe_allow_html=True)

# 使用例
right_aligned_bubble("ここに吹き出しの内容が入ります。この内容は左寄りになります。")
