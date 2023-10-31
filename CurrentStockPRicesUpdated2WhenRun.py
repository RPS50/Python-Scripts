# install the 'openpyxl' library by running the following command in your terminal:

# pip install openpyxl

# pip install pandas yfinance schedule

import pandas as pd
import yfinance as yf
import os
from datetime import datetime, timedelta

# Define the stock symbols you want to retrieve data for:
stocks = ['AAPL', 'GOOGL', 'MSFT']

# Calculate the start and end dates for yesterday:
end_date = pd.Timestamp(datetime.now() - timedelta(1))
start_date = end_date

# Use the yf.download() function to fetch the stock data for yesterday:
data = yf.download(stocks, start=start_date, end=end_date, interval='1d')

# Create a pandas DataFrame from the downloaded data:
df = pd.DataFrame(data['Adj Close'])
df.index = data.index  # Set the index to the date and time

# Check if the file exists
file_path = 'stock_prices.csv'

if os.path.isfile(file_path):
    # If the file exists, append yesterday's data to it
    existing_data = pd.read_csv(file_path, index_col=0)
    yesterday_data = df.loc[df.index.date == pd.Timestamp(end_date).date()]
    updated_data = pd.concat([existing_data, yesterday_data])
    updated_data.to_csv(file_path)
else:
    # If the file doesn't exist, create a new file with yesterday's data
    df.to_csv(file_path)

print(f"Yesterday's stock data has been saved to {file_path}")
