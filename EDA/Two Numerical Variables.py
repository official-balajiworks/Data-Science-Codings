import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'Hours_Studied': [2, 4, 6, 8, 10],
    'Marks': [50, 65, 70, 85, 90]
})
sns.scatterplot(x='Hours_Studied', y='Marks', data=df)
plt.title("Hours vs Marks (Two Numerical Variables)")
plt.show()
