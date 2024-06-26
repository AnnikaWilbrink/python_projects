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

profit = 0


def make_coffee(name_drink, order_ingredients):
    """
    Makes coffee if there are enough resources to make the selected drink
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {name_drink}. Enjoy!")


def check_transaction(inserted_coins, drink_name):
    """
    Checks transaction
    """
    global profit
    if inserted_coins < MENU[drink_name]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if inserted_coins > MENU[drink_name]["cost"]:
            print(f"Here is ${inserted_coins - MENU[drink_name]['cost']} in change.")
        profit += MENU[drink_name]["cost"]
        make_coffee(drink_name, MENU[drink_name]["ingredients"])


def process_coins(drink_name):
    total = 0
    print("Please insert coins.")
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    check_transaction(round(total, 2), drink_name)


def check_resources(order_ingredients):
    """
    Checks if there are enough resources to make the chosen drink.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def machine(is_on):
    """
    Handles input.
    """
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif choice in MENU:
            is_enough_resources = check_resources(MENU[choice]["ingredients"])
            if is_enough_resources:
                process_coins(choice)
        else:
            print("Sorry, that's not on the menu")


if __name__ == '__main__':
    machine(True)
