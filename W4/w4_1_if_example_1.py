import os
#mac 
os.system('clear') 
#window
#os.system('cls') 

# Variables containing integers
a = 10
b = 20

# If-elif-else statement using the specified comparison operators
if a == b:
    print("a is equal to b.")
elif a != b:
    print("a is not equal to b.")
    
    # Further categorize the relationship between a and b
    if a < b:
        print("a is less than b.")
    elif a <= b:
        print("a is less than or equal to b.")
    elif a > b:
        print("a is greater than b.")
    elif a >= b:
        print("a is greater than or equal to b.")
else:
    print("The relationship between a and b is undefined.")

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my