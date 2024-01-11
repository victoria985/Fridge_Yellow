import os
import json

# Functioning product class
class Product:

    # Defining Class
    def __init__(self, name, quantity:float = 0, unit_of_measurement: str = 'unit', category: str = '', **kwargs):
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = unit_of_measurement
        self.category = category
        for key, value in kwargs.items():
            setattr(self, key, value)

    # Defininf str output
    def __str__(self) -> str:
        return f"{self.category}: {self.name}- {self.quantity} {self.unit_of_measurement}"

    # Defininf repr output
    def __repr__(self) -> str:
        return f"'{self.name}': ({self.quantity}, '{self.unit_of_measurement}', '{self.category}')"


# Class not functional for now
class Recipe:

    def __init__(self, ingredients:dict = {}, instruction:str = ''):
        self.ingredients = ingredients
        self.instruction = instruction
    
    # ingredient check, used in later functions
    def check_ingredient(self, product: Product):
        return product.name in self.ingredients.keys()

    # ingredients check for recepy, returs modified list for convinience
    def check_ingredients_needed(self):
        ingredients_check = {}
        for key, value in self.ingredients.items():
            ingredients_check[key] = value
        return ingredients_check
    
    # add function
    def add_ingredient(self, product: Product):
        self.ingredients[product.name] = [{product.quantity}, product.unit_of_measurement]

    # change value fucntion
    def change_ingredient_quantity(self, product:Product, new_quantity):
        if self.check_ingredient(product) is True:
            self.ingredients[product.name][0] = new_quantity
    
    # remove ingredient function
    def remove_ingredient(self, product):
        if self.check_ingredient(product) is True:
            del self.ingredients[product.name]
        else:
            print(f'You are trying to remove what does not exist in recipe')


class SmartFridge:

    # Defining class
    def __init__(self, user_name: str = '', pin_code: str = '', temperature: int = 5, contents: dict = {}):
        self.user_name = user_name
        self.__pin = pin_code
        self.__temperature = temperature
        self.contents = contents


    # String representation of a class for checks
    def __str__(self):
        return f'{self.user_name}: {self.__pin}: {self.__temperature}: {self.contents}'
    
    # Products check function neveikianti pakoklas
    def check_product(self, product:Product):
        return product.name in self.contents.keys()
        
    # Products quantity check function neveikia
    def check_product_quantity(self, product: Product):
        if self.check_product(product) is True:
            return self.contents[product.name][0]
        else:
            print(f'{product.name} has not been found in the fridge')

    # Add product function
    def add_product(self, product:Product):
        if not self.check_product(product):
            self.contents[product.name] = [product.quantity, product.unit_of_measurement, product.category]
        else:
            new_quantity = self.contents[product.name][0] + product.quantity
            self.contents[product.name][0] = new_quantity
    
    # Removing product
    def remove_product(self, product):
        if self.check_product(product):
            current_quantity = self.contents[product.name][0]
            if product.quantity <= 0:
                del self.contents[product.name]
            elif product.quantity >= current_quantity:
                del self.contents[product.name]
            else:
                new_quantity = current_quantity - product.quantity
                self.contents[product.name][0] = new_quantity
        else:
            print(f"Product '{product.name}' not found in inventory.")
            
    # Print fridge content
    def print_contents(self):
        printable_content = {}
        for product, values in self.contents.items():
            category = values[2]
            product_info = f"{product}: {values[0]} {values[1]}"
            
            if category not in printable_content:
                printable_content[category] = [product_info]
            else:
                printable_content[category].append(product_info)

        for category, products in printable_content.items():
            print(f"{category}:")
            for product_info in products:
                print(f"  {product_info}")


    # Recepy check function (not working)
    def check_recipe(self, recipe: Recipe):
        for key in recipe.ingredients.keys():
            if key in self.contents.keys():
                needed = recipe.ingredients[key][0]
                inside = self.contents[key][0]
                unit = self.contents[key][1]
                if needed <= inside:
                    print(f'There is enough {key} to make the recipe\nIn fridge: {inside} {unit} \nneeded: \033[32m{needed} {unit}\033[0m')
            else:
                print(f'There is not enough {key} to make the recipe\nIn fridge: \033[31m{inside} {unit}\033[0m \nneeded: \033[31m{needed} {unit}\033[0m')
        else:
            print(f'Item \033[31m{key}\033[0m does not exist in the fridge')

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
                if line.startswith('user_name'):
                    user_name = line.split('=')[1].strip()
                elif line.startswith('pin_code'):
                    pin_code = line.split('=')[1].strip()
        return user_name, pin_code

    # Function to change class values to user information
    def set_attributes_from_input_user(self):
        user_name, pin_code = self.get_user_input()
        self.user_name = user_name
        self.__pin = pin_code

    # Pin code check
    def confirm_pin(self):
        while True:
            confirm_pin = input("Please confirm your PIN code: ")
            if confirm_pin == self.__pin:
                print("PIN code confirmed.")
                break
            else:
                print("PIN code does not match. Please try again.")
    
    # Closing fridge, save file and exit program
    def close_fridge(self):
        self._update_json_file()
    
    # Main function of runing the fridge
    def main(self):
        if os.path.isfile('user_data.txt'):
            print("User data file already exists.")
            user_name, pin_code = self.read_user_data_from_file()
            self.user_name = user_name
            self.__pin = pin_code
            print(f"Welcome back, {user_name}")
            self.confirm_pin()
            if os.path.isfile('fridge_contents.json'):
                self.contents = self.extract_fridge_content()
            else:
                self.create_fridge_content_file()
        else:
            print("User data file does not exist.")
            self.set_attributes_from_input_user()
            self.write_user_data_to_file()
            print("User data has been saved to user_data.txt")
            if os.path.isfile('fridge_contents.json'):
                self.contents = self.extract_fridge_content()
            else:
                self.create_fridge_content_file()
        return self.contents


# Test parameters

if __name__ == "__main__":
    fridge = SmartFridge()
    fridge.main()


    milk = Product('milk', 20, 'l', 'dairy')
    print(milk)
    cheese = Product('cheese', 2, 'Kg', 'dairy' )
    print(cheese)
    fridge.add_product(milk)
    print('first milk')
    print(fridge.contents)
    fridge.add_product(milk)
    fridge.add_product(cheese)
    print(fridge.contents)
    remove_milk = Product('milk', 10)
    fridge.remove_product(remove_milk)
    print('milk removal')
    print(fridge.contents)
    remove_all_milk = Product('milk')
    fridge.remove_product(remove_all_milk)
    print(fridge.contents)
    fridge.contents = {
        'apple': [5, 'pieces', 'fruits'],
        'banana': [2, 'pieces', 'fruits'],
        'milk': [1, 'liter', 'dairy'],
        'cheese': [250, 'grams', 'dairy'],
        'lettuce': [1, 'head', 'vegetables'],
    }
    fridge.print_contents()
    recipy_dict = {
        'apple': [5, 'pieces', 'fruits'],
        'milk': [1, 'liter', 'dairy'],
        'cheese': [500, 'grams', 'dairy'],
        'bread': [1, 'loaf', 'bakery'],
    }
    new_recipe = Recipe(recipy_dict)
    print(new_recipe.ingredients)
    fridge.check_recipe(new_recipe)
    print(fridge.contents)
    fridge._update_json_file()
 