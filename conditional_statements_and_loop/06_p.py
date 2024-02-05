''' 
6.  Write a Python program to count the number of even and odd numbers in a series of numbers
    Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)'''

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
length = len(numbers)

for i in range(0, length+1):
    if(i%2==0):
        print(i)
    else:
        pass