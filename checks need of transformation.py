import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.Series([100, 200, 300, 1000, 10000, 50000])

print(data.skew())

# Plot histogram
sns.histplot(data, kde=True)
plt.title("Check Data Distribution")
plt.show()
print(data.skew())
