import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

populations = np.random.randint(low=160, high=190, size=100)
mean = np.mean(populations)
std = np.std(populations)

# upper line
# upper_line = mean + std
upper_line = mean + 2 * std


# lower line
# lower_line = mean - std
lower_line = mean - 2 * std


plt.scatter(range(len(populations)), populations)
plt.plot([0, 100], [upper_line, upper_line], color="green")
plt.plot([0, 100], [mean, mean], color="Blue")
plt.plot([0, 100], [lower_line, lower_line], color="red")
plt.title("Population Distribution")
plt.xlabel("Population")
plt.ylabel("Density")
plt.show()