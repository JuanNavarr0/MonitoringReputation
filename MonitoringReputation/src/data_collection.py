import requests
import pandas as pd

def fetch_news(api_key, query="Kamala Harris OR Donald Trump", date="2024-09-28", language="en"):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': query,
        'from': date,
        'language': language,
        'sortBy': 'relevancy',
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        print(f"Error fetching news: {response.status_code}")
        return []

def save_news_to_csv(articles, filename="data/news_articles.csv"):
    df = pd.DataFrame([{
        'source_name': article['source']['name'],
        'author': article['author'],
        'title': article['title'],
        'description': article['description'],
        'url': article['url'],
        'published_at': article['publishedAt'],
        'content': article['content']
    } for article in articles])
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} articles to {filename}")

if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your API key
    articles = fetch_news(API_KEY)
    save_news_to_csv(articles)
