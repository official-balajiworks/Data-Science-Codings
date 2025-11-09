import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Gender': ['Male','Female','Male','Female','Male','Female','Male','Female','Male','Female'],
    "Marks": [85,90,78,92,88,85,91,87,83,89]}
df = pd.DataFrame(data)           
sns.boxplot(x='Gender', y='Marks', data=df)
plt.title("Marks by Gender (Numerical vs Categorical)")
plt.show()
