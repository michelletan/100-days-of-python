import os
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    done = False
    answer = num1
    while not done:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](answer, num2)
        print(f"{answer} {operation_symbol} {num2} = {answer}")

        user_done = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if user_done == 'n':
            done = True
            os.system("clear")
            calculator()


# Start program
calculator()
