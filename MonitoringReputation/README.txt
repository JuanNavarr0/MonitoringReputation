# 📰 Monitoring Reputation - News Sentiment & Topic Analysis

🚀 **A Machine Learning pipeline for collecting, processing, and analyzing news articles.**

## 📌 Project Overview
This project automates the process of **news monitoring and sentiment analysis**. It:
- Fetches news articles from an external API.
- Cleans and preprocesses the text.
- Performs **topic modeling** using LDA.
- Conducts **sentiment analysis** using NLP models.

## 🏗️ Tech Stack
- **Data Collection**: `requests`, `pandas`
- **Text Processing**: `nltk`, `gensim`
- **Machine Learning**: `transformers`, `torch`
- **Visualization**: `matplotlib`, `seaborn`, `wordcloud`

## 🛠️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MonitoringReputation.git
   cd MonitoringReputation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API key in `data_collection.py`:
   ```python
   API_KEY = "your_api_key_here"
   ```
4. Run the project:
   ```bash
   python main.py
   ```

## 📊 Expected Output
- **Dataset of news articles** (CSV format)
- **Preprocessed text** ready for analysis
- **LDA topic modeling** visualizations
- **Sentiment analysis results**

## 📎 License
This project is licensed under the MIT License.