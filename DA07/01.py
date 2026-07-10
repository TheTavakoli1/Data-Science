# Data Cleaning

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("weather.csv")
# 1
# print(df)
# print(type(df))

# 2
# print(df.info())
# print(df.describe())

# df["wind_speed_180m (km/h)"] = pd.to_numeric(df["wind_speed_180m (km/h)"], errors="raise")
# df["wind_speed_180m (km/h)"] = pd.to_numeric(df["wind_speed_180m (km/h)"], errors="ignore")
df["wind_speed_180m (km/h)"] = pd.to_numeric(df["wind_speed_180m (km/h)"], errors="coerce", downcast="float")
# df.dropna(inplace=True)
# df.fillna(100, inplace=True)
# print(np.mean(df["wind_speed_180m (km/h)"]))
df.fillna(np.mean(df["wind_speed_180m (km/h)"]), inplace=True)

# print(df)
# print(df.info())
# print(df.describe())
# print(df.head())
# print(df.tail())
print(df.index)
# print(df.columns)
df.rename(columns={"time": "date"}, inplace=True)
print(df.columns)
df.set_index(np.arange(1000, 1168), inplace=True)
# print(df.head())
df.reset_index(inplace=True)
print(df.head())
df.drop(0, axis=0, inplace=True)
print(df.head())
df.drop(["index"], axis=1, inplace=True)
print(df.head())