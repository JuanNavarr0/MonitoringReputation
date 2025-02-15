import pandas as pd
import gensim
import gensim.corpora as corpora
from gensim.models import LdaModel
from nltk.tokenize import word_tokenize

def train_lda_model(data_file="data/processed_news.csv", num_topics=5, passes=10):
    df = pd.read_csv(data_file)
    texts = [word_tokenize(doc) for doc in df['processed_content'].dropna()]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=passes)
    return lda_model, dictionary, corpus

if __name__ == "__main__":
    model, dictionary, corpus = train_lda_model()
    model.save("data/lda_model.model")
    print("LDA model saved successfully.")