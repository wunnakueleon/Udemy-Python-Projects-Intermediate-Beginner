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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_ingredients(chosen_drink):
    if chosen_drink not in MENU:
        return False

    required_water = MENU[chosen_drink]['ingredients']['water']
    required_milk = MENU[chosen_drink]['ingredients'].get('milk', 0)
    # To turn milk to zero if not present
    required_coffee = MENU[chosen_drink]['ingredients']['coffee']

    if (resources['water'] >= required_water and
            resources['milk'] >= required_milk and
            resources['coffee'] >= required_coffee):
        resources['water'] -= required_water
        resources['milk'] -= required_milk
        resources['coffee'] -= required_coffee
        return True
    else:
        return False


def check_money(user_payment, user_drink):
    global money
    if user_payment == MENU[user_drink]['cost']:
        print('Thank you for your payment.')
        money += MENU[user_drink]['cost']
        return True
    elif user_payment < MENU[user_drink]['cost']:
        required_money = float(MENU[user_drink]['cost']) - user_payment
        print(f'The payment has not been fully covered. You need ${required_money}.')
        return False
    else:
        change = user_payment - float(MENU[user_drink]['cost'])
        print(f'Here is your change: ${change}')
        money += MENU[user_drink]['cost']
        return True


money = 0
while True:
    print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}")
    user_drink = input('What would you like to have?\nCappuccino, Espresso, Latte: ').lower()
    if user_drink == 'stop':
        break
    try:
        user_drink = str(user_drink)
        print(f"It will cost {MENU[user_drink]['cost']}")

    except KeyError:
        print('Please type in correctly.')
        continue

    user_pay = input('Please enter the amount. Numbers only: $')

    try:
        user_pay = float(user_pay)
    except ValueError:
        print('Please enter a valid number.')
        continue

    if check_ingredients(user_drink) and check_money(user_pay, user_drink):
        print('')
        print(f'remaining resources: {resources}')
        print(f'{money}$ collected')
        print('')
    else:
        print('Sorry, the ingredients are not enough.')
        break
