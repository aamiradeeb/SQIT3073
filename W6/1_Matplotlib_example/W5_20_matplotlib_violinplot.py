import matplotlib.pyplot as plt
import numpy as np

# Simulated salary data for a company's employees (in thousand USD)
salaries = np.random.normal(70, 15, 100)

plt.figure(figsize=(10, 6))
plt.violinplot(salaries, showmedians=True)
plt.xlabel('Company')
plt.ylabel('Salary (Thousand USD)')
plt.title('Distribution of Salaries in a Company')
plt.grid(True)
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my