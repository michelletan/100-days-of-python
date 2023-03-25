from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def process_user_input():
    global menu, coffee_maker, money_machine
    user_input = input(
        f"What would you like? ({menu.get_items()}): ").lower()

    if user_input == "off":
        print("Switching off...")
        quit()
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
        return
    elif menu.find_drink(user_input):
        drink = menu.find_drink(user_input)

        if not coffee_maker.is_resource_sufficient(drink):
            # If there are not enough resources, prompt user again
            return

        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


while True:
    process_user_input()
