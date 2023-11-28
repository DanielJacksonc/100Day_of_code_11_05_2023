from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menuitem = MenuItem()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()


machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"what would you like to drink?{options} ").lower()
    if choice == "off":
        print("Your Machine if OFF.")
        machine_on = False
    elif choice == "report":
        money_report = money_machine.report()
        coffe_report = coffeemaker.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)






