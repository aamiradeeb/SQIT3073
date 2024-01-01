import os

# Get the current directory where the Python file is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create folders and subfolders
main_folder = os.path.join(current_directory, 'main_folder_xlsx')
os.makedirs(main_folder, exist_ok=True)

import pandas as pd 

# Create a sample DataFrame
df = pd.DataFrame({
    'Student_ID': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 21, 22, 23, 24],
    'Grade': [90, 85, 77, 95, 88],
    'Subject': ['Math', 'Science', 'Math', 'History', 'Science']
})

# Create an Excel writer object
with pd.ExcelWriter(os.path.join(main_folder,'example_dataset.xlsx')) as writer:

    # Save original DataFrame to Excel
    df.to_excel(writer, sheet_name='Original_Data', index=False)

    # 1. Filtering
    filtered_df = df[df['Grade'] > 85]
    filtered_df.to_excel(writer, sheet_name='Filtered_Data', index=False)

    # 2. Sorting
    sorted_df = df.sort_values('Age')
    sorted_df.to_excel(writer, sheet_name='Sorted_Data', index=False)

    # 3. Aggregation
    average_grade = pd.DataFrame({'Average Grade': [df['Grade'].mean()]})
    average_grade.to_excel(writer, sheet_name='Aggregated_Data', index=False)

    # 4. Adding Columns
    df['Status'] = ['Pass' if grade >= 80 else 'Fail' for grade in df['Grade']]
    df.to_excel(writer, sheet_name='Added_Column_Data', index=False)

    # 5. Dropping Columns
    df_dropped = df.drop(columns=['Age'])
    df_dropped.to_excel(writer, sheet_name='Dropped_Column_Data', index=False)

    # 6. Renaming Columns
    df_renamed = df.rename(columns={'Grade': 'Score'})
    df_renamed.to_excel(writer, sheet_name='Renamed_Column_Data', index=False)

    # 7. Replacing Values
    df_replaced = df.replace({'Status': {'Pass': 'P', 'Fail': 'F'}})
    df_replaced.to_excel(writer, sheet_name='Replaced_Values_Data', index=False)

    # 8. Grouping and Aggregation
    grouped_df = df.groupby('Subject')['Grade'].mean().reset_index()
    grouped_df.to_excel(writer, sheet_name='Grouped_Data', index=False)

    # 9. Merging DataFrames
    df2 = pd.DataFrame({
        'Student_ID': [1001, 1002, 1006],
        'Attendance': [95, 90, 88]
    })
    merged_df = pd.merge(df, df2, on='Student_ID', how='left')
    merged_df.to_excel(writer, sheet_name='Merged_Data', index=False)

    # 10. Pivoting DataFrames
    pivot_df = df.pivot_table(index='Name', columns='Subject', values='Grade', aggfunc='mean')
    pivot_df.to_excel(writer, sheet_name='Pivoted_Data')

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my