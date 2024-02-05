'''
34. Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.'''

num1 = int(input('Enter the first value: '))
num2 = int(input('Enter the second value: '))

sum = num1+num2

if sum in range(15, 21):
    sum = 20
    print(f'The sum if {num1} and {num2} is {sum}')
else:
    print(f'The sum of {num1} and {num2} is {sum}')