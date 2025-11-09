import matplotlib.pyplot as plt
import pandas as pd



months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [200, 250, 300, 400]
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales (Time Series)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
