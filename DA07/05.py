import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

# (70000, 784)
# (70000,)
X, y = fetch_openml("mnist_784", return_X_y=True)
print(X)
print(type(X))

number = 2
plt.imshow(X.iloc[number].values.reshape(28, 28), cmap="gray")
plt.title(y[number])
plt.show()