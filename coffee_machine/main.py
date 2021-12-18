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

def menu_selection():
    customer_order = str.lower(input('What would you like? (espresso/latte/cappuccino) '))
    for key in MENU:
        if customer_order == 'off':
            print('Powering Down...')
            sys.exit()

        elif customer_order == 'report':
            print("REPORT\n-----")
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
            sys.exit()

        elif customer_order not in key:
            print('Invalid Selection, please try again.')
            menu_selection()
    
        else:
            return customer_order

if __name__ == '__main__':
    
    # initialize money in the till

    print('☕️ Welcome to the Coffee Pot!')
    order = menu_selection()
    print(f'You ordered a {order}')