from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

barista = CoffeeMaker()
menu = Menu()
coins = MoneyMachine()


machine_functions = True
while machine_functions:
    user_input = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_input == "off":
        machine_functions = False
    elif user_input == "report":
        barista.report()
        coins.report()
    else:
        drink = menu.find_drink(user_input)
        if barista.is_resource_sufficient(drink) and coins.make_payment(drink.cost):
            barista.make_coffee(drink)



