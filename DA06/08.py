import numpy as np
import matplotlib.pyplot as plt

numbers = np.random.normal(loc=0, scale=1, size=10000)
plt.hist(numbers, bins=20)
plt.title("Histogram")
plt.show()