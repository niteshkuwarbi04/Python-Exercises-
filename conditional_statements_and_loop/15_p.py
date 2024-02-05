'''
15. Write a Python program to check the validity of passwords input by users.
    Validation :

    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
'''
import re

def is_valid_password(password):
    # Check if the password length is between 6 and 16 characters
    if 6 <= len(password) <= 16:
        # Check if there is at least 1 lowercase letter, 1 uppercase letter, and 1 digit
        if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password):
            # Check if there is at least 1 character from [$#@]
            if re.search("[$#@]", password):
                return True
    return False

user_password = input("Enter a password: ")

if is_valid_password(user_password):
    print("Valid password!")
else:
    print("Invalid password. Please follow the specified criteria.")

