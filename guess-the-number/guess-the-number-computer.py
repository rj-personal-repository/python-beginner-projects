# Computer generates a secret number for us to guess

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("sorry guess again. Too Low.")
        elif guess > random_number:
            print("sorry, guess again. Too High.")
    print(f"You guessed {random_number}! This is correct.")

guess(10)