Banks ETL Project
📊 Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline to process data about the world’s largest banks by market capitalization. The data is scraped from Wikipedia, transformed using exchange rates, and stored in both CSV and SQLite database formats for analysis.

🌐 Data Source

https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks

⚙️ What the Project Does

🔹 Extract
Scrapes banking data from a Wikipedia page using BeautifulSoup
Extracts the table of largest banks by market capitalization
Converts HTML table into a Pandas DataFrame
Cleans the market capitalization column

🔹 Transform
Renames column to MC_USD_Billion
Converts USD values into:
GBP
EUR
INR
Uses exchange rate values from a CSV file
Rounds values to 2 decimal places

🔹 Load
Saves transformed data into:
📁 CSV file (largest_banks.csv)
🗄️ SQLite database (Banks.db)

🔹 Query
Runs SQL queries on the database:
Full dataset view
Average market capitalization in GBP
Top 5 banks by market cap

🔹 Logging
Logs each step of the ETL pipeline into code_log.txt
Tracks execution timestamps and process flow
🛠️ Tools Used
Python
Pandas
NumPy
BeautifulSoup
Requests
SQLite3
📁 Project Structure
banks_project.py
exchange_rate.csv
largest_banks.csv
Banks.db
code_log.txt
▶️ How to Run
python3 banks_project.py
📊 Output Files

After running the script, the following files are generated:

largest_banks.csv → Cleaned dataset in CSV format
Banks.db → SQLite database containing bank data
code_log.txt → Execution logs of ETL pipeline

📌 Key Skills Demonstrated
Web scraping
Data cleaning and transformation
Currency conversion using exchange rates
Database operations with SQLite
SQL querying
ETL pipeline design


👤 Author
Fisayo
