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

# Create a sample DataFrame
df = pd.DataFrame({
    'Student_ID': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 21, 22, 23, 24],
    'Grade': [90, 85, 77, 95, 88]
})

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# 1. Filtering: Filter students with Grade above 85
filtered_df = df[df['Grade'] > 85]
print("\nFiltered DataFrame (Grade > 85):")
print(filtered_df)

# 2. Sorting: Sort students by Age in ascending order
sorted_df = df.sort_values('Age')
print("\nSorted DataFrame (by Age):")
print(sorted_df)

# 3. Aggregation: Calculate the average Grade
average_grade = df['Grade'].mean()
print(f"\nAverage Grade: {average_grade}")

# 4. Adding a Column: Add a column to indicate pass/fail based on Grade
df['Status'] = ['Pass' if grade >= 80 else 'Fail' for grade in df['Grade']]
print("\nDataFrame with Status Column:")
print(df)

# 5. Dropping a Column: Remove the Age column
df_dropped = df.drop(columns=['Age'])
print("\nDataFrame after Dropping Age Column:")
print(df_dropped)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my