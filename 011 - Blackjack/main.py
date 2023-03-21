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
from enum import Enum


class GameState(Enum):
    WIN = 0
    LOSE = 1
    DRAW = 2


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card():
    return random.choice(cards)


def get_score(hand):
    return sum(hand)


def add_cards_to_hand(hand, num=1):
    for _ in range(num):
        hand.append(get_card())


def is_blackjack(hand):
    return get_score(hand) == 21


def get_formatted_hand(hand):
    return f"[{', '.join(map(str, hand))}]"


def print_scores(player_hand, computer_hand):
    print(
        f"Your cards: {get_formatted_hand(player_hand)}, final score: {get_score(player_hand)}")
    print(
        f"Computer's first card: {str(computer_hand[0])}")


def print_final_scores(player_hand, computer_hand):
    print(
        f"Your cards: {get_formatted_hand(player_hand)}, final score: {get_score(player_hand)}")
    print(
        f"Computer's cards: {get_formatted_hand(computer_hand)}, final score: {get_score(computer_hand)}")


def handle_end(player_hand, computer_hand, state):
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
    user_action = input("Type 'y' to start another game, or 'n' to end.")
    if user_action == 'y':
        blackjack()
    else:
        print("Thanks for playing!")
        quit()


def blackjack():
    player_hand = []
    computer_hand = []

    # Deal 2 cards to each player
    add_cards_to_hand(player_hand, 2)
    add_cards_to_hand(computer_hand, 2)

    if is_blackjack(player_hand):
        if is_blackjack(computer_hand):
            handle_end(player_hand, computer_hand, GameState.DRAW)
        else:
            handle_end(player_hand, computer_hand, GameState.WIN)
    elif is_blackjack(computer_hand):
        handle_end(player_hand, computer_hand, GameState.LOSE)

    # Continue
    print_scores(player_hand, computer_hand)
    player_card = input("Want another card?: ")


# Program Start
blackjack()
