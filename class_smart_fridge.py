import os
import json
from class_recipe import Recipe
from class_product import Product

class SmartFridge:

    # Defining class
    def __init__(self, user_name: str = '', pin_code: str = '', temperature: int = 5, contents: list = []):
        self.user_name = user_name
        self.__pin = pin_code
        self.__temperature = temperature
        self.contents = contents


    # String representation of a class for checks
    def __str__(self):
        return f'{self.user_name}: {self.__pin}: {self.__temperature}: {self.contents}'
    
    def check_product(self, product: Product):
        return product in self.contents
    
    # Products check function 
    def check_product_name(self, product_name:str):
        for product in self.contents:
            if product.name == product_name:
                return product
        return  None
    
    # check product function
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    # add product fucntion
    def add_product(self, product: Product):
            if self.check_product(product) is False:
                self.contents.append(product)
            else:
                print(f'{product.name} alredy is in the fridge({product.quantity} {product.unit_of_measurement}), please enter quantity you would like to add')
                quantity = float(input)
                self.change_quantity(product, quantity)

    # remove product    
    def remove_product(self, product: Product):
        if self.check_product(product):
            print(f'{product.name} found ({product.quantity}).\nPlease choose what to do with it (type [r] to remove completely or enter [quantity] to remove a specified amount)')
            
            while True:
                choice = input("Your choice: ")
                if choice == 'r':
                    self.contents.remove(product)
                    break
                elif choice.isdigit():
                    quantity = int(choice)
                    if quantity < product.quantity:
                        new_quantity = self.check_product_quantity(product, quantity)
                        product.quantity = new_quantity
                    else:
                        self.contents.remove(product)
                    break
                else:
                    print("Invalid input. Please enter 'r' to remove or a numeric value for quantity.")
    
    # change quantity function
    def change_quantity(self, product: Product, quantity:float):
         new_quantity = product.quantity + quantity
         product.quantity = new_quantity
            
    # Print fridge content
    def print_products(self):
        # Create a dictionary to store products by category
        products_by_category = {}

        # Group products by category
        for product in self.contents:
            category = product.category
            if category not in products_by_category:
                products_by_category[category] = []
            products_by_category[category].append(product)

        # Print products by category
        for category, products in products_by_category.items():
            print(f"{category}:")
            for product in products:
                print(f"{product.name} - {product.quantity} {product.unit_of_measurement}")
            print()


    # Recipe check function (not working)
    def check_recipe(self, recipe: Recipe):
        for key in recipe.ingredients.keys():
            if key in self.contents.keys():
                needed = recipe.ingredients[key][0]
                inside = self.contents[key][0]
                unit = self.contents[key][1]
                if needed <= inside:
                    print(f'There is enough {key} to make the recipe\nIn fridge: {inside} {unit} \nneeded: \033[32m{needed} {unit}\033[0m')
            else:
                print(f'There is not enough {key} to make the recipe\nIn fridge: \033[31m{inside} {unit}\033[0m \nneeded: \033[91m{needed} {unit}\033[0m')
        else:
            print(f'Item \033[91m{key}\033[0m does not exist in the fridge')

    # extract product from contents for further use
    # will be writen if needed later
    
    # editing mode of the product, removes product form content, stores it localy, and then adds it back once finished
    def edit_product(self, product_name):
        edit_product = self.check_product_name(product_name)
        while True:
            print(f'Product info:\n {edit_product.__str__()}')
            choice = input('Product editing mode on. Please chose command ([exit], [name], [quantity], [unit], [category])')
            match choice:
                case 'name':
                    new_name = input('Enter new name:')
                    edit_product.name = new_name
                case 'quantity':
                    new_quantity = input('Enter new quantity:')
                    edit_product.quantity = new_quantity
                case 'unit':
                    new_unit = input('Enter new unit:')
                    edit_product.unit_of_measurement = new_unit
                case 'category':
                    new_category = input('Enter new category:')
                    edit_product.category = new_category
                case 'exit':
                    break
            
    # User input function to get user name and pin code
    @staticmethod
    def get_user_input():
        user_name = input("Enter your username: ")
        while True:
            pin_code = input("Enter your 4-digit PIN code: ")
            if pin_code.isdigit() and len(pin_code) == 4:
                break
            else:
                print("Invalid PIN code. Please enter a 4-digit number.")
        return user_name, pin_code

    # Function to save user information localy
    def write_user_data_to_file(self):
        with open('user_data.txt', 'w') as file:
            file.write(f"user_name = {self.user_name}\n")
            file.write(f"pin_code = {self.__pin}")

    # Creation of json file
    def create_fridge_content_file(self):
        file_name = 'fridge_contents.json'

        if self.contents:
            with open(file_name, 'w') as file:
                print('creating file')
                json.dump(self.contents, file, indent=4)

    # Extraction of json file
    def extract_fridge_content(self):
        file_name = 'fridge_contents.json'
        with open(file_name, 'r') as file:
            print('extracting file')
            data = json.load(file)
            return data

    # Update json file
    def _update_json_file(self):
        file_name = 'fridge_contents.json'

        with open(file_name, 'w') as file:
            json.dump(self.contents, file, indent=4)
    
    # Read and extract user data from storage
    def read_user_data_from_file(self):
        user_name = None
        pin_code = None
        with open('user_data.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                if key == 'user_name':
                    user_name = value
                elif key == 'pin_code':
                    pin_code = value
        return user_name, pin_code

    # Function to change class values to user information
    def set_attributes_from_input_user(self):
        user_name, pin_code = self.get_user_input()
        self.user_name = user_name
        self.__pin = pin_code

    # Pin code check
    def confirm_pin(self):
        while True:
            pin = input("Please confirm your PIN code: ")
            if pin == self.__pin:
                print("PIN code confirmed.")
                break
            else:
                print("PIN code does not match. Please try again.")
    
    # Closing fridge, save file and exit program
    def close_fridge(self):
        self._update_json_file()