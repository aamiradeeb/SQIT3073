import matplotlib.pyplot as plt

# Average monthly temperatures in New York City for the year 2020 with error (in Fahrenheit)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
avg_temps = [32, 35, 42, 55, 65, 72, 77, 75, 68, 57, 48, 37]
temp_error = [3, 3, 2, 2, 1, 1, 1, 1, 2, 2, 3, 3]

plt.figure(figsize=(10, 6))

plt.errorbar(months, avg_temps, yerr=temp_error, fmt='o', color='m', ecolor='g', capsize=5, label='Avg Temp')
plt.xlabel('Months')
plt.ylabel('Average Temperature (°F)')
plt.title('Average Monthly Temperature in New York City with Error (2020)')
plt.legend()
plt.grid(True)
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my