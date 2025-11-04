import pandas as pd
import numpy as np

# Sample dataset with missing values
data = {
    'Age': [25, 30, np.nan, 40, 35],
    'Salary': [50000, 60000, 55000, np.nan, 52000],
    'Department': ['HR', 'IT', np.nan, 'Finance', 'IT']
}

df = pd.DataFrame(data)

print("Before filling missing values:\n")
print(df)

# ✅ Fill numeric columns with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# ✅ Fill numeric columns with median
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# ✅ Fill categorical columns with mode (most frequent value)
df['Department'].fillna(df['Department'].mode()[0], inplace=True)

print("\nAfter filling missing values:\n")
print(df)
