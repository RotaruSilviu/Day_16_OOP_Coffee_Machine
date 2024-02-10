from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# E bine sa le salvam in "object" sau variabile  pentru ca e mult mai usor de scris codul ulterior.
barista = CoffeeMaker()
menu = Menu()
coins = MoneyMachine()

#coffee = MenuItem("coffee",50, 20, 45, 2.8)

machine_functions = True
while machine_functions:
    user_input = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_input == "off":
        machine_functions = False
    elif user_input == "report":
        # Aici am chemat amandoua rapoarte ca sa ne dea raportul.
        barista.report()
        coins.report()
    else:
        # Asa ajungem la numele bauturii din programul nostru, nu mai e suficient ca sa introducem mereu variabila de la
        #user imput, trebuie sa o cautam in bucata de cod din librarie.
        drink = menu.find_drink(user_input)
        # !!!!! IMPORTANT.  Ca sa ajungi la ATRIBUTELE unei clase trebuie sa gasesti obiectul in cazul asta e "drink",
        # si sa scrii dupa el ce anume cauti.
        # In cazul de fata "drink.cost" mi a luat 2 ore ca sa il deslusesc cum sa chem variabila cost!!!!
        if barista.is_resource_sufficient(drink) and coins.make_payment(drink.cost):
            barista.make_coffee(drink)



