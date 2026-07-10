import time
import sys

start_time = time.time()

X = list(range(100_000_000))

for i in range(100_000_000):
    X[i] += 1

end_time = time.time()

print(end_time - start_time, "Second")
print(sys.getsizeof(X) / (1024 * 1024), "MB")


# 12.40372633934021 Second
# 762.9395065307617 MB