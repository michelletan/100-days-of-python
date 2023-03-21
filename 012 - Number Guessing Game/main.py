import os
import random
from art import logo

NUM_TURNS_EASY = 10
NUM_TURNS_HARD = 5


def new_game():
    os.system('clear')
    print(logo)
    difficulty = input(
        "Welcome to Guess a Number! Please choose your difficulty. Type 'e' for easy or 'h' for hard. \n >> ")

    if difficulty == "e":
        num_guesses = NUM_TURNS_EASY
    elif difficulty == "h":
        num_guesses = NUM_TURNS_HARD
    else:
        print("Please select a difficulty by typing 'e' or 'h'.")
        new_game()

    print("The computer has chosen a number between 1 - 100. ")
    number = random.randint(1, 100)

    while num_guesses > 0:
        guess = int(input(
            "Enter your guess here: \n >> "))

        if guess == number:
            print(f"Congrats! You've won! The correct number is {number}.")
            return
        elif guess > number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")
        num_guesses -= 1
        print(f"You have {num_guesses} guesses remaining.")
    print("Game over! You ran out of guesses.")


new_game()
