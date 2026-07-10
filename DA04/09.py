import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = yf.download(tickers="BTC-USD", start="2020-12-17", end="2024-01-10")
mean = np.mean(df["Close"].values)
print(df)
plt.plot([0, 1118], [mean, mean], "k--", color="red", linewidth=2)
plt.plot(df["Close"].values)
plt.legend()
plt.show()
