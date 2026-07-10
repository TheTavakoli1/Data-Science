import numpy as np

x = np.array([1, 2, 3, 4, 5_000])
print(np.mean(x)) # --> Vulnerability
print(np.median(x)) # --> Ok