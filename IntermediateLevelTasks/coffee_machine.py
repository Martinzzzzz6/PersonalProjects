MENU = {
    "espresso" : {
        "ingredients": {
            "water" : 50,
            "coffee" : 18
        },
        "cost" : 1.5
    },
    "latte" : {
        "ingredients": {
            "water" : 200,
            "coffee" : 24,
            "milk" : 150
        },
        "cost" : 2.5
    },
    "cappucino" : {
        "ingredients" : {
            "water" : 250,
            "coffee" : 24,
            "milk" : 100
        },
        "cost" : 3.0
    }
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 0
}


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def check_resources(order):
    for item in MENU[order]["ingredients"]:
        if resources[item] < MENU[order]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def check_transaction(order, total):
    if total < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total >= MENU[order]["cost"]:
        chagne = round(total - MENU[order]["cost"],2)
        print(f"Here is ${chagne} in change.")
        return True
    
def make_coffee(order):
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]
    print(f"Here is your {order} ☕. Enjoy!")

def coffee_machine():
    flag = True
    while flag:
        order = input("What would you like? (espresso/latte/cappucino): ").lower()
        if order == 'off':
            flag = False
        elif order == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        elif order in MENU:
            if check_resources(order):
                total = process_coins()
                if check_transaction(order, total):
                    resources["money"] += MENU[order]["cost"]
                    make_coffee(order)
            else:
                continue
        else:
            print("Invalid choice.")
            continue

coffee_machine()