import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from googletrans import Translator

# 7 major countries GDP data in trillion dollars
gdp_data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'UK', 'India', 'France'],
    'GDP (trillion $)': [23.5, 14.3, 5.1, 4.2, 2.9, 2.8, 2.7]
}

# Convert GDP values to trillion dollars (if needed)
df = pd.DataFrame(gdp_data)

# Streamlit application title
st.title('GDP Comparison of 7 Major Countries')
if .button('全体を翻訳する'):
    # ここに全体を翻訳する処理を記述する（例として、'Hello'を日本語に翻訳する）
    translation = translator.translate('Hello', dest='ja').text
    st.write(f'翻訳結果: {translation}')

# Display raw data as an option
if st.checkbox('Show raw data'):
    st.write(df)

# Plotting the bar chart
st.subheader('Comparison of GDP (trillion $)')

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting the bar chart
ax.bar(df['Country'], df['GDP (trillion $)'], color='blue')

# Setting labels and title
ax.set_xlabel('Country')
ax.set_ylabel('GDP (trillion $)')
ax.set_title('GDP of Major Countries')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot in Streamlit
st.pyplot(fig)
