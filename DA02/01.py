# x = [1, 2, 3.14, True, "Ahmad"]


# just multiplication

x = [1, 2, 3, 4, 5]
# print(x * 2)

# print(x+2) --> Error
# print(x + [5, 5, 5]) --> Extend

# 1
# for i in range(len(x)):
#     x[i] *= 2

# 2 map, lambda --> more speed than for loop
# def zarb(number):
#     return number * 2

# print(list(map(lambda x: x * 2, x)))

# filter, lambda
# print(list(filter(lambda x: x % 2 != 0, x)))

from functools import reduce
print(reduce(lambda x, y: x + y, x))