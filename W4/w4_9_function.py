
import os
#mac 
os.system('clear') 
#window
#os.system('cls') 

# Function to perform the calculation
def calculate(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            return "Cannot divide by zero"
        else:
            return x / y
    else:
        return "Invalid Operation"

# Display welcome message
print("Welcome to the Simple Calculator Program")

# Main loop
while True:
    # Input: Ask for the first operand (x)
    x = float(input("Please enter the first operand (x): "))
    
    # Input: Ask for operation (op)
    op = input("Please enter the operation (either +, -, *, /): ")
    
    # Input: Ask for the second operand (y)
    y = float(input("Please enter the second operand (y): "))
    
    # Call Function: calculate(x, y, op)
    result = calculate(x, y, op)
    
    # Output: Display the result
    print(f"The result is: {result}")
    
    # Input: Ask if the user wants to continue
    continue_calculation = input("Would you like to perform another calculation? (Y/N): ")
    if continue_calculation.lower() != 'Y':
        break

# Display exit message
print("Thank you for using the Simple Calculator Program. Goodbye!")

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my