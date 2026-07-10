import numpy as np


X = np.array([[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]],[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]],
              dtype= np.uint8)

print(X)
print(X.shape)
print(X.size)
print(X.ndim)
print(X.dtype)