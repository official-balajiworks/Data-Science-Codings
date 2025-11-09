import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame({
    'Height': [160,165,170,175,180],
    'Weight': [55,60,65,70,75],
    'Age': [18,19,20,21,22],
    'Score': [80,85,90,95,100]
})
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (Many Variables)")
plt.show()
