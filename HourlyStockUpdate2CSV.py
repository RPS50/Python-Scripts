# To pull data about stock prices into a spreadsheet that is updated automatically, you can use Python's libraries such as pandas and yfinance. Here's a simple example:
# To automatically change the date to today's date for the hourly updates, you can use the datetime module in Python. Here's an updated example:


# Install the required libraries by running the following command in your terminal:

# pip install pandas yfinance
# pip install pandas yfinance schedule
# pip install openpyxl

# Import the necessary libraries in your Python script:

##import pandas as pd
##import yfinance as yf
##import schedule
##import time
##from datetime import datetime
##Define the function to fetch and save the stock data:
##
##def fetch_stock_data():
##    stocks = ['AAPL', 'GOOGL', 'MSFT']
##    data = yf.download(stocks, start='2022-01-01', end='2022-01-01')
##    df = pd.DataFrame(data['Adj Close'])
##    df.to_csv('stock_prices.csv')  # Save as CSV
##Schedule the function to run every hour:
##
##schedule.every().hour.do(fetch_stock_data)
##Run the scheduled task in an infinite loop:
##
##while True:
##    schedule.run_pending()
##    time.sleep(1)

import pandas as pd
import yfinance as yf
import schedule
import time
from datetime import datetime

# Define the function to fetch and save the stock data:
def fetch_stock_data():
    stocks = ['AAPL', 'GOOGL', 'MSFT']
    today = datetime.today().strftime('%Y-%m-%d')
    data = yf.download(stocks, start=today, end=today)
    df = pd.DataFrame(data['Adj Close'])
    df.to_csv('Hourly_stock_prices' + today + '.csv')  # Save as CSV

# Schedule the function to run every hour:
schedule.every().hour.do(fetch_stock_data)

# Run the scheduled task in an infinite loop:
while True:
    schedule.run_pending()
    time.sleep(1)
