import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("weather.csv")
print(df.columns)
plt.boxplot(df["relative_humidity_2m (%)"])
plt.show()