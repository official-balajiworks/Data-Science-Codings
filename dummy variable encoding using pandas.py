import pandas as pd

# Sample data
df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Red']})

# Dummy Variable Encoding
encoded = pd.get_dummies(df, columns=['Color'], drop_first=True)
print(encoded)
