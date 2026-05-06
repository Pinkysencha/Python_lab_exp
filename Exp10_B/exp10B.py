import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_theme(style="whitegrid")

categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 55, 20]
time = np.arange(10)
growth = np.cumsum(np.random.randn(10))
x_rand = np.random.randn(50)
y_rand = np.random.randn(50)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# A. Line Plot
sns.lineplot(x=time, y=growth, ax=axes[0, 0], marker='o', color='b')
axes[0, 0].set_title('Line Plot: Growth Over Time')

# B. Bar Chart
sns.barplot(x=categories, y=values, ax=axes[0, 1], palette='viridis')
axes[0, 1].set_title('Bar Chart: Category Comparison')

# C. Scatter Plot
sns.scatterplot(x=x_rand, y=y_rand, ax=axes[1, 0], color='r', s=100)
axes[1, 0].set_title('Scatter Plot: Correlation Check')

# D. Histogram
sns.histplot(np.random.normal(0, 1, 1000), kde=True, ax=axes[1, 1], color='purple')
axes[1, 1].set_title('Histogram: Normal Distribution with KDE')

# Final adjustments
plt.tight_layout()
