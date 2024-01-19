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
    def check_product_quantity(self, product:Product, quantity:float = 0):
        return print(f'{product.name} : {product.quantity} {product.unit_of_measurement}')

    # add product fucntion
    def add_product(self, product: Product):
            self.contents.append(product)
            print(f'{product.quantity} {product.unit_of_measurement} of {product.name} has been added to the fridge')

    # remove product    
    def remove_product(self, product: Product):
        if self.check_product(product):
            print(f'{product.name} found ({product.quantity}).\nPlease choose what to do with it (type [r] to remove completely or enter [quantity] to remove a specified amount)')
            
            while True:
                choice = input("Your choice: ")
                if choice == 'r':
                    self.contents.remove(product)
                    print(f'{product.name} has been removed from fridge')
                    break
                elif choice.isdigit():
                    quantity = float(choice)
                    if quantity < product.quantity:
                        new_quantity = self.check_product_quantity(product, quantity)
                        product.quantity = new_quantity
                        print(f'In fridge: {product.name} - {product.quantity} {product.unit_of_measurement}')
                    else:
                        self.contents.remove(product)
                        print(f'{product.name} has been removed from fridge')
                    break
                else:
                    print("Invalid input. Please enter 'r' to remove or a numeric value for quantity.")
    
    # change quantity function
    def change_quantity(self, product: Product, quantity:float):
         new_quantity = product.quantity + quantity
         product.quantity = new_quantity
            
    # Print fridge content
    def print_products(self):

        if self.contents == []:
            print('FRIDGE IS EMPTY')
        else:
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
                print(f'\n{category}:')
                for product in products:
                    if product.quantity > 0:
                        print(f'{product.name} - {product.quantity} {product.unit_of_measurement}')
                print()


    # Recipe check function (not working)
    def check_recipe(self, recipe: Recipe):
        for ingredient in recipe.ingredients:
            if ingredient.quantity >= ingredient.recipe_quantity:
                print(f'There is enough of {ingredient.name} to make the recipe (in fridge: {ingredient.quantity}, needed : {ingredient.recipe_quantity})')
            else:
                print(f'Needed for recipe: {ingredient.name} {ingredient.recipe_quantity} {ingredient.unit_of_measurement}')
            
    # extract product from contents for further use
    # will be writen if needed later
    
    # editing mode of the product, removes product form content, stores it localy, and then adds it back once finished
    def edit_product(self, product_name):
        edit_product = self.check_product_name(product_name)
        while True:
            print(f'Product info:\n {edit_product.__str__()}')
            choice = input('Product editing mode on. Please chose command ([exit], [name], [quantity], [unit], [category])\n')
            match choice:
                case 'name':
                    new_name = input('Enter new name:\n')
                    edit_product.name = new_name
                case 'quantity':
                    new_quantity = input('Enter new quantity:\n')
                    edit_product.quantity = new_quantity
                case 'unit':
                    new_unit = input('Enter new unit:\n')
                    edit_product.unit_of_measurement = new_unit
                case 'category':
                    new_category = input('Enter new category:\n')
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
            file.write(f"user_name={self.user_name}\n")
            file.write(f"pin_code={self.__pin}")

    # Creation of json file
    def create_fridge_content_file(self):
        file_name = 'fridge_contents.json'

        with open(file_name, 'w') as file:
            print('creating file')
            json.dump(self.contents, file, indent=4)

    # Extraction of json file
    def load_from_json(self, filename):
        # Initialize an empty list to store the loaded data
        loaded_products = []

        try:
            # Load data from the JSON file
            with open(filename, 'r') as json_file:
                loaded_data = json.load(json_file)

            # Create Product objects from the loaded data
            loaded_products = [Product(**product_data) for product_data in loaded_data]

        except FileNotFoundError:
            print(f"File '{filename}' not found.")

        # Always update self.contents, even if it's an empty list
        self.contents = loaded_products

        return loaded_products

    # Update json file
    def save_to_json(self, filename = 'fridge_contents.json'):
        data = []
        for product in self.contents:
            # Convert each product to a dictionary
            product_dict = {
                "name": product.name,
                "quantity": product.quantity,
                "unit_of_measurement": product.unit_of_measurement,
                "category": product.category,
                "recipe_quantity": product.recipe_quantity
                # Add any additional attributes from kwargs as needed
            }
            data.append(product_dict)

        # Save the list of product dictionaries to a JSON file
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)
    
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
            pin = input("Please confirm your PIN code: ").strip()
            if pin == self.__pin:
                print("PIN code confirmed.")
                break
            else:
                print("PIN code does not match. Please try again.")