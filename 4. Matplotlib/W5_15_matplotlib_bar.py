import matplotlib.pyplot as plt


# Quarterly revenue for a company in the year 2020 (in million USD)
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
revenue = [200, 220, 250, 275]

plt.figure(figsize=(10, 6))
plt.bar(quarters, revenue, color=['r', 'g', 'b', 'y'], edgecolor='black', linewidth=1.2)
plt.xlabel('Quarters')
plt.ylabel('Revenue (Million USD)')
plt.title('Quarterly Revenue for a Company (2020)')
plt.legend()
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my