#Sets are unordered collections of unique elements in Python. 
#They are often used when you need to work with a collection of 
#items where duplicates are not allowed, 
#or when you need to perform set operations like union and intersection.

import os
#mac
os.system('clear') 
#window
#os.system('cls') 

# Create a set
fruits = {"apple", "banana", "cherry", "date"}

# Add an element to the set
fruits.add("grape")

# Remove an element from the set
fruits.remove("cherry")

# Check if an element is in the set
contains_banana = "banana" in fruits
contains_orange = "orange" in fruits

# Iterate through the set
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Create another set
citrus_fruits = {"orange", "lemon", "lime"}

# Perform set operations
union_fruits_citrus = fruits.union(citrus_fruits)
intersection_fruits_citrus = fruits.intersection(citrus_fruits)
difference_fruits_citrus = fruits.difference(citrus_fruits)

# Print the results
print("Contains 'banana'? ", contains_banana)
print("Contains 'orange'? ", contains_orange)
print("Union of fruits and citrus fruits:", union_fruits_citrus)
print("Intersection of fruits and citrus fruits:", intersection_fruits_citrus)
print("Difference between fruits and citrus fruits:", difference_fruits_citrus)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my