import streamlit as st
import pandas as pd

# Function to load data from Excel file
def load_data():
    return pd.read_excel("28.xlsx")

# Load data from Excel file
countries_df = load_data()

# Initialize a list to store visited countries
visited_countries = []

# Function to display map and handle game logic
def display_map_and_game():
    st.subheader('国の地図を表示してください')
    
    # Ask the user to input a country name
    country_name = st.text_input("国名を入力してください")
    
    if st.button('地図を表示'):
        # Check if the input country exists in the data
        country_data = countries_df[countries_df["国名"] == country_name]
        
        if not country_data.empty:
            st.map(pd.DataFrame({'lat': [country_data["緯度"].values[0]],
                                 'lon': [country_data["経度"].values[0]]}), zoom=4)
            
            # Game section
            st.write("この国の首都は何ですか？")
            capital_guess = st.text_input("首都の名前を入力してください")

            if capital_guess.strip().lower() == country_data["首都"].values[0].lower():
                st.write("正解です！")
                if country_name not in visited_countries:
                    visited_countries.append(country_name)
            else:
                st.write("残念、不正解です。正解は:", country_data["首都"].values[0])
        else:
            st.write("国名が見つかりませんでした。正しい国名を入力してください。")

# Main part of the app
st.write("国の地図を表示し、その首都を当てるゲームです。")

if len(visited_countries) < len(countries_df):
    display_map_and_game()
else:
    st.write("すべての国を訪れました！おめでとうございます！")
