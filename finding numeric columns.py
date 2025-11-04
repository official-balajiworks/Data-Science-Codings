import pandas as pd

# Example: create or load a dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Height': [5.5, 6.0, 5.8, 5.9],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

df = pd.DataFrame(data)

# Method 1: Using select_dtypes()
numeric_columns = df.select_dtypes(include=['number']).columns

print("Numeric Columns:")
print(numeric_columns)
