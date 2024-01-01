# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the list
print("Original list:", numbers)

# Access elements by index
first_element = numbers[0]
print("The first element is:", first_element)


# Slice the list to get a subset
subset = numbers[2:4]
print("Subset of the list:", subset)

# Modify an element in the list
numbers[1] = 10
print("Modified list:", numbers)



# Append an element to the end of the list
numbers.append(6)
print("List after appending 6:", numbers)

# Remove an element by value
numbers.remove(3)
print("List after removing 3:", numbers)


# Find the index of an element
index_of_4 = numbers.index(4)
print("Index of 4:", index_of_4)

# Check if an element is in the list
contains_7 = 7 in numbers
print("Does the list contain 7?", contains_7)


# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

 
# Create a list of strings
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my