from data_collection import fetch_news, save_news_to_csv
from preprocessing import process_news_data
from lda_model import train_lda_model
from sentiment_analysis import analyze_sentiment

def main():
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    print("Fetching news articles...")
    articles = fetch_news(API_KEY)
    save_news_to_csv(articles)
    
    print("Processing news data...")
    process_news_data()
    
    print("Training LDA model...")
    model, dictionary, corpus = train_lda_model()
    print("LDA model training completed.")
    
    print("Performing sentiment analysis...")
    analyze_sentiment()
    print("Sentiment analysis completed.")

if __name__ == "__main__":
    main()
