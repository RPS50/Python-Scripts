##import yfinance as yf
##
### Define the stock symbol
##symbol = 'GOOGL'
##
### Fetch the stock data from Yahoo Finance
##stock = yf.Ticker(symbol)
##
### Get the current stock price
##current_price = stock.history().tail(1)['Close'].iloc[0]
##
### Write the stock price to a file
##with open(symbol + '.txt', 'w') as file:
##    file.write(f'The current stock price of {symbol} is {current_price}')
##
##print('Stock price written to file.')

# Here's an updated version of the script that fetches stock prices for multiple symbols (AAPL and MSFT) and writes them to a file:

##import yfinance as yf
##import datetime
##
### Define the stock symbols
##symbols = ['AAPL', 'MSFT', "GOOG"]
##symbols_string = ' '.join(symbols)
##
### Fetch the stock data from Yahoo Finance for each symbol
##stock_data = yf.download(symbols, period='1d', interval='1d')['Close']
##
### Get the current stock prices for each symbol
##current_prices = stock_data.iloc[-1]
##
### Get the current date
##current_date = datetime.date.today()
##
### Write the stock prices to a file
##with open('stock_prices' + symbols_string + '.txt', 'w') as file:
##    file.write('Date\t\tSymbol\tPrice\n')
##    for symbol, price in current_prices.items():
##        file.write(f'{current_date}\t{symbol}\t{price}\n')
##
##print('Stock prices written to file.')

import yfinance as yf
import datetime
import csv

# Define the stock symbols
symbols = ['AAPL', 'ABBV', 'AEP', 'AMD', 'AMRC', 'AMZN', 'APHA', 'AQB', 'AYX', 'BA', 'BABA', 'BBBY', 'BRK.B', 'BROS', 'CCI', 'CL', 'COIN', 'CRM', 'CSCO', 'CURRENCY:BTCUSD', 'CURRENCY:ETHUSD', 'CVS', 'CVX', 'DIS', 'DISCK', 'DNKN', 'DOMO', 'DOW', 'F', 'FSLY', 'GNUS', 'GOOG', 'GRTS', 'GRWG', 'GS', 'GT', 'HON', 'INSG', 'INTC', 'LAD', 'LHX', 'LLY', 'LMND', 'MAT', 'META', 'MLM', 'MS', 'MSFT', 'MU', 'NCNO', 'NVDA', 'ORI', 'PANW', 'PATH', 'PAYX', 'PENN', 'PINS', 'PLUG', 'PYPL', 'QS', 'RBLX', 'RPRX', 'RUN', 'SBUX', 'SNOW', 'STZ', 'SWKS', 'TEAM', 'THO', 'TJX', 'TLRY', 'TPGY', 'TSCO', 'TSLA', 'TTD', 'TTWO', 'UAL', 'UNP', 'VERU', 'VFIAX', 'VMW', 'VTI', 'VZ', 'WBD', 'WYNN', 'ZUO'
]
symbols_string = ' '.join(symbols)


# Fetch the stock data from Yahoo Finance for each symbol
stock_data = yf.download(symbols, period='1d', interval='1d')['Close']

# Get the current stock prices for each symbol
current_prices = stock_data.iloc[-1]

# Get the current date
current_date = datetime.date.today()

# Write the stock prices to a CSV file
# filename = 'stock_prices for ' + symbols_string + '.csv'
filename = 'stock_prices for my portfolio.csv'
with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date'] + symbols)
    writer.writerow([current_date] + [current_prices[symbol] for symbol in symbols])

print(f'Stock prices written to {filename}.')
