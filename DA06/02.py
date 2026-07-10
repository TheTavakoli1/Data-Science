import matplotlib.pyplot as plt
import numpy as np

productions = ["Mobile", "Laptop", "Speaker"]
count = [3, 4, 2]
plt.bar(productions, count, color="green")
plt.title("Productions Density")
plt.xlabel("Productions")
plt.ylabel("Density")
plt.show()