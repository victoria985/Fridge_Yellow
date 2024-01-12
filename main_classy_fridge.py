import os
import json
from class_product import Product
from class_recipe import Recipe
from class_smart_fridge import SmartFridge
    
# Main function of starting the fridge
def start():
    fridge = SmartFridge()
    if os.path.isfile('user_data.txt'):
        print("User data file already exists.")
        user_name, pin_code = fridge.read_user_data_from_file()
        fridge.user_name = user_name
        fridge.__pin = pin_code
        print(f"Welcome back, {user_name}")
        fridge.confirm_pin()
        if os.path.isfile('fridge_contents.json'):
            fridge.contents = fridge.extract_fridge_content()
        else:
            fridge.create_fridge_content_file()
    else:
        print("User data file does not exist.")
        fridge.set_attributes_from_input_user()
        fridge.write_user_data_to_file()
        print("User data has been saved to user_data.txt")
        if os.path.isfile('fridge_contents.json'):
            fridge.contents = fridge.extract_fridge_content()
        else:
            fridge.create_fridge_content_file()
    return fridge.contents

# main function of running the fridge
def main():

    run = True
    print(f'Hello {fridge.user_name}!')

    while run is True:
        print(f'What would you like to do?')
        user_command = input('Enter a command ([help] for help meniu): ')
        match user_command:
            case 'help':
                print(f'Help meniu\n')
                print('[contents] - show the contents of the fridge')
                print('[add] - add product')
                print('[remove] - remove product')
                print('[check] - check product quantity')
                print('[edit_product] - editing mode, use at your own risk')
                print('[exit] - exit')
            case 'contents':
                fridge.print_products()
            case 'add':
                name = input('Please enter product name:\n ')
                quantity = input('Enter product quantity:\n ')
                unit = input('Enter product unit of measurment:\n ')
                category = input('Enter product category:\n ')
                add_item = Product(name, quantity, unit, category)
                fridge.add_product(add_item)
            case 'remove':
                name = input('Please enter product name:\n ')
                quantity = input('Enter product quantity:\n ')
                remove_item = Product(name, quantity)
                fridge.remove_product(remove_item)
            case 'check':
                name = input('Please enter product name:\n ')
                check_product = Product(name)
                fridge.check_product_quantity(check_product)
            case 'edit_product':
                name_edit = input('Please enter product you want to edit:\n')
                fridge.edit_product(name_edit)
            case 'recipe':
                while True:
                    recipe = Recipe()
                    print('Recipe meniu, type [help] for help\n')
                    choice = input
                    match choice:
                        case 'help':
                            print('Options:\n')
                            print('[add] - to add ingredient to recipe')
                            print('[change] - change ingredient quantity')
                            print('[remove] - remove ingredient from recipe')
                            print('[create] - create a recepy file')
                            print('[fetch] - fetch recepy file')
                            print('[exit] - exit')
                        case 'add':
                            name = input('Enter name of ingredient:')
                            r_product = recipe.check_ingredient_name(name)
                            if r_product is not None:
                                print(f'Ingredient already is in recipe({r_product.name})')
                                choice = input()
                                pass
                        case 'change':
                            choice = input('Enter ingredient:')
                            c_product = recipe.check_ingredient_name(choice)
                            if c_product is not None:
                                new_quantity = input(f'{c_product.name} {c_product.quantity}Please enter new quantity')
                                recipe.change_ingredient_quantity(c_product, new_quantity)
                        case 'remove':
                            choice = input('Enter ingredient you want to remove: ')
                            r_product = recipe.check_ingredient_name(choice)
                            if r_product is not None:
                                recipe.remove_ingredient(r_product)
                        case 'create':
                            pass
                        case 'fetch':
                            pass
                        case 'exit':
                            break
            case 'exit':
                run = False
                



# Test parameters

product1 = Product("Apple", 5, "pieces", "Fruits")
product2 = Product("Banana", 3, "pieces", "Fruits")
product3 = Product("Milk", 1, "liter", "Dairy")
product4 = Product("Bread", 2, "loaves", "Bakery")

fridge = SmartFridge()

fridge.add_product(product1)
fridge.add_product(product2)
fridge.add_product(product3)
fridge.add_product(product4)

fridge.print_products()

fridge.remove_product(product1)

# if __name__ == "__main__":
#     fridge = SmartFridge()
#     fridge.start()
#     fridge.main()

# fridge = SmartFridge()
# milk = Product('milk', 20, 'l', 'dairy')
# print(milk)
# cheese = Product('cheese', 2, 'Kg', 'dairy' )
# print(cheese)
# fridge.add_product(milk)
# print('first milk')
# print(fridge.contents)
# fridge.add_product(milk)
# fridge.add_product(cheese)
# print(fridge.contents)
# remove_milk = Product('milk', 10)
# fridge.remove_product(remove_milk)
# print('milk removal')
# print(fridge.contents)
# remove_all_milk = Product('milk')
# fridge.remove_product(remove_all_milk)
# print(fridge.contents)
# fridge.contents = {
#     'apple': [5, 'pieces', 'fruits'],
#     'banana': [2, 'pieces', 'fruits'],
#     'milk': [1, 'liter', 'dairy'],
#     'cheese': [250, 'grams', 'dairy'],
#     'lettuce': [1, 'head', 'vegetables'],
# }
# fridge.print_contents()
# recipy_dict = {
#     'apple': [5, 'pieces', 'fruits'],
#     'milk': [1, 'liter', 'dairy'],
#     'cheese': [500, 'grams', 'dairy'],
#     'bread': [1, 'loaf', 'bakery'],
# }
# new_recipe = Recipe(recipy_dict)
# print(new_recipe.ingredients)
# fridge.check_recipe(new_recipe)
# print(fridge.contents)
# fridge._update_json_file()