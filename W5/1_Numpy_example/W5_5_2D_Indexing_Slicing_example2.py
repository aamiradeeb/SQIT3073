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


# Import the NumPy library
import numpy as np

# Initialize a 2D array for demonstration
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Basic Indexing: Access a single element
# Fetch the element in the first row and third column (value is 3)
element = array_2d[0, 2]

# Slicing: Extract a subset of the array
# Extract a 2x2 array consisting of elements from rows 0-1 and columns 1-2
subset = array_2d[0:2, 1:3]

# Boolean Indexing: Select elements based on conditions
# Return an array of elements greater than 4
result = array_2d[array_2d > 4]

# Fancy Indexing: Select rows or columns out of order
# Select the third and first rows, maintaining their original columns
fancy_result = array_2d[[2, 0], :]

# Combined Indexing: Combine different types of indexing
# Select rows 1 to the end and only columns 0 and 2
combined_result = array_2d[1:, [0, 2]]

# Display the results
print("Original Array:")
print(array_2d)
print("Element (Basic Indexing):", element)
print("Subset (Slicing):")
print(subset)
print("Result (Boolean Indexing):", result)
print("Fancy Result (Fancy Indexing):")
print(fancy_result)
print("Combined Result (Combined Indexing):")
print(combined_result)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my