from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Create 2D data (required for sklearn)
data = np.array([[10], [20], [30], [40], [50]])

# Initialize scaler
scaler = MinMaxScaler(feature_range=(0, 1))  # you can change to (-1,1) if needed

# Fit and transform data
normalized = scaler.fit_transform(data)

print("Normalized Data:\n", normalized)
