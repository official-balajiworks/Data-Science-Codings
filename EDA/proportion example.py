import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
labels = ['A', 'B', 'C']
sizes = [300, 200, 100]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Product Sales Proportion (Pie Chart)")
plt.show()
