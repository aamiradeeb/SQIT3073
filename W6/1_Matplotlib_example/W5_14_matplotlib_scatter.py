import matplotlib.pyplot as plt
import numpy as np

# Simulated SAT scores and high school GPAs for 50 students
sat_scores = np.random.randint(1300, 1600, 50)
gpa_scores = np.random.uniform(3.0, 4.0, 50)

plt.figure(figsize=(10, 6))
plt.scatter(sat_scores, gpa_scores, color='g', marker='s', s=40, label='Students')
plt.xlabel('SAT Scores')
plt.ylabel('High School GPA')
plt.title('SAT Scores vs. High School GPA')
plt.legend()
plt.grid(True)
plt.show()

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my