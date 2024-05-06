# Define a string variable
message = "This is an apple."

# Print the string
print(message)

# Access individual characters in the string
first_character = message[0]
print("The first character is:", first_character)

# Find the length of the string
length = len(message)
print("The length of the string is:", length)



#
# Get user input for the name
name = input("Enter your name: ")
#
#



# Concatenate (combine) two strings
greeting = "Hello, " + name + "!"
print(greeting)

# Use string methods
uppercase_message = greeting.upper()
print("Uppercase message:", uppercase_message)

# Check if a substring is in the string
contains_TZYY = "TZYY" in greeting
print("Does the message contain 'TZYY'? ", contains_TZYY)

# Replace part of the string
new_message = message.replace("TZYY", "World")
print("Updated message:", new_message)
