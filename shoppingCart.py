shopping_cart = {}
def shoppingCart():

    while True:
        response = input('Would you like to view list, add to list, remove from list, or quit? [show/add/remove/quit]: ')
        print(f"---------------------------")
        
        if response.lower() == 'add' or response.lower() == 'a':
            addItem()
        elif response.lower() == 'remove' or response.lower() == 'r':
            removeItem()
        elif response.lower() == 'show' or response.lower() == 's':
            printCart()
        elif response.lower() == 'quit' or response.lower() == 'q':
            printCart()
            break
        else:
            print("Please enter a valid response to the questions.\n")

def addItem():
    item = input('\nWhat would you like to add to your shopping list?: [item] ').title()
    while True:
        try:
            qty = int(input('\nHow many do you need?: [qty] '))
            break
        except:
            print("Please enter a valid integer quantity")
    
    shopping_cart[item.title()] = qty

def removeItem():
    item = input('\nWhat would you like to remove from your shopping list?: [item] ').title()
    try:
        shopping_cart.pop(item)
        print(f"{item} was removed.\n")
        print(f"------------------------\n")
    except:
        print(f"{item} is not in your shopping list.\n")
        print(f"------------------------\n")

def printCart():
    for key, value in shopping_cart.items():
        print(f"{key}: {value}")
    print(f"------------------------\n")

shoppingCart()