import pandas as pd

def load_data(file="Task-1\customer_service_interactions.csv"):
    try:
        return pd.read_csv(file)
    except FileNotFoundError:
        print(f"[ERROR] {file} not found.")
        return pd.DataFrame()

def total_queries(df):
    return len(df)

def most_common_topics(df, top_n=5):
    if 'topic' in df.columns:
        return df['topic'].value_counts().head(top_n)
    return {}

def average_satisfaction(df):
    if 'satisfaction' in df.columns:
        return round(df['satisfaction'].dropna().astype(float).mean(), 2)
    return "N/A"
