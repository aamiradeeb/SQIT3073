import os

try:
    # Attempt to clear the screen for macOS
    os.system('clear')
except:
    try:
        # Attempt to clear the screen for Windows if the first try fails
        os.system('cls')
    except:
        # Output an error message if both attempts fail
        print("Unable to clear the screen.")

import pandas as pd

# Initialize an empty list to store data
data_int_id = []

# Generate student names and IDs in a loop
for i in range(1, 6):  # Assuming we have 5 students
    student_name = f"Student_{i}"
    student_id = 1000 + i
    data_int_id.append([student_id, student_name])

# Create a DataFrame using the list
df_int_id = pd.DataFrame(data_int_id, columns=['Student_ID', 'Student_Name'])

# Display the DataFrame
print("DataFrame using Integer IDs:")
print(df_int_id)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my