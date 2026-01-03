import numpy as np
import pandas as pd
import datetime
import yfinance as yf
import time

start_date = datetime.date(2022,1,1)
end_date = datetime.date.today()

stock_list = [
    'GOOGL',  # Google
    'META',   # Meta
    'MSFT',   # Microsoft
    'NFLX',   # Netflix
    'TSLA',   # Tesla
    'AMZN',   # Amazon
    'COST',   # Costco
    'AVGO',   # Broadcom
    'QBTS',   # Qbts
    'NVDA',   # Nvidia
    'AMD',    # AMD
    'SOUN',   # SoundHound AI
    'AAPL',   # Apple
    'AXP',    # American Express
    'COF',    # Capital One
    'JPM',    # Chase
    'PLTR',   # Palantir
    'WMT',    # Walmart  
    'QQQM',   # Investco 100
    'VOO'     # Vanguard S&P 500
]

all_stocks = list()

for stock in stock_list:
    data = yf.download(stock,start=start_date,end=end_date,auto_adjust=True)
    if data.empty:
        print(f"No data for {stock}")
        continue
    data = data.reset_index()
    data.columns = data.columns.get_level_values(0)
    data.columns.name = None
    data["Sym"] = stock
    time.sleep(5)
    all_stocks.append(data)

df = pd.concat(all_stocks,ignore_index=True)
print(f"\nTotal rows downloaded: {len(df)}")
print(df.head())
df.to_csv('stocks.csv')