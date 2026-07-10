from scipy.stats import mode
import numpy as np

# Mode
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1])
print(mode(x))
