import streamlit as st
import requests

def fetch_news():
    # APIから最新のニュースを取得する関数
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",  # 例としてアメリカのニュースを取得する設定
        "apiKey": "YOUR_NEWSAPI_KEY"  # 自分のNews APIのAPIキーを入力してください
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']
        return articles
    else:
        st.error("Error fetching news")

def main():
    st.title("最新の世界情報")

    articles = fetch_news()

    for article in articles:
        st.markdown(f"### {article['title']}")
        st.write(article['description'])
        st.write(f"Source: {article['source']['name']}")
        st.write("---")

if __name__ == "__main__":
    main()
