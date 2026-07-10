import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = yf.download(tickers="BTC-USD", start="2018-01-01", end="2019-02-01")
print(df)