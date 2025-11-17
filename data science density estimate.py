import matplotlib.pyplot as plt
import numpy as np

ages = [12, 15, 22, 25, 32, 35, 36, 40, 42, 50, 55, 60, 65, 70, 75]

plt.hist(ages, bins=5, density=False, edgecolor='black')
plt.title("Age Distribution Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# With Density Estimation
plt.hist(ages, bins=5, density=True, edgecolor='black')
plt.title("Age Distribution (Density Estimate)")
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()
