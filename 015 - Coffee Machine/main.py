from enum import Enum

# Constants


class Money(Enum):
    QUARTER = 0
    DIME = 1
    NICKEL = 2
    PENNY = 3


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

current_money = 0

# Prompt user for their order (3 types of coffee)


def process_user_input():
    global current_money
    action = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if action == "off":
        print("Switching off...")
        quit()
    elif action == "report":
        print_report()
        return
    elif action in MENU.keys():
        drink_name = action
        drink = MENU[action]

        if not is_resources_enough(drink):
            # If there are not enough resources, prompt user again
            return

        # Ask for coins
        print(f"Please insert {format_money_string(drink['cost'])} in coins.")
        received_money = receive_coins()
        if received_money < drink["cost"]:
            print(
                f"Sorry, that's not enough. Refunding {format_money_string(received_money)}...")
            return
        else:
            if received_money > drink["cost"]:
                refund = round(received_money - drink['cost'], 2)
                print(
                    f"Returning {format_money_string(refund)} in change...")
            current_money += drink["cost"]

        # Make the drink
        make_drink(drink)
        print(f"Here's your {drink_name}, enjoy!")
    else:
        print(f"Sorry, we don't serve {action}.")


def print_report():
    global resources, current_money
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {format_money_string(current_money)}")


def is_resources_enough(drink):
    global resources
    recipe = drink["ingredients"]
    for k in recipe.keys():
        if resources[k] < recipe[k]:
            print(f"Sorry, there is not enough {k}.")
            return False
    return True


def receive_coins():
    q = sanitise_coin_input(input("How many quarters?: "))
    d = sanitise_coin_input(input("How many dimes?: "))
    n = sanitise_coin_input(input("How many nickels?: "))
    p = sanitise_coin_input(input("How many pennies?: "))

    return get_total_value({
        Money.QUARTER: q,
        Money.DIME: d,
        Money.NICKEL: n,
        Money.PENNY: p
    })


def sanitise_coin_input(x):
    if x and x.isdigit():
        return int(x)
    else:
        return 0


def format_money_string(x):
    """Converts number to string with 2 decimal places and adds $"""
    return "${:.2f}".format(x)


def get_total_value(coins):
    q = coins[Money.QUARTER] * 0.25
    d = coins[Money.DIME] * 0.1
    n = coins[Money.NICKEL] * 0.05
    p = coins[Money.PENNY] * 0.01
    return q + d + n + p


def make_drink(drink):
    global resources
    recipe = drink["ingredients"]
    for k in recipe.keys():
        resources[k] -= recipe[k]


while True:
    process_user_input()
