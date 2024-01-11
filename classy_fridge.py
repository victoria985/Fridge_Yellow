import os
import json

# Functioning product class
class Product:

    # Defining Class
    def __init__(self, name, quantity: float = 0, unit_of_measurement: str = 'unit', category: str = '', **kwargs):
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

    def __init__(self, ingredients: list = [], instruction:str = ''):
        self.ingredients = ingredients
        self.instruction = instruction
    
    # ingredient check, used in later functions
    def check_ingredient(self, product: Product):
        return product in self.ingredients
    
    # check product from name
    def check_ingredient_name(self, product_name:str):
        for product in self.contents:
            if product.name == product_name:
                return product
        return  None

    # add function
    def add_ingredient(self, product: Product):
        if self.check_ingredient(product) is True:
            print('Ingredient already exists in recipe, try changing it')
        else:
            self.ingredients.append(product)

    # change value fucntion
    def change_ingredient_quantity(self, product:Product, new_quantity):
        if self.check_ingredient(product) is True:
            product.quantity = new_quantity
    
    # remove ingredient function
    def remove_ingredient(self, product):
        if self.check_ingredient(product) is True:
            self.ingredients.pop(product)
        else:
            print(f'You are trying to remove what does not exist in recipe')
    
    # create json file for recipe
    def create_recipe_file(self, recipe_name):
        file_name = f'{recipe_name}.json'

        if self.contents:
            with open(file_name, 'w') as file:
                print('creating recipe file')
                json.dump(self.contents, file, indent=4)
    
    # extract recipy from json file
    def extract_recipe(self, recipe_name):
        file_name = f'{recipe_name}.json'
        with open(file_name, 'r') as file:
            print('extracting file')
            recipe_data = json.load(file)
            return recipe_data


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
        
    def remove_product(self, product: Product):
        if self.check_product(product) is True:
            print(f'{product.name} found.\nPlease choose what do do with it (type [r] for remove completety or enter [quantity] to remove ammount specified)')
            choice = input
            if choice == 'r':
                self.contents.pop(product)
            else:
                quantity = float(choice)
                new_quantity = self.check_product_quantity(product, quantity)
                product.quantity = new_quantity
    
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
                print(f'There is not enough {key} to make the recipe\nIn fridge: \033[31m{inside} {unit}\033[0m \nneeded: \033[91m{needed} {unit}\033[0m')
        else:
            print(f'Item \033[91m{key}\033[0m does not exist in the fridge')

    # extract product from contents for further use
    def extract_product(self, product_name):
        if product_name in self.contents.keys():
            name = product_name
            quantity = self.contents[product_name][0]
            unit = self.contents[product_name][1]
            category = self.contents[product_name][2]
            extracted_product = Product(name, quantity, unit, category)
            return extracted_product
    
    # editing mode of the product, removes product form content, stores it localy, and then adds it back once finished
    def edit_product(self, product_name):
            edit_product = self.extract_product(product_name)
            self.remove_product(edit_product)
            print(edit_product)
            while True:
                choise = input('Chose parameter you want to change([done] to finish):\n')
                match choise:
                    case 'name':
                        new_name = input('Enter new name: ')
                        edit_product.name = new_name
                    case 'quantity':
                        new_quantity = input('Enter new quantity: ')
                        edit_product.quantity = new_quantity
                    case 'unit':
                        new_unit = input('Enter new unit: ')
                        edit_product.unit = new_unit
                    case 'category':
                        new_category = input('Enter new category: ')
                        edit_product.category = new_category
                    case 'done':
                        self.add_product(edit_product)
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
    
    # Main function of starting the fridge
    def start(self):
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

    # main function of running the fridge
    def main(self):

        run = True
        print(f'Hello {self.user_name}!')

        while run is True:
            print(f'What would you like to do?')
            user_command = input('Enter a command: ')
            match user_command:
                case 'help':
                    print(f'Help menue\n')
                    print()
                case 'contents':
                    self.print_contents()
                case 'add':
                    name = input('Please enter product name:\n ')
                    quantity = input('Enter product quantity:\n ')
                    unit = input('Enter product unit of measurment:\n ')
                    category = input('Enter product category:\n ')
                    add_item = Product(name, quantity, unit, category)
                    self.add_product(add_item)
                case 'remove':
                    name = input('Please enter product name:\n ')
                    quantity = input('Enter product quantity:\n ')
                    remove_item = Product(name, quantity)
                    self.remove_product(remove_item)
                case 'check':
                    name = input('Please enter product name:\n ')
                    check_product = Product(name)
                    self.check_product_quantity(check_product)
                case 'edit_product':
                    while True:
                        print('Product editing mode on\n')
                        choise = input('Enter product name if you like to proceed (type [exit] to leave this mode):\n')
                        if choise == 'exit':
                                break
                        else:
                            self.edit_product(choise)
                case 'recipe':
                    print('Recepy meniu\n')
                    print('Options:\n[add] - to add product to recepy\n[]')
                    



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