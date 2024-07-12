import streamlit as st
import pandas as pd
import random

# Function to load data from Excel file
def load_data():
    return pd.read_excel("28.xlsx")

# Load data from Excel file
countries_df = load_data()

# Initialize a list to store visited countries
visited_countries = []

# Global variables for game state
random_country = None
country_data = None
correct_answer = None
user_answer = None

# Function to initialize game state
def initialize_game():
    global random_country, country_data, correct_answer, user_answer
    random_country = random.choice(countries_df["国名"].tolist())
    country_data = countries_df[countries_df["国名"] == random_country]
    correct_answer = random_country
    user_answer = None

# Function to display map and handle game logic
def display_map_and_game():
    global user_answer
    
    st.subheader('地図を問題にして国名を当てるゲームです')
    
    # Display map for the selected country
    st.map(pd.DataFrame({'lat': [country_data["緯度"].values[0]],
                         'lon': [country_data["経度"].values[0]]}), zoom=4)
    
    # Display game prompt and input field
    st.write("この国はどこでしょう？")
    user_answer = st.text_input("国名を入力してください")
    
    # Display answer button
    if st.button('回答する'):
        if user_answer.strip().lower() == correct_answer.lower():
            st.write("正解です！")
            if correct_answer not in visited_countries:
                visited_countries.append(correct_answer)
            initialize_game()  # Reset for the next question
        else:
            st.write(f"残念、不正解です。正解は: {correct_answer}")

# Main part of the app
st.write("地図を問題にして国名を当てるゲームです。")

if len(visited_countries) < len(countries_df):
    if random_country is None:
        initialize_game()  # Initialize game state for the first question
    display_map_and_game()
else:
    st.write("すべての国を訪れました！おめでとうございます！")
