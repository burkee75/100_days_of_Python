import sys
from typing import ItemsView

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
        if resources[item] < MENU[menu_item]['ingredients'][item]:
            print(f"There is not enough {item} to make your order.")
            return False
        else:
            for item in MENU[menu_item]['ingredients']:
                resources[item] -= MENU[menu_item]['ingredients'][item]
                # for debugging
            print(resources)
            return True

def sales_register(menu_item):

    item_cost = float(MENU[menu_item]['cost'])

    # for debugging...
    #print(f"The ordered item is a '{menu_item}' and it costs ${item_cost}")

    # TODO: add exception checking for string input. 
    quarters_inserted = float(input("Please insert some quarters: "))
    deposited_amount = quarters_inserted * 0.25
    if deposited_amount < item_cost:
        print(f"Paid Amount: ${deposited_amount}. Total Due: ${item_cost}.")
        dimes_inserted = float(input("Please insert some dimes:"))
        deposited_amount += dimes_inserted * 0.10

        if deposited_amount < item_cost:
            print(f"Paid Amount: ${deposited_amount}. Total Due: ${item_cost}.")
            nickles_inserted = float(input("Please insert some nickles:"))
            deposited_amount += nickles_inserted * 0.05

            if deposited_amount < item_cost:
                print(f"Paid Amount: ${deposited_amount}. Total Due: ${item_cost}.")
                pennies_inserted = float(input("Please insert some pennies:"))
                deposited_amount += pennies_inserted * 0.01

                if deposited_amount < item_cost:
                    print(f"Insufficent Funds. Exiting...")
                    return False
                
                else:
                    print(f"Amount Paid: ${deposited_amount}")
            
            else:
                print(f"Amount Paid: ${deposited_amount}")
        
        else:
            print(f"Amount Paid: ${deposited_amount}")
   
    else:
        print(f"Amount Paid: ${deposited_amount}")

    if item_cost > deposited_amount:
        "Insufficent Funds. Exiting..."
        sys.exit()
    else:
        customer_change_amount = "{:.2f}".format(deposited_amount - item_cost)
        print(f"Your change is: ${customer_change_amount}\n")
        # TODO: need to add to total machine profit
        return True

def menu_selection():
    customer_order = str.lower(input('What would you like? (espresso/latte/cappuccino) '))
    # check that the order is an item from the list MENU. If not and also not a special command return error.
    if customer_order in MENU.keys():
        sales_register(customer_order)
        ingredients_available(customer_order)

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