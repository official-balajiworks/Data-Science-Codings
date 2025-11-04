import pandas as pd

# Sample dataset
data = {
    'Age': [22, 25, 24, 30, 28, 120, 26, 23, 27, 29],
    'Salary': [30000, 32000, 31000, 35000, 34000, 1000000, 33000, 30000, 36000, 37000]
}

df = pd.DataFrame(data)

print("Before removing outliers:\n")
print(df)

# ✅ Calculate Q1 (25%), Q3 (75%) and IQR
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# ✅ Define acceptable range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# ✅ Remove outliers
df= df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]

print("\nAfter removing outliers:\n")
print(df)
