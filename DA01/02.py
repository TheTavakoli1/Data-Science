import time
import sys
import numpy as np

start_time = time.time()

X = np.arange(200_000_000) + 1

end_time = time.time()

print(end_time - start_time, "Second")
print(sys.getsizeof(X) / (1024 * 1024), "MB")


# 12.40372633934021 Second
# 762.9395065307617 MB

# 0.30721044540405273 Second
# 381.46983337402344 MB