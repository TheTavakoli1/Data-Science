import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# x = (1797, 64)
# y = (1797,)
X, y = load_digits(return_X_y=True)
# print(X.shape)
# print(y.shape)

number = 1356
plt.imshow(X[number].reshape((8, 8)), cmap='gray')
plt.title(y[number])
print(X[number].reshape((8, 8)))
plt.show()
