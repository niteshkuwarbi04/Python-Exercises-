''' 
14. Write a Python program that accepts a string and calculates the number of digits and letters.'''

data = input('Enter any word containing digits and letters : ')

d=l=0

for i in data:
    if i.isdigit():
        d = d+1
    elif i.isalpha():
        l = l+1
    else:
        pass

print(f'Digits : {d}')
print(f'Alphabets : {l}')
