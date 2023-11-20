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

# Below is a Python code snippet that demonstrates various DataFrame manipulations, including:

#1.Filtering
#2.Sorting
#3.Aggregation
#4.Adding Columns
#5.Dropping Columns
#6.Renaming Columns
#7.Replacing Values
#8.Grouping and Aggregation
#9.Merging DataFrames
#10.Pivoting DataFrames


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Student_ID': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 21, 22, 23, 24],
    'Grade': [90, 85, 77, 95, 88],
    'Subject': ['Math', 'Science', 'Math', 'History', 'Science']
})

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# 1. Filtering
filtered_df = df[df['Grade'] > 85]
print("\n1. Filtered DataFrame (Grade > 85):")
print(filtered_df)

# 2. Sorting
sorted_df = df.sort_values('Age')
print("\n2. Sorted DataFrame (by Age):")
print(sorted_df)

# 3. Aggregation
average_grade = df['Grade'].mean()
print(f"\n3. Average Grade: {average_grade}")

# 4. Adding a Column
df['Status'] = ['Pass' if grade >= 80 else 'Fail' for grade in df['Grade']]
print("\n4. DataFrame with Status Column:")
print(df)

# 5. Dropping a Column
df_dropped = df.drop(columns=['Age'])
print("\n5. DataFrame after Dropping Age Column:")
print(df_dropped)

# 6. Renaming Columns
df_renamed = df.rename(columns={'Grade': 'Score'})
print("\n6. DataFrame with Renamed Column:")
print(df_renamed)

# 7. Replacing Values
df_replaced = df.replace({'Status': {'Pass': 'P', 'Fail': 'F'}})
print("\n7. DataFrame with Replaced Values:")
print(df_replaced)

# 8. Grouping and Aggregation: Group by Subject and calculate mean Grade
grouped_df = df.groupby('Subject')['Grade'].mean()
print("\n8. Grouped DataFrame with Mean Grade:")
print(grouped_df)


# 9. Merging DataFrames
df2 = pd.DataFrame({
    'Student_ID': [1001, 1002, 1006],
    'Attendance': [95, 90, 88]
})
merged_df = pd.merge(df, df2, on='Student_ID', how='left')
print("\n9. Merged DataFrame:")
print(merged_df)

# 10. Pivoting DataFrames
# Using pivot_table instead of pivot to handle duplicate entries
pivot_df = df.pivot_table(index='Name', columns='Subject', values='Grade', aggfunc='mean')
print("\n10. Pivoted DataFrame:")
print(pivot_df)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my