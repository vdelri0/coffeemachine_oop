from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while on:
    items = menu.get_items()

    espresso = menu.find_drink(items[0]).cost
    latte = menu.find_drink(items[1]).cost
    cappuccino = menu.find_drink(items[2]).cost

    choice = input(f"​What would you like? (espresso ${espresso}/latte ${latte}/cappuccino ${cappuccino}): ").lower()

    if choice == 'off':
        on = False
        print("I'm gonna turn off, bye bye!")
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice in ('espresso', 'latte', 'cappuccino'):
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Please select a valid option.")