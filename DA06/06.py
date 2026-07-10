import numpy as np
import matplotlib.pyplot as plt

numbers = np.random.uniform(low=0, high=10, size=1000)
plt.hist(numbers, bins=30)
plt.title("Uniform Distribution (0,10)")
plt.xlabel("Numbers")
plt.ylabel("Density")
plt.show()