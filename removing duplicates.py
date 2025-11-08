# --------------------------------------------
# 🧹 Removing Duplicates from a Dataset using Pandas
# --------------------------------------------

import pandas as pd

# Load dataset (change 'data.csv' to your file name)
df = pd.read_csv("data.csv")

# --------------------------------------------
# 1️⃣ View the original dataset
# --------------------------------------------
print("Original Data:")
print(df)

# --------------------------------------------
# 2️⃣ Remove all duplicate rows (keep first occurrence)
# --------------------------------------------
df_no_duplicates = df.drop_duplicates()

# --------------------------------------------
# 3️⃣ Remove duplicates based on specific column(s)
# Example: Remove duplicates only based on 'Name' and 'Age'
# --------------------------------------------
df_no_duplicates_cols = df.drop_duplicates(subset=['Name', 'Age'])

# --------------------------------------------
# 4️⃣ Keep only the last occurrence of duplicates
# --------------------------------------------
df_keep_last = df.drop_duplicates(keep='last')

# --------------------------------------------
# 5️⃣ Remove ALL duplicates (no occurrence kept)
# --------------------------------------------
df_remove_all = df.drop_duplicates(keep=False)

# --------------------------------------------
# 6️⃣ Save the cleaned dataset to a new file
# --------------------------------------------
df_no_duplicates.to_csv("cleaned_data.csv", index=False)

# --------------------------------------------
# 7️⃣ Print confirmation
# --------------------------------------------
print("\n✅ Duplicates removed successfully!")
print("\nData after removing duplicates:")
print(df_no_duplicates)
