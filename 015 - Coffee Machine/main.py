import os
from till import Money, Till

# Constants
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# State Variables


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

current_till = Till()

# Prompt user for their order (3 types of coffee)


def process_user_input():
    action = input("What would you like? (espresso/latte/cappucino): ").lower()

    if action == "off":
        print("Switching off...")
        quit()
    elif action == "report":
        print_report()
        return
    elif action in MENU.keys():
        drink = MENU[action]

        # Check if resources are sufficient

        # Ask for coins
        coins = receive_coins()
        if coins.get_total_value() < drink["cost"]:
            print("Not enough money.")
        return
    else:
        print(f"Sorry, we don't serve {action}.")


def print_report():
    global resources, current_till
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${(current_till.get_total_value())}")


def receive_coins():
    q = sanitise_coin_input(input("How many quarters?: "))
    d = sanitise_coin_input(input("How many dimes?: "))
    n = sanitise_coin_input(input("How many nickels?: "))
    p = sanitise_coin_input(input("How many pennies?: "))

    return Till([q, d, n, p])


def sanitise_coin_input(x):
    if x and x.isdigit():
        return int(x)
    else:
        return 0


while True:
    process_user_input()

# 4. Check if machine has enough resources before producing coffee
# 5. Process coins given by user
# 6. Check if transaction is successful ie. user has given enough money
# 7. Make coffee - use up resources and output the chosen coffee
