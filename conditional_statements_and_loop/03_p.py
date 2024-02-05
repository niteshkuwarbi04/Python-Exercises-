'''
3. Write a Python program to guess a number between 1 and 9.
   Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until 
   guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.'''

import random

def guess_num():
    
    target_num = random.randint(1,9)

    while True:
        user_guess = int(input("Guess a number between 1 and 9: "))

        if user_guess == target_num:
            print('Well guessed !')
            break
            
        else:
            print('Try again. Wrong answer')

guess_num()