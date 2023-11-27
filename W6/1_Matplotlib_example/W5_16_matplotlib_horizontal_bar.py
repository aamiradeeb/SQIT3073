import matplotlib.pyplot as plt
import numpy as np

# Number of employees in different departments of a company
departments = ['HR', 'Sales', 'Engineering', 'Marketing']
employees = [50, 200, 300, 100]

plt.figure(figsize=(10, 6))
plt.barh(departments, employees, color=['purple', 'orange', 'cyan', 'magenta'], edgecolor='black', linewidth=1.2, )
plt.xlabel('Number of Employees')
plt.ylabel('Departments')
plt.title('Number of Employees in Different Departments')
plt.legend()
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my