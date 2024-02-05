'''Write a Python program that accepts a word from the user and reverses it and checks whether it is palindrome or not.'''

word = input('Write any word to reverse it : ')
length = len(word)
rev = ''

for char in range(length-1, -1, -1):
    rev += word[char]
print(rev)

if(rev==word):
    print("The entered word is a palindrome.")
else:
    print("The entered word is not a palindrome.") 