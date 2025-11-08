import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = pd.DataFrame({'Income': [10000, 20000, 50000, 200000, 1000000]})

# Apply log transformation
data['Log_Income'] = np.log10(data['Income'])

print(data)

# Plot
plt.figure(figsize=(6,4))
plt.subplot(1,2,1)
plt.hist(data['Income'], bins=5)
plt.title("Before Log Transformation")

plt.subplot(1,2,2)
plt.hist(data['Log_Income'], bins=5)
plt.title("After Log Transformation")
plt.show()
