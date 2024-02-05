'''
35. Write a Python program that checks whether a string represents an integer or not.'''

def is_integer(s):
    # Check for empty string
    if not s:
        return False
    
    # Check for negative sign at the beginning
    if s[0] == '-':
        s = s[1:]

    # Check if the remaining characters are digits
    return s.isdigit()

# Get input from the user
user_input = input("Enter a string: ")

# Check if the input represents an integer
if is_integer(user_input):
    print(f"{user_input} represents an integer.")
else:
    print(f"{user_input} does not represent an integer.")
