# To pull data about stock prices into a spreadsheet that is updated automatically, you can use Python's libraries such as pandas and yfinance. Here's a simple example:

# Install the required libraries by running the following command in your terminal:

# pip install pandas yfinance
# pip install openpyxl

# Import the necessary libraries in your Python script:

import pandas as pd
import yfinance as yf
# Define the stock symbols you want to retrieve data for:

stocks = ['AAPL', 'GOOGL', 'MSFT']
# Use the yf.download() function to fetch the stock data:

data = yf.download(stocks, start='2021-01-01', end='2021-12-31')
# Create a pandas DataFrame from the downloaded data:

df = pd.DataFrame(data['Adj Close'])
# Save the DataFrame to a spreadsheet file (e.g., CSV or Excel):

df.to_csv('stock_prices.csv')  # Save as CSV
df.to_excel('stock_prices.xlsx')
