from game_data import data
import art
import random
import os

NUM_CHOICES = len(data)


def get_one_choice(state):
    """Picks a random index from state and removes the chosen index.
    Returns the element at the corresponding index from data list."""
    index = random.choice(state)
    state.remove(index)
    return data[index]


def print_header():
    os.system("clear")
    print(art.logo)
    print("------------------")


def prompt_replay():
    play_again = input("Play again? Type 'y' for yes, 'n' for no: ")
    if play_again == 'y':
        new_game()
    else:
        print("Thanks for playing!")
        quit()


def new_game():
    print_header()

    # State remembers the choices that have not been shown yet. This ensures that we
    # do not show duplicate or same choices. Eg: A vs A
    state = [x for x in range(NUM_CHOICES)]
    score = 0
    print(f"Current score: {score}")
    a = get_one_choice(state)

    while state:
        b = get_one_choice(state)

        # Get the correct answer
        answer = "a" if a["follower_count"] > b["follower_count"] else "b"

        print_header()
        print(f"Your current score is: {score}")

        # Prompt user to select a choice
        print(
            f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
        print(art.vs)
        print(
            f"Against B: {b['name']}, {b['description']}, from {b['country']}")
        player_choice = input("Who has more followers? Type 'A' or 'B': ")

        if player_choice.lower() == answer:
            score += 1
            # Save the correct answer as choice A for the next round
            if answer == "b":
                a = b
        else:
            # Game Over
            print_header()
            print(f"Oops, that wasn't correct. Your final score is {score}.")
            prompt_replay()

    # No more choices left, player wins
    print("You've won the game!")
    prompt_replay()


# Program Start
new_game()
