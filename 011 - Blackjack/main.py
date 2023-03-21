############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
import os
from art import logo
from enum import Enum


class GameState(Enum):
    WIN = 0
    LOSE = 1
    DRAW = 2


# Ace starts with value 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card():
    return random.choice(cards)


def get_score(hand):
    return sum(hand)


def add_card_to_hand(hand):
    hand.append(get_card())
    curr_score = get_score(hand)
    if curr_score > 21 and 11 in hand:
        # If the score is over 21, check if there are aces to convert to value 1
        i = hand.index(11)
        hand[i] = 1


def is_blackjack(hand):
    return get_score(hand) == 21


def is_over(hand):
    return get_score(hand) > 21


def get_formatted_hand(hand):
    return f"[{', '.join(map(str, hand))}]"


def print_scores(player_hand, computer_hand):
    print(
        f"Your cards: {get_formatted_hand(player_hand)}, current score: {get_score(player_hand)}")
    print(
        f"Computer's first card: {str(computer_hand[0])}")


def print_final_scores(player_hand, computer_hand):
    print(
        f"Your cards: {get_formatted_hand(player_hand)}, final score: {get_score(player_hand)}")
    print(
        f"Computer's cards: {get_formatted_hand(computer_hand)}, final score: {get_score(computer_hand)}")


def handle_end(player_hand, computer_hand, state, is_blackjack=False):
    """Handles the end of the game, given the game state.
    The game state should be a GameState enum."""
    print_final_scores(player_hand=player_hand, computer_hand=computer_hand)
    match state:
        case GameState.WIN:
            print("You win!")
        case GameState.LOSE:
            print("You lose...")
        case GameState.DRAW:
            print("Draw!")
        case _:
            print("No game state given.")
    user_action = input("Type 'y' to start another game, or 'n' to end. >> ")
    if user_action == 'y':
        os.system('clear')
        blackjack()
    else:
        print("Thanks for playing!")
        quit()


def blackjack():
    player_hand = []
    computer_hand = []

    print(logo)
    print("Welcome to Blackjack! \n")

    # Deal 2 cards to each player
    add_card_to_hand(player_hand)
    add_card_to_hand(player_hand)
    add_card_to_hand(computer_hand)
    add_card_to_hand(computer_hand)

    if is_blackjack(player_hand):
        if is_blackjack(computer_hand):
            handle_end(player_hand, computer_hand, GameState.DRAW)
        else:
            handle_end(player_hand, computer_hand, GameState.WIN, True)
    elif is_blackjack(computer_hand):
        handle_end(player_hand, computer_hand, GameState.LOSE, True)

    # Player's turn
    player_done = False
    while not player_done:
        print_scores(player_hand, computer_hand)
        player_input = input(
            "Want another card? Type 'y' for another card, 'n' to end your turn: ")
        if player_input == 'y':
            add_card_to_hand(player_hand)
            if is_over(player_hand):
                handle_end(player_hand, computer_hand, GameState.LOSE)
        else:
            player_done = True

    # Computer's turn
    computer_done = False
    while not computer_done:
        if get_score(computer_hand) < 17:
            add_card_to_hand(computer_hand)
            if is_over(computer_hand):
                handle_end(player_hand, computer_hand, GameState.WIN)
        else:
            computer_done = True

    # Compare final scores
    player_score = get_score(player_hand)
    computer_score = get_score(computer_hand)
    if player_score > computer_score:
        handle_end(player_hand, computer_hand, GameState.WIN)
    elif player_score < computer_score:
        handle_end(player_hand, computer_hand, GameState.LOSE)
    else:
        handle_end(player_hand, computer_hand, GameState.DRAW)


# Program Start
blackjack()
