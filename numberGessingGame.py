# 1. Number Guessing Game
# ------------------------
# This game generates a random number between 1 and 100 and asks the user to guess it.
# It gives feedback whether the guess is too high or too low until the user gets it right.
import random
def number_guessing_game():
     number =random.randint(1,100)  # Generate random number
     guess = None
     while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
           print('Too low!')
        elif guess > number:
           print('Too high!')    
        else:
            print("Correct! The number was", number)   
number_guessing_game()            