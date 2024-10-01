# News Data Extraction, Transformation, and Loading (ETL) with NewsAPI

This project extracts news articles related to "AI" from the NewsAPI, transforms the data, and loads it into an SQLite database. The project leverages `pandas` for data manipulation and `sqlite3` for database storage.

## Features

- **Extract**: Connects to the NewsAPI to fetch articles related to "AI."
- **Transform**: Cleans and formats the article data, including:
  - Parsing dates.
  - Formatting author names.
- **Load**: Stores the transformed data into an SQLite database for further analysis.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.x**
- `pandas` library for data manipulation
- `sqlite3` for database interaction
- `newsapi-python` to interact with the NewsAPI

You can install the required libraries by running:

```bash
pip install pandas sqlite3 newsapi-python
