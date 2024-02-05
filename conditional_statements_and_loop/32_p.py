'''
32. Write a Python program to check whether an alphabet is a vowel or consonant.'''

alpha = input('Enter any alphabet: ')

if alpha in ('a', 'e', 'i', 'o', 'u'):
    print(f'{alpha} is a vowel.')
else:
    print(f'{alpha} is a consonant.') 