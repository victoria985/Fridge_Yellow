import os
import json

# Not functioning
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


class Smart_Fridge:

    # Defining class
    def __init__(self, user_name: str, pin_code: str, temperature: int = 5, fridge_content: dict = {}):
        self.user_name = user_name
        self.__pin = pin_code
        self.__temperature = temperature
        self.fridge_content = fridge_content


    # String representation of a class for checks
    def __str__(self):
        return f'{self.user_name}: {self.__pin}: {self.__temperature}: {self.fridge_content}'
    
    # Products check function neveikianti pakoklas
    def check_product(self, product_name: str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None
    
    # Products quantity check function neveikia
    def check_product_quantity(self, product: Product, quantity: float):
        return product.quantity - quantity

    # Add product function
    def add_product(self, category, item, quantity: float):
        if category in self.fridge_content:
            self.fridge_content[category].append((item, quantity))
        else:
            self.fridge_content[category] = [(item, quantity)]
        
        # Update JSON file after adding product
        self._update_json_file()
        # Print statement for adding product
        print(f"Added {quantity} of '{item}' to '{category}'")

    # Remove product function
    def remove_product(self, category, item, quantity=None):
        if category in self.fridge_content:
            if any(product[0] == item for product in self.fridge_content[category]):
                updated_items = []
                for product_name, product_quantity in self.fridge_content[category]:
                    if product_name == item:
                        if quantity is None or quantity >= product_quantity:
                            # Remove the entire item if quantity is not given or greater/equal to current quantity
                            continue
                        else:
                            updated_items.append((product_name, product_quantity - quantity))
                    else:
                        updated_items.append((product_name, product_quantity))
                self.fridge_content[category] = updated_items
                # Update JSON file after removing product
                self._update_json_file()
                if quantity is None:
                    # Print statement for removing entire item
                    print(f"Removed '{item}' entirely from '{category}'")
                else:
                    # Print statement for removing product
                    print(f"Removed {quantity} {'units' if quantity > 1 else 'unit'} of '{item}' from '{category}'")
            else:
                print(f"Product '{item}' does not exist in '{category}'. Removal failed.")
        else:
            print(f"Category '{category}' does not exist. Removal failed.")

    # Print fridge content (not working for now)
    def print_contents(self):
        content = self.extract_fridge_content()
        print(content)

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
            json.dump(self.fridge_content, file, indent=4)

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
            json.dump(self.fridge_content, file, indent=4)
    
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
    fridge = Smart_Fridge("", "", 5, fridge_content)
    fridge.main()
    print(fridge)


    fridge.create_fridge_content_file()
    fridge_data = fridge.extract_fridge_content()
    fridge.add_product('dairy', 'butter', 2)
    fridge.add_product('proteins', 'eggs', 50)
    fridge.remove_product('proteins', 'eggs', 20)
    fridge_data = fridge.extract_fridge_content()
    fridge.print_contents
    print(fridge_data)
 