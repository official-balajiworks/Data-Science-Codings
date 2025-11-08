from sklearn.preprocessing import OneHotEncoder
import pandas as pd

data = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Red']})

encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded = encoder.fit_transform(data[['Color']])

print(encoded)
