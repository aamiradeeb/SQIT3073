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

import numpy as np  # Import the NumPy library for numerical operations

# Create 3D NumPy arrays
# Initializing 3-dimensional arrays for demonstration purposes.
arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr2 = np.array([[[12, 11, 10], [9, 8, 7]], [[6, 5, 4], [3, 2, 1]]])

# Access elements
# Accessing the first and last elements to demonstrate element retrieval.
first_element = arr1[0, 0, 0]
last_element = arr1[-1, -1, -1]

# Perform basic mathematical operations

# Summation: Calculate the sum of all elements in the array.
sum_elements = np.sum(arr1)

# Mean: Compute the mean value of the array elements.
mean_elements = np.mean(arr1)

# Product: Calculate the product of all elements in the array.
product_elements = np.prod(arr1)

# Minimum: Find the smallest element in the array.
min_element = np.min(arr1)

# Maximum: Find the largest element in the array.
max_element = np.max(arr1)

# Standard Deviation: Compute the standard deviation of the array elements.
std_dev = np.std(arr1)

# Variance: Calculate the variance of the array elements.
variance = np.var(arr1)

# Element-wise Addition: Add corresponding elements of arr1 and arr2.
elementwise_add = np.add(arr1, arr2)

# Element-wise Subtraction: Subtract corresponding elements of arr1 and arr2.
elementwise_sub = np.subtract(arr1, arr2)

# Element-wise Multiplication: Multiply corresponding elements of arr1 and arr2.
elementwise_mul = np.multiply(arr1, arr2)

# Element-wise Division: Divide corresponding elements of arr1 and arr2.
elementwise_div = np.divide(arr1, arr2)

# Trigonometric Operations: Calculate the sine of each element in arr1.
sine_values = np.sin(arr1)

# Logarithmic Operations: Calculate the natural logarithm of each element in arr1.
log_values = np.log(arr1)

# Display results
# Outputting the results to the console.
print(f"Original array 1:\n{arr1}")
print(f"Original array 2:\n{arr2}")
print(f"First element: {first_element}")
print(f"Last element: {last_element}")
print(f"Sum of elements: {sum_elements}")
print(f"Mean of elements: {mean_elements}")
print(f"Product of elements: {product_elements}")
print(f"Minimum element: {min_element}")
print(f"Maximum element: {max_element}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
print(f"Element-wise Addition:\n{elementwise_add}")
print(f"Element-wise Subtraction:\n{elementwise_sub}")
print(f"Element-wise Multiplication:\n{elementwise_mul}")
print(f"Element-wise Division:\n{elementwise_div}")
print(f"Sine values:\n{sine_values}")
print(f"Natural Logarithm values:\n{log_values}")

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my