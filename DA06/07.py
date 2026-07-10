import numpy as np
import matplotlib.pyplot as plt

numbers = np.random.randn(10000)
plt.hist(numbers, bins=20)
plt.title("Histogram")
plt.show()