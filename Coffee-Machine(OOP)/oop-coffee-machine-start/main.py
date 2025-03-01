from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
#menu_item = MenuItem
money_machine = MoneyMachine()


def coffe_making():
    while True:
        options = menu.get_items()
        choice = input(f'What would you like to have?{options}: ').lower()
        if choice == 'off':
            print('Thank you! Come again.')
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        elif choice == 'latte' or choice == 'espresso' or choice == 'cappuccino':
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print('Please type in correctly.')


coffe_making()
