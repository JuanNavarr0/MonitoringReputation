import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def display_head(df, num_rows=5):
    print(df.head(num_rows))