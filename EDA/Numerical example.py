import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = np.random.normal(70, 10, 100)
sns.histplot(data, kde=True)
plt.title("Distribution of Marks (Numerical Data)")
plt.show()
