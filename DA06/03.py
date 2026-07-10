import matplotlib.pyplot as plt
import numpy as np

productions = ["Mobile", "Laptop", "Mobile", "Mobile", "Laptop", "Speaker", "Speaker", "Mobile"]
plt.figure()
plt.barh(productions, range(len(productions)), color="green")
plt.title("Productions Density")
plt.xlabel("Density")
plt.ylabel("Productions")
plt.show()