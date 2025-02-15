import pandas as pd
from transformers import pipeline

def analyze_sentiment(input_file="data/processed_news.csv", output_file="data/sentiment_news.csv"):
    df = pd.read_csv(input_file)
    sentiment_pipeline = pipeline("sentiment-analysis")
    df['sentiment'] = df['clean_content'].astype(str).apply(lambda x: sentiment_pipeline(x)[0]['label'])
    df.to_csv(output_file, index=False)
    print(f"Sentiment analysis results saved to {output_file}")

if __name__ == "__main__":
    analyze_sentiment()