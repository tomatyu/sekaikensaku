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

# Function to display map and handle game logic
def display_map_and_game():
    st.subheader('地図を問題にして国名を当てるゲームです')
    
    # Randomly select a country from the dataframe
    random_country = random.choice(countries_df["国名"].tolist())
    
    # Retrieve country data
    country_data = countries_df[countries_df["国名"] == random_country]
    
    # Display map for the selected country
    st.map(pd.DataFrame({'lat': [country_data["緯度"].values[0]],
                         'lon': [country_data["経度"].values[0]]}), zoom=4)
    
    # Game section
    st.write("この国はどこでしょう？")
    country_guess = st.text_input("国名を入力してください")
    
    if country_guess.strip().lower() == random_country.lower():
        st.write("正解です！")
        if random_country not in visited_countries:
            visited_countries.append(random_country)
    else:
        st.write("残念、不正解です。正解は:", random_country)

# Main part of the app
st.write("地図を問題にして国名を当てるゲームです。")

if len(visited_countries) < len(countries_df):
    display_map_and_game()
else:
    st.write("すべての国を訪れました！おめでとうございます！")
