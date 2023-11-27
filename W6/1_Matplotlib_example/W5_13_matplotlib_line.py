import matplotlib.pyplot as plt


# Monthly average temperatures in New York City for the year 2020 (in Fahrenheit)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
avg_temps = [32, 35, 42, 55, 65, 72, 77, 75, 68, 57, 48, 37]

plt.figure(figsize=(10, 6))

plt.plot(months, avg_temps, color='b', marker='x', linestyle='-', linewidth=2, markersize=8, label='Avg Temp')


plt.xlabel('Months')
plt.ylabel('Average Temperature (°F)')
plt.title('Monthly Average Temperature in New York City (2020)')
plt.legend()
plt.grid(True)

plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my
