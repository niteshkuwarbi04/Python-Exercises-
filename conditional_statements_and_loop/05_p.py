'''
5. Write a Python program that accepts a word from the user and reverses it.'''

user_input = input('Enter any word: ')

reversed_word = user_input[::-1]

print(f'The reversed word is : {reversed_word}')

if user_input == reversed_word:
    print('The word is palindrome.')
else:
    print('The word is not palindrome')
    