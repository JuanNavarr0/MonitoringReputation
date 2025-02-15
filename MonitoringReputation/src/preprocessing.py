import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text.strip()

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    words = word_tokenize(text)
    filtered_words = [stemmer.stem(word) for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def process_news_data(input_file="data/news_articles.csv", output_file="data/processed_news.csv"):
    df = pd.read_csv(input_file)
    df['clean_content'] = df['content'].astype(str).apply(clean_text)
    df['processed_content'] = df['clean_content'].apply(preprocess_text)
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    process_news_data()