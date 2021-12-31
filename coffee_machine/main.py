import sys

# Menu provided by instructor
MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

# project did not include any information about the money the machine has at the start so I am creating these values.
vending_cash = {
    'quarters': 20,
    'dimes': 20,
    'nickles': 20,
    'pennies': 100
}

def ingredients_available(menu_item):
    """Accepts a dictionary of ingedients and checks if the machine has enough to make the drink"""
    for item in MENU[menu_item]['ingredients']:
        if resources[item] <= MENU[menu_item]['ingredients'][item]:
            print(f"There is not enough {item} to make your order.")
            return False
        return True

def menu_selection():
    customer_order = str.lower(input('What would you like? (espresso/latte/cappuccino) '))
    # check that the order is an item from the list MENU. If not and also not a special command return error.
    if customer_order in MENU.keys():
        if ingredients_available(customer_order):
            menu_item_cost = "{:.2f}".format(MENU[customer_order]['cost'])
            print(f"The cost for {customer_order} is ${menu_item_cost}")
        else:
            sys.exit()

    elif customer_order == 'off':
        print('Powering Down...')
        sys.exit()
    elif customer_order == 'report':
        print("REPORT\n-----")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        sys.exit()
    else:
        print('Invalid Selection, please try again.')
        menu_selection()


if __name__ == '__main__':
    
    # initialize money in the till

    print('☕️ Welcome to the Coffee Pot!')
    order = menu_selection()
    # return if selection is availabel based and resources and the cost
    # next ask for payment
    # if sufficent payment, make order and update reources