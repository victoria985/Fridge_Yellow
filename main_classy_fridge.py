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
        print(fridge.read_user_data_from_file)
        fridge = SmartFridge(user_name, pin_code)
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
        fridge.create_fridge_content_file()
    return fridge

# main function of running the fridge
def main():

    run = True
    print(f'Hello {fridge.user_name}!')

    while run is True:
        print(f'What would you like to do?')
        user_command = input('Enter a command ([help] for help meniu):\n')
        match user_command.lower():
            case 'help':
                print('Help meniu:\n')
                print('[contents] - show the contents of the fridge')
                print('[add] - add product')
                print('[remove] - remove product')
                print('[check] - check product quantity')
                print('[recipe] - recipe meniu')
                print('[edit_product] - editing mode, use at your own risk')
                print('[exit] - exit')
            case 'contents':
                fridge.print_products()
            case 'add':
                a_name = input('Please enter product name:\n ')
                a_product = fridge.check_product_name(a_name)
                if a_product is not None:
                    print(f'{a_product.name} is in the fridge ({a_product.quantity} {a_product.unit_of_measurement})')
                    while True:
                        a_quantity = input('Please enter quantity you would like to add:\n')
                        if float(a_quantity) is False:
                             print('Wrong value, expecting float')
                        else:
                            break
                    fridge.change_quantity(a_product, float(a_quantity))
                    print(f'In fridge: {a_product.name} : {a_product.quantity} {a_product.unit_of_measurement}')
                else:
                    while True:
                        quantity = input('Enter product quantity:\n ')
                        if float(quantity) is False:
                            print('Wrong value, expecting float')
                        else:
                            break
                    unit = input('Enter product unit of measurment:\n ')
                    category = input('Enter product category:\n ')
                    a_product = Product(a_name, float(quantity), unit, category)
                    fridge.add_product(a_product)
            case 'remove':
                r_name = input('Please enter product name:\n ')
                r_product = fridge.check_product_name(r_name)
                if r_product is not None:
                    fridge.remove_product(r_product)
                else:
                    print(f'{r_name} is not in the fridge')
            case 'check':
                name = input('Please enter product name:\n ')
                check_product = fridge.check_product_name(name)
                fridge.check_product_quantity(check_product)
            case 'edit_product':
                name_edit = input('Please enter product you want to edit:\n')
                fridge.edit_product(name_edit)
            case 'recipe':
                recipe = Recipe()
                while True:
                    print('Recipe meniu, type [help] for help\n')
                    choice = input()
                    match choice.lower():
                        case 'help':
                            print('Options:\n')
                            print('[add] - to add ingredient to recipe')
                            print('[change] - change ingredient quantity')
                            print('[remove] - remove ingredient from recipe')
                            print('[check] - check fridge contents for recipe ingredients needed')
                            print('[create] - create a recipe file')
                            print('[fetch] - fetch recipe file')
                            print('[exit] - exit')
                        case 'add':
                            i_name = input('Please enter name:\n')
                            i_quantity = float(input('Please enter quantity:\n'))
                            i_product = fridge.check_product_name(i_name)
                            if i_product is None:
                                i_unit = input('Please enter unit of measurement:\n')
                                i_category = input('Please enter category:\n')
                                i_product = Product(i_name, 0 , i_unit, i_category, i_quantity)
                                recipe.add_ingredient(i_product)
                                fridge.add_product(i_product)
                                print(f'{i_product.recipe_quantity} {i_product.unit_of_measurement} of {i_name} has been added to recipe')
                            else:
                                i_product.recipe_quantity = i_quantity
                                recipe.add_ingredient(i_product)
                                print(f'{i_product.recipe_quantity} {i_product.unit_of_measurement} of {i_name} has been added to recipe')
                        case 'change':
                            i_name = input('Please enter name:\n')
                            i_product = recipe.check_ingredient_name(i_name)
                            if i_product is not None:
                                i_value = input('Please enter new quantity in recipe:\n')
                                recipe.change_ingredient_quantity(i_product, i_value)
                            else:
                                print(f'{i_name} is not in recipe, try adding it')
                        case 'remove':
                            i_name = input('Please enter name:\n')
                            i_remove = recipe.check_ingredient_name(i_name)
                            if i_remove is not None:
                                recipe.remove_ingredient(i_remove)
                            else:
                                print(f'You are trying to remove what does not exist in recipe')
                        case 'check':
                            fridge.check_recipe(recipe)
                        case 'create':
                            pass
                        case 'fetch':
                            pass
                        case 'exit':
                            break
            case 'exit':
                fridge._update_json_file
                run = False
                return run
                



# Test parameters

fridge = start()
main()