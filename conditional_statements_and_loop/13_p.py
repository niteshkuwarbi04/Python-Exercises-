'''
13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program 
    will print the numbers that are divisible by 5 in a comma separated sequence.
'''

# Function to convert binary to decimal and check divisibility by 5
def binary_to_decimal_and_check_divisibility(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number % 5 == 0

# Take input of comma-separated binary numbers
binary_input = input("Enter comma-separated 4-digit binary numbers: ")

# Split the input into a list of binary numbers
binary_numbers = binary_input.split(',')

# Filter numbers divisible by 5 using list comprehension
divisible_by_5 = [num for num in binary_numbers if binary_to_decimal_and_check_divisibility(num.strip())]

# Print the result in a comma-separated sequence
print("Numbers divisible by 5:", ', '.join(divisible_by_5))

