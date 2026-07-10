# In Python, we used range to generate numerical sequences

# range(1, 11, 2) --> list, for loop

# 1 --> list(range(1, 11, 2))
# 2 --> for i in range(1, 11, 2):

"""And we can't use decimal numbers in range function
And the range is not a set of numbers,
it consists of 2 numbers.
"""

import numpy as np

# range(1, 11, 1.5) --> Error

# in numpy we used arange

# arr = np.arange(1, 11, 1, dtype=np.uint8) --> vector
# arr = np.arange(1, 11, dtype=np.uint8) --> vector
# arr = np.arange(11, dtype=np.uint8) --> vector

# lst = [[1, 2, 3], [2, 4, 6]]
# arr = np.array(lst, dtype=np.float32)

# arr = np.arange(1, 11, 0.5, dtype=uint8) --> Error
arr = np.arange(1, 11, 1, dtype=np.uint8)
print(arr * 1.3)

