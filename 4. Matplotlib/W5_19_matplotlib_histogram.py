import matplotlib.pyplot as plt
import numpy as np

# Simulated age data from a survey of 100 respondents
ages = np.random.randint(18, 65, 100)

plt.figure(figsize=(10, 6))
plt.hist(ages, bins=10, color='c', edgecolor='black', alpha=0.7, label='Age Distribution')

#bins=10: Divides the data into 10 bins.
#color='c': Sets the color of the histogram bars to cyan.
#edgecolor='black': Sets the edge color to black.
#alpha=0.7: Sets the transparency level to 0.7.
#label='Age Distribution': Adds a label for the legend.
#grid=True: Adds a grid to the plot.

plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution in a Survey')
plt.legend()
plt.grid(True)
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my