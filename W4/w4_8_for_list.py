# For Loop
# Deterministic Range: A for loop is beneficial 
# when you know in advance the number of elements that will be appended to the list.

# Readability: for loops are often more readable and self-explanatory, 
# particularly when iterating over known data structures like lists, dictionaries, or ranges.

# Example using a for loop:

import os
#mac 
os.system('clear') 
#window
#os.system('cls') 

my_list_1 = []
for i in range(5):  # Known range
    my_list_1.append(i)

print (my_list_1)

my_list_2 = []
initial_value=2
upper_limit=11
increment=1

# For loop using the range() function with initial value, upper limit, and increment

for num in range(initial_value, upper_limit, increment):
    my_list_2.append(num)

print (my_list_2)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my