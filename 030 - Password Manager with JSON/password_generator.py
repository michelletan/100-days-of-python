from random import choice, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(num_letters=10, num_numbers=2, num_symbols=4):
    """Generates a password string with random letters, numbers and symbols.

    Args:
        num_letters: Number of letters for the password
        num_numbers: Number of numbers in the password
        num_symbols: Number of symbols in the password

    Returns:
        A string representing a password with given number of letters, numbers and symbols."""

    random_letters = [choice(letters) for _ in range(num_letters)]
    random_numbers = [choice(numbers) for _ in range(num_numbers)]
    random_symbols = [choice(symbols) for _ in range(num_symbols)]

    password = random_letters + random_numbers + random_symbols
    shuffle(password)
    return ''.join(password)
