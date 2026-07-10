import yfinance as yf

df = yf.download(tickers='USD-BTC', start='2019-01-01', end='2020-12-31')
print(df)
