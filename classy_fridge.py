import os
import json

# Functioning product class
class Product:

    # Defining Class
    def __init__(self, name: str, unit_of_measurement: str = 'unit', quantity: float = 0 , **kwargs) -> None:
        self.name = name
        self.unit_of_measurement = unit_of_measurement  # options: kg, g, L, ml
        self.quantity = quantity
        for key, value in kwargs.items():
            setattr(self, key, value)

    # Defininf str output
    def __str__(self) -> str:
        return f"{self.category}: {self.name}: {self.quantity} {self.unit_of_measurement}"

    # Defininf repr output
    def __repr__(self) -> str:
        return f"({self.category}, {self.name}, {self.quantity}, {self.unit_of_measurement})"


# Class not functional for now
class Recipe:
    ingredients = []
    instructions = ""

    def add_ingredient(self, product: Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id: int, new_quantity: float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id: int):
        self.ingredients.pop(ingredient_id)


class SmartFridge: # no underscore

    # Defining class
    def __init__(self, user_name: str, pin_code: str, temperature: int = 5, content: dict = {}):
        self.user_name = user_name
        self.__pin = pin_code
        self.__temperature = temperature
        self.content = content


    # String representation of a class for checks
    def __str__(self):
        return f'{self.user_name}: {self.__pin}: {self.__temperature}: {self.content}'
    
    # Products check function neveikianti pakoklas
    def check_product(self, product_name: str) -> (int, Product):
        for product_id, product in enumerate(self.content):
            if product['name'] == product_name:
                return product_id, product
        return None, None
    
    # Products quantity check function neveikia
    def check_product_quantity(self, product: Product, quantity: float):
        return product.quantity - quantity

    # Add product function
    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))

    # Remove product function
    def remove_product(self, category, product: Product, quantity=None):
        if category in self.content:
            if any(prod['name'] == product.name for prod in self.content[category]):
                updated_items = []
                for prod in self.content[category]:
                    if prod['name'] == product.name:
                        if quantity is None or quantity >= prod['quantity']:
                            continue
                        else:
                            updated_items.append({'name': prod['name'], 'quantity': prod['quantity'] - quantity, 'unit_of_measurement': prod['unit_of_measurement']})
                    else:
                        updated_items.append(prod)
                self.content[category] = updated_items
                self._update_json_file()
                if quantity is None:
                    print(f"Removed '{product.name}' entirely from '{category}'")
                else:
                    print(f"Removed {quantity} {'units' if quantity > 1 else 'unit'} of '{product.name}' from '{category}'")
            else:
                print(f"Product '{product.name}' does not exist in '{category}'. Removal failed.")
        else:
            print(f"Category '{category}' does not exist. Removal failed.")

    # Print fridge content
    def print_contents(self):
        print(self.content)


    # Recepy check function (not working)
    def check_recipe(self, recipe: Recipe):
        pass

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
        file_name = 'fridge_content.json'

        with open(file_name, 'w') as file:
            json.dump(self.content, file, indent=4)

    # Extraction of json file
    def extract_fridge_content(self):
        file_name = 'fridge_content.json'

        with open(file_name, 'r') as file:
            data = json.load(file)
            return data

    # Update json file
    def _update_json_file(self):
        file_name = 'fridge_content.json'

        with open(file_name, 'w') as file:
            json.dump(self.content, file, indent=4)
    
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
    
    # Main function of runing the fridge
    def main(self):
        if os.path.isfile('user_data.txt'):
            print("User data file already exists.")
            user_name, pin_code = self.read_user_data_from_file()
            self.user_name = user_name
            self.__pin = pin_code
            print(f"Welcome back, {user_name}")
            self.confirm_pin()
        else:
            print("User data file does not exist.")
            self.set_attributes_from_input_user()
            self.write_user_data_to_file()
            print("User data has been saved to user_data.txt")


# Test parameters

fridge_content = {
    'proteins': [
        ('chicken', 2),
        ('beef', 3),
        ('tofu', 4)
    ],
    'dairy': [
        ('milk', 1),
        ('cheese', 2),
        ('yogurt', 3)
    ],
    'starch': [
        ('rice', 2),
        ('pasta', 3),
        ('potato', 4)
    ],
    'fruits/vegetables': [
        ('apple', 5),
        ('broccoli', 2),
        ('banana', 3)
    ],
    'fats': [
        ('avocado', 2),
        ('olive oil', 3),
        ('nuts', 4)
    ]
}

if __name__ == "__main__":
    fridge = SmartFridge("", "", 5, fridge_content)
    fridge.main()
    print(fridge)


    fridge.create_fridge_content_file()
    fridge_data = fridge.extract_fridge_content()
    product_to_add = Product('butter', quantity=2, unit_of_measurement='kg')
    product_to_remove = Product('milk', quantity=1, unit_of_measurement='L')

    # Adding product
    fridge.add_product('dairy', product_to_add)

    # Removing product
    fridge.remove_product('dairy', product_to_remove)
    fridge_data = fridge.extract_fridge_content()
    fridge.print_contents
    print(fridge_data)
 