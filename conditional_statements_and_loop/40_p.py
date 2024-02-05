'''
40. Write a Python program to find the median of three values.'''

def find_median(num1, num2, num3):
    numbers = [num1, num2, num3]

    numbers.sort()

    median = numbers[1]

    return median

num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))

median = find_median(num1, num2, num3)
print(f"The median is {median}.")
