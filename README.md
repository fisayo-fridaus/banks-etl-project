# Banks ETL Project

## Project Overview
This project extracts data about the largest banks by market capitalization from a Wikipedia page and processes it using Python.

## Data Source
https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks

## What the Project Does
- Extracts bank data from a webpage
- Converts HTML table into a Pandas DataFrame
- Cleans market capitalization values
- Renames columns for clarity
- Displays structured data
- Logs each step of the process

## Tools Used
- Python
- Pandas
- BeautifulSoup
- Requests

## How to Run
```bash
python3 banks_project.py
