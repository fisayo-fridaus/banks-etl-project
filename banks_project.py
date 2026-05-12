from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import sqlite3

def log_progress(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("code_log.txt", "a") as f:
        f.write(timestamp + " : " + message + "\n")

log_progress("Preliminaries complete. Initiating ETL process")

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"

def extract(url):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    tables = data.find_all('table')
    df = pd.read_html(str(tables[0]))[0]
    df["Market cap (US$ billion)"] = df["Market cap (US$ billion)"].astype(str).str.replace("\n", "")
    df["Market cap (US$ billion)"] = df["Market cap (US$ billion)"].astype(float)
    df = df.rename(columns={"Market cap (US$ billion)": "MC_USD_Billion"})
    return df

exchange_rate_df = pd.read_csv("exchange_rate.csv")
exchange_rate = exchange_rate_df.set_index('Currency').to_dict()['Rate']

df = extract(url)

print(df)

log_progress("Data extraction complete. Initiating Transformation process")

def transform(df, exchange_rate):

    gbp_rate = float(exchange_rate['GBP'])
    df['MC_GBP_Billion'] = [
        np.round(x * gbp_rate, 2) for x in df['MC_USD_Billion']
    ]

    eur_rate = float(exchange_rate['EUR'])
    df['MC_EUR_Billion'] = [
        np.round(x * eur_rate, 2) for x in df['MC_USD_Billion']
    ]

    inr_rate = float(exchange_rate['INR'])
    df['MC_INR_Billion'] = [
        np.round(x * inr_rate, 2) for x in df['MC_USD_Billion']
    ]

    return df

df = transform(df, exchange_rate)

#print(df)

log_progress("Data transformation complete")

print(df['MC_EUR_Billion'][4])

def load_to_csv(df, output_path):

    df.to_csv(output_path, index=False)

    log_progress("Data saved to CSV file")

output_path = "largest_banks.csv"
load_to_csv(df, output_path)

def load_to_db(df, connection, table_name):

    df.to_sql(table_name, connection, if_exists='replace', index=False)

    log_progress("Data loaded to Database as a table, Executing queries")


connection = sqlite3.connect("Banks.db")

load_to_db(df, connection, "Largest_banks")

def run_queries(query, connection):

    print("\nQuery:", query)

    cursor = connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        print(row)


# Query 1: Full table
run_queries("SELECT * FROM Largest_banks", connection)

# Query 2: Average GBP market cap
run_queries("SELECT AVG(MC_GBP_Billion) FROM Largest_banks", connection)

# Query 3: Top 5 banks
run_queries('SELECT "Bank name" FROM Largest_banks LIMIT 5', connection)


connection.close()

log_progress("Server Connection closed")
log_progress("Process Complete")