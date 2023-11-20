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
import numpy as np

# Using Lists
data_list = [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]
df_list = pd.DataFrame(data_list, columns=['ID', 'Name'])
print("DataFrame from List:")
print(df_list)

# Using Dictionaries
data_dict = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
df_dict = pd.DataFrame(data_dict)
print("\nDataFrame from Dictionary:")
print(df_dict)

# Using Series
id_series = pd.Series([1, 2, 3])
name_series = pd.Series(['Alice', 'Bob', 'Charlie'])
df_series = pd.DataFrame({'ID': id_series, 'Name': name_series})
print("\nDataFrame from Series:")
print(df_series)

# Using NumPy Arrays
data_numpy = np.array([[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']])
df_numpy = pd.DataFrame(data_numpy, columns=['ID', 'Name'])
print("\nDataFrame from NumPy Array:")
print(df_numpy)

# Using Another DataFrame
df_existing = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df_from_existing = pd.DataFrame(df_existing)
print("\nDataFrame from Another DataFrame:")
print(df_from_existing)


# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my