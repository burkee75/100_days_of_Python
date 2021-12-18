import sys

# Menu provided by instructor
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

def menu_selection():
    customer_order = input("What would you like? (espresso/latte/cappuccino) ")
    coffee_types = {"espresso", "latte", "cappuccino"}
    if customer_order == "off":
        print("Powering Down...")
        sys.exit()

    elif customer_order not in coffee_types:
        print("Invalid Selection, please try again.")
        menu_selection()
    
    else:
        return customer_order

if __name__ == "__main__":
    print("☕️ Welcome to the Coffee Pot!")
    order = menu_selection()
    print(f"You ordered a {order}")