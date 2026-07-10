import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-5, 5, 1000)
y = norm.pdf(x, loc=0, scale=1)
mean = 0
median = 0
mode = 0
plt.plot(x, y)
plt.axvline(mean, linestyle='dashed', )
plt.axvline(median, linestyle='dashed')
plt.axvline(mode, linestyle='dashed')
plt.title("Normal Distribution")
plt.grid(True)
plt.show()