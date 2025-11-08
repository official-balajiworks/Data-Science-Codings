import pandas as pd

# Sample data
data = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Red']
})

# One-Hot Encoding
encoded = pd.get_dummies(data, columns=['Color'])
print(encoded)
