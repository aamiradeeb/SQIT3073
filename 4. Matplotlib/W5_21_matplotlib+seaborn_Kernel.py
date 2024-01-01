import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Simulated customer ratings for a product (scale of 1 to 5)
ratings = np.random.randint(1, 6, 100)

plt.figure(figsize=(10, 6))
sns.kdeplot(ratings, color='purple', linestyle='--', linewidth=2, label='Ratings')
plt.xlabel('Customer Ratings')
plt.ylabel('Density')
plt.title('Distribution of Customer Ratings for a Product')
plt.legend()
plt.grid(True)
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my