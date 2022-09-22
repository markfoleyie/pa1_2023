"""
while-else
Simple guessing game: start with a random number and
guess with hints until:
   guess is  correct
   the guess is out of range indicating the user is quitting
All non-typed variables are integers: Rule 4
"""

import random  # get the random number module
UPPER_LIMIT = 100  # set an upper limit
number = random.randint(0, UPPER_LIMIT)  # get a random number between 0 and 100 inclusive
print("Hi-Lo Number Guessing Game: between 0 and 100 inclusive.\n")

try:
    # get an initial guess
    guess_str = input("Guess a number: ")
    guess = int(guess_str)  # convert string to number

    # while guess is range, keep asking
    while 0 <= guess <= UPPER_LIMIT:
        if guess > number:
            print(f"Guessed Too High. {guess}")
        elif guess < number:
            print(f"Guessed Too Low. {guess}")
        else:  # correct guess, exit with break
            print(f"You guessed it. The number was: {number}")
            break
        # keep going, get the next guess
        guess_str = input("Guess a number: ")
        guess = int(guess_str)
    else:
        print(f"You quit early, the number was: {number}")
    print("Finished.")
except ValueError as e:
    print(f"\n{'='*50}\nSomething bad happened!\n{e}\n{'='*50}")
    quit(1)