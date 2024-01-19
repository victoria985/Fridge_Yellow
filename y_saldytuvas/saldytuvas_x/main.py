from fridge import Fridge
from recipe import Recipe
import json


def main():
    fridge = Fridge()
    recipe = Recipe()

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
            fridge.save()
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
            recipe.print_recipe_contents()
        else:
            print("Bad choice, try again")


if __name__ == "__main__":
    main()