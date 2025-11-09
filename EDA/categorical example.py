import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'Gender': ['Male']*60 + ['Female']*40})
sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution (Categorical Data)")
plt.show()
