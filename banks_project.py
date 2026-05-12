from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

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

df = extract(url)

print(df)

log_progress("Data extraction complete. Initiating Transformation process")