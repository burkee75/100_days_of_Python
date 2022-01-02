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

def sales_register(menu_item):

    # TODO: return specific coin amounts. Ex. 3 quarters, 1 nickle in change.

    item_cost = float(MENU[menu_item]['cost'])

    # for debugging...
    print(f"The ordered item is a '{menu_item}' and it costs ${item_cost}")

    customer_payment_amount = float(input("Enter payment:\n"))
    # TODO: add exception checking for string input. 
    
    if item_cost > customer_payment_amount:
        "Insufficent Funds. Exiting..."
        sys.exit()
    else:
        customer_change_amount = "{:.2f}".format(customer_payment_amount - item_cost)
        print(f"Your change is: ${customer_change_amount}\n")
        return customer_change_amount

def menu_selection():
    customer_order = str.lower(input('What would you like? (espresso/latte/cappuccino) '))
    # check that the order is an item from the list MENU. If not and also not a special command return error.
    if customer_order in MENU.keys():
        sales_register(customer_order)

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