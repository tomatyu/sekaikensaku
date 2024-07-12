import streamlit as st
import pandas as pd

# Sample countries dataframe (replace this with your actual data)
countries_data = {
    "国名": ["Japan", "United States", "China"],
    "首都": ["Tokyo", "Washington D.C.", "Beijing"],
    "GDP": [5081, 21433, 14342],  # Example GDP values
    "概要": ["Japan overview", "US overview", "China overview"],
    "緯度": [35.6895, 38.8951, 39.9042],  # Example latitude values
    "経度": [139.6917, -77.0364, 116.4074]  # Example longitude values
}

countries_df = pd.DataFrame(countries_data)

# Initialize GDP data (if not already initialized)
if 'gdp_data' not in st.session_state:
    st.session_state['gdp_data'] = {'Country': [], 'GDP': []}

elif tab == '国検索':
    st.write("国名を入力してください（適用していない国もあります）")
    a = st.text_input("")
    
    if st.button('国を表示'):
        if a.strip() != "":
            selected_country = countries_df[countries_df["国名"] == a]
            
            if not selected_country.empty:
                selected_country = selected_country.iloc[0]
                st.write("国名:", selected_country["国名"])
                st.write("首都:", selected_country["首都"])
                st.write("GDP:", selected_country["GDP"])
                st.write("概要:", selected_country["概要"])

                # 地図表示
                st.subheader('国の地図')
                st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=4)

                # 選択された国のGDPデータをgdp_dataに追加する
                if selected_country["国名"] not in st.session_state['gdp_data']['Country']:
                    st.session_state['gdp_data']['Country'].append(selected_country["国名"])
                    st.session_state['gdp_data']['GDP'].append(selected_country["GDP"])

                # ゲームの部分
                st.write("次の国の首都を当ててください！")
                capital_guess = st.text_input("首都の名前を入力してください")
                
                if capital_guess.strip().lower() == selected_country["首都"].lower():
                    st.write("正解です！")
                else:
                    st.write("残念、不正解です。正解は:", selected_country["首都"])

            else:
                st.write("検索結果なし")

# Display collected GDP data
st.write("収集されたGDPデータ:", st.session_state['gdp_data'])
