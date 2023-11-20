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

# Get the current directory where the Python file is located
current_directory = os.path.dirname(os.path.realpath(__file__))

# Create folders and subfolders
main_folder = os.path.join(current_directory, 'main_folder_csv')
subfolder = os.path.join(main_folder, 'subfolder')

os.makedirs(subfolder, exist_ok=True)

# Create a sample DataFrame
df = pd.DataFrame({
    'Student_ID': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 21, 22, 23, 24],
    'Grade': [90, 85, 77, 95, 88],
    'Subject': ['Math', 'Science', 'Math', 'History', 'Science']
})

# Save original DataFrame to CSV
df.to_csv(os.path.join(main_folder, 'example_dataset_1.csv'), index=False)

# Perform DataFrame manipulations and save them as CSV files in the subfolder

# 1. Filtering
filtered_df = df[df['Grade'] > 85]
filtered_df.to_csv(os.path.join(subfolder, 'filtered_dataset.csv'), index=False)

# 2. Sorting
sorted_df = df.sort_values('Age')
sorted_df.to_csv(os.path.join(subfolder, 'sorted_dataset.csv'), index=False)

# 3. Aggregation
average_grade = df['Grade'].mean()
with open(os.path.join(subfolder, 'average_grade.csv'), 'w') as f:
    f.write(f"Average Grade,{average_grade}")

# 4. Adding Columns
df['Status'] = ['Pass' if grade >= 80 else 'Fail' for grade in df['Grade']]
df.to_csv(os.path.join(subfolder, 'added_column_dataset.csv'), index=False)

# 5. Dropping Columns
df_dropped = df.drop(columns=['Age'])
df_dropped.to_csv(os.path.join(subfolder, 'dropped_column_dataset.csv'), index=False)

# 6. Renaming Columns
df_renamed = df.rename(columns={'Grade': 'Score'})
df_renamed.to_csv(os.path.join(subfolder, 'renamed_column_dataset.csv'), index=False)

# 7. Replacing Values
df_replaced = df.replace({'Status': {'Pass': 'P', 'Fail': 'F'}})
df_replaced.to_csv(os.path.join(subfolder, 'replaced_values_dataset.csv'), index=False)

# 8. Grouping and Aggregation
grouped_df = df.groupby('Subject')['Grade'].mean().reset_index()
grouped_df.to_csv(os.path.join(subfolder, 'grouped_dataset.csv'), index=False)

# 9. Merging DataFrames
df2 = pd.DataFrame({
    'Student_ID': [1001, 1002, 1006],
    'Attendance': [95, 90, 88]
})
merged_df = pd.merge(df, df2, on='Student_ID', how='left')
merged_df.to_csv(os.path.join(subfolder, 'merged_dataset.csv'), index=False)

# 10. Pivoting DataFrames
pivot_df = df.pivot_table(index='Name', columns='Subject', values='Grade', aggfunc='mean')
pivot_df.to_csv(os.path.join(subfolder, 'pivoted_dataset.csv'))

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my