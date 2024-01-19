import os
import pickle
from fridge_ok import Fridge
from fridge_ok import Recipe


FRIDGE_FILE = "fridge.pkl"


def load_fridge(FRIDGE_FILE=FRIDGE_FILE):
    if os.path.exists(FRIDGE_FILE):
        with open(FRIDGE_FILE, 'rb') as file:
            return pickle.load(file)
    else:
        return Fridge()
    
def save_fridge(fridge, FRIDGE_FILE=FRIDGE_FILE):
    with open(FRIDGE_FILE, 'wb') as file:
        pickle.dump(fridge, file)

def main():
    fridge = Fridge()
    recipe = Recipe()
    fridge = load_fridge()
    while True:
        print('---Fridge world---')
        print('0: exit')
        print('1: Add product')
        print('2: Remove product')
        print('3: Print fridge contents')
        print('4: Check recipe')
        print('5: Add ingredients to recipe')
        print('6: Print recipe ingredients')
        choice = input('Choice 0-6: ')
        if choice == "0":
            break
        elif choice == "1":
            name = input('Product name: ')
            quantity = float(input('Product quantity: '))
            fridge.add_product(name, quantity)
        elif choice == "2": 
            name = input('Product name: ')
            quantity = float(input('Product quantity: '))
            fridge.remove_product(name, quantity) 
        elif choice == '3':
            fridge.print_contents()
        elif choice == '4':
            fridge.check_recipe(recipe)
        elif choice == '5':
            name = input("Product name: ")
            quantity = float(input("Product quantity: "))
            recipe.add_ingredient(name, quantity)
        elif choice == "6":  
            recipe.print_recipe_contens()
        else:    
            print("Bad choice, try again") 

fridge = Fridge()
fridge.add_product('milk', 1)
fridge.add_product('mayonnaise', 2)
fridge.add_product('egg', 15)
fridge.add_product('cheese', 3)

recipe = Recipe()
recipe.add_ingredient('mayonnaise', 1)
recipe.add_ingredient('cheese', 1)
recipe.add_ingredient('egg', 5)

main()      