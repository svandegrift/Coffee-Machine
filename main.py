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


def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${total_money}')


def check_resources(choice):
    have_enough_resources = True
    for ingredient in MENU[choice]['ingredients']:
        if resources[ingredient] < MENU[choice]["ingredients"][ingredient]:
            have_enough_resources = False
            print(f"Sorry, there is not enough {ingredient}")
    return have_enough_resources


def process_coins(price):
    print(f"That will be ${price}")
    quarters = int(input("Enter how many quarters: ")) * 0.25
    dimes = int(input("Enter how many dimes: ")) * 0.1
    nickels = int(input("Enter how many nickels: ")) * 0.05
    pennies = int(input("Enter how many pennies: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    if price > total:
        print("That is not enough funds, purchase voided")
        return False, 0
    change = round(total - price, 2)
    print(f'Here is your change: ${change}')
    return True, price


def update_resources(item):
    for ingredient in item:
        resources[ingredient] -= item[ingredient]


is_coffee_machine_on = True
total_money = 0
while is_coffee_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino)")
    if user_choice == 'off':
        is_coffee_machine_on = False
        break
    elif user_choice == "report":
        print_report()
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        enough_ingredients = check_resources(user_choice)
        if enough_ingredients:
            transaction_was_successful, total_money = process_coins(MENU[user_choice]['cost'])
            if transaction_was_successful:
                update_resources(MENU[user_choice]['ingredients'])
                print(f"Here is your {user_choice}. Enjoy!")
