import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

# Load the data initially
@st.cache
def load_data():
    return pd.read_excel("17.xlsx")

# Load countries data
countries_df = load_data()

# Define initial 7 major countries GDP data
gdp_data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'UK', 'India', 'France'],
    'GDP': [23.5, 14.3, 5.1, 4.2, 2.9, 2.8, 2.7]
}

# Streamlit app setup
st.title("世界検索")
st.write("好きな国を検索して、:red[知識] を見つけましょう！")
a = st.text_input("国名を入力してください（適用していない国もあります）")

# Country search button
if st.button('国検索'):
    if any(countries_df["国名"] == a):
        with st.spinner("検索中....."):
            time.sleep(1)

        selected_country = countries_df[countries_df["国名"] == a].iloc[0]
        st.write("国名:", selected_country["国名"])
        st.write("首都:", selected_country["首都"])
        st.write("GDP:", selected_country["GDP"])
        st.write("概要:", selected_country["概要"])

        # Update gdp_data with selected country if it's not already in the list
        if selected_country["国名"] not in gdp_data['Country']:
            gdp_data['Country'].append(selected_country["国名"])
            gdp_data['GDP'].append(selected_country["GDP"])

        # Map display
        st.map(pd.DataFrame({'lat': [selected_country["緯度"]], 'lon': [selected_country["経度"]]}), zoom=2)
    else:
        st.write("検索結果なし")

# GDP search button
if st.button('国のGDP検索'):
    # Convert gdp_data to DataFrame
    df = pd.DataFrame(gdp_data)

    # Streamlit app setup for GDP comparison
    st.title('7大国のGDPをバーチャートで表示するアプリ')

    # Display raw data (optional)
    if st.checkbox('生データを表示する'):
        st.write(df)

    # Plot bar chart
    st.subheader('7大国のGDPの比較')

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot bar chart
    ax.bar(df['Country'], df['GDP'], color='red')  # Example using bar plot (displayed in red)

    # Highlight the selected country in a different color
    if a in df['Country'].values:
        idx = df.index[df['Country'] == a][0]
        ax.bar(df['Country'][idx], df['GDP'][idx], color='blue')  # Highlight selected country in blue

    # Set axis labels and title
    ax.set_xlabel('国')
    ax.set_ylabel('GDP (兆ドル単位)')
    ax.set_title('主要国のGDP')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Display the plot in Streamlit
    st.pyplot(fig)
