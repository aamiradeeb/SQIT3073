import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Simulated dataset with features A, B, C, and D
data = {'A': np.random.rand(50),
        'B': np.random.rand(50),
        'C': np.random.rand(50),
        'D': np.random.rand(50)}

df = pd.DataFrame(data)

# Compute the correlation matrix
corr = df.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=.5, cbar_kws={"shrink": 0.75})
plt.title('Correlation Matrix of Features')
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my