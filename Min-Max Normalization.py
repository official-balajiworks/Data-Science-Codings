import numpy as np

# Original data
data = np.array([10, 20, 30, 40, 50])

# Min-Max Normalization
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

print("Original:", data)
print("Normalized:", normalized)
