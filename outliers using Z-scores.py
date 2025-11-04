import numpy as np

data = [10, 12, 13, 12, 11, 14, 13, 100]  # 100 is an outlier

mean = np.mean(data)
std = np.std(data)

z_scores = [(x - mean) / std for x in data]
outliers = [x for x, z in zip(data, z_scores) if abs(z) > 3]

print("Z-scores:", z_scores)
print("Outliers:", outliers)
