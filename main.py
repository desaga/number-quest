import random

from art import logo
from utils import clear_terminal

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 10

def choose_difficulty():
    '''Based on user input returns number of attempts'''
    choice = input("Choose a difficulty. Type 1 for easy or 2 for hard: > ")
    if choice == "1":
        attempts = EASY_LEVEL_ATTEMPTS
    elif choice == "2":
        attempts = HARD_LEVEL_ATTEMPTS
    else:
        attempts = 0
    return attempts

def play_game():
    '''Do-While loop for game until user hit "n"'''
    # Choose a difficulty until a player type a correct value
    attempts = 0
    while True:
        attempts = choose_difficulty()
        if attempts > 0:
            break
    target_number = random.choice(range(100))

    for attempt in range(attempts):
        print(f"You have {attempts - attempt} attempts remaining to guess the number")
        guess = int(input("Make a guess: > "))
        if guess == target_number:
            print("You win!")
            break
        elif guess > target_number:
            print("Too high, try again.")
        else:
            print("To low, try again.")

# The Game logic is here
while True:
    clear_terminal()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    play_game()
    if input("Do you want to continue? type 'y' or 'n' > ") != "y":
        break
