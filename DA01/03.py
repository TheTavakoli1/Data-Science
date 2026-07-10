import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

days = np.array([1, 2, 3, 4, 5, 6, 7])

germany = np.array([12, 14, 17, 13, 18, 11, 7])
italy = np.array([14, 16, 21, 29, 20, 14, 17])

plt.plot(days, germany,
         color="blue",
         linestyle="dotted",
         label="Germany Death")

plt.plot(days, italy,
         color="red",
         marker="P",
         label="Italy Death")

plt.title("Comparison Of Germany and Italy Covid Death")
plt.xlabel("Days")
plt.ylabel("Death")

plt.legend()
plt.grid()

# plt.savefig("plot.jpg")
# plt.show()

df = pd.DataFrame(np.c_[days, germany, italy])
df.columns = ['Dayes', "Germany", "italy"]
print(df)

df.to_excel(r"Covid.xlsx", index=False)
