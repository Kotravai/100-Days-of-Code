from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
choice = menu.get_items()

is_machine_on = True

while is_machine_on:
    order = str(input(f"What would you like to have? {choice} ")).lower()
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        is_machine_on = False
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(order)






