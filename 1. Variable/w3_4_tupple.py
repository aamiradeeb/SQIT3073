# Create a tuple
fruits = ("apple", "banana", "cherry", "date")

( "a" , 1 , 2.3 , "b"    )




# Access elements by index
first_fruit = fruits[0]
second_fruit = fruits[1]

# Iterate through the tuple
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Check if an element is in the tuple
contains_cherry = "cherry" in fruits

# Find the length of the tuple
num_fruits = len(fruits)

# Concatenate two tuples
more_fruits = ("grape", "kiwi")
all_fruits = fruits + more_fruits

# Nested tuple
nested_tuple = ("red", ("green", "blue"))

# Print the results
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Does it contain 'cherry'? ", contains_cherry)
print("Number of fruits:", num_fruits)
print("All fruits:", all_fruits)
print("Nested tuple:", nested_tuple)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my