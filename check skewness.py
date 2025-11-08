import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example DataFrame
df = pd.DataFrame({'Income': [1000, 2000, 5000, 20000, 100000, 500000]})

# 1. Check basic stats
print(df['Income'].describe())

# 2. Check distribution
sns.histplot(df['Income'], kde=True)
plt.show()

# 3. Check skewness
print("Skewness:", df['Income'].skew())
