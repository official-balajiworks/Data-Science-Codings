import pandas as pd

data = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90, 150]  # 150 is an outlier
Q1 = pd.Series(data).quantile(0.25)
Q3 = pd.Series(data).quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = [x for x in data if x < lower or x > upper]
print("Outliers:", outliers)
