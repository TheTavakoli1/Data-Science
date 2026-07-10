# Scikit Learn
# from sklearn.datasets
# from sklearn.preprocessing
# Mnist(60_000(28*28))Train, (10_000(28*28))Test --> Mnist(fetch)

from sklearn.datasets import load_digits

data = load_digits()
print(data)
print(type(data))