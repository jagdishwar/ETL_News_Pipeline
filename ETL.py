import pandas as pd
import sqlite3
import logging
from newsapi import NewsApiClient

news_api_key = "3fed3924473c4572acd085a352d87ea8"  # Replace with your actual API key
news_api = NewsApiClient(api_key=news_api_key)


def extract_news_data():
    try:
        result = news_api.get_everything(q="AI", language="en",sort_by='publishedAt')
        logging.info("Connection is successful.")
        return result["articles"]
    except:
        logging.error("Connection is unsuccessful.")
        return None

articles = extract_news_data()

print(articles[:3])

def clean_author_column(text):
    try:
        return text.split(",")[0].title()
    except AttributeError:
        return "No Author"


def transform_news_data(articles):
    article_list = []
    for i in articles:
        article_list.append([value.get("name", 0) if key == "source" else value for key, value in i.items() if
                             key in ["author", "title", "publishedAt", "content", "url", "source"]])

    df = pd.DataFrame(article_list, columns=["Source", "Author Name", "News Title", "URL", "Date Published", "Content"])

    df["Date Published"] = pd.to_datetime(df["Date Published"]).dt.strftime('%Y-%m-%d %H:%M:%S')
    df["Author Name"] = df["Author Name"].apply(clean_author_column)

    return df


transformed_data = transform_news_data(articles)

print(transformed_data)


def load_news_data(data):
    with sqlite3.connect("news_data.sqlite") as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS news_table (
                "Source" VARCHAR(30),
                "Author Name" TEXT,
                "News Title" TEXT,
                "URL" TEXT,
                "Date Published" TEXT,
                "Content" TEXT
            )
        ''')
    data.to_sql(name="news_table", con=connection, index=False, if_exists="append")


load_news_data(transformed_data)