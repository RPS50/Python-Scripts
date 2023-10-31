import yfinance as yf
df = yf.download('TSLA', '2023-01-01')
df.to_csv('Tesla.csv')
