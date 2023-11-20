# While Loop
# Indeterministic Range: 
# If the number of elements to be appended depends on some condition that could change dynamically, 
# a while loop is more appropriate.

# Flexibility: while loops offer greater flexibility for complex conditions 
# but might sacrifice some readability.

# Example using a while loop:

import os
#mac 
os.system('clear') 
#window
#os.system('cls') 

my_list = []
i = 0

while i < 5:  # Condition could change dynamically
    my_list.append(i)
    i += 1

print (my_list)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my