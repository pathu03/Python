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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def suf(abc):
    for item in abc:
        if abc[item]>=resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True
def money():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def pymeny_succsess(orignal,drink_cost):
    if orignal >= drink_cost:
        change=round(orignal - drink_cost ,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def mack_coffee(drink_name,oder_name):
    for item in oder_name:
        resources[item]-=oder_name[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":    
        is_on=False
    elif choice=="report":
        print(f"water : {resources['water']}")
        print(f"milk : {resources['milk']}")
        print(f"coffee : {resources['coffee']}")
        print(f"profit : {profit}")
    else:
        drink=MENU[choice]
        if suf(drink["ingredients"]):
            pyment=money()
            if pymeny_succsess(pyment,drink["cost"]):
                mack_coffee(choice,drink["ingredients"])




