import os
import json

class Product:
    def __init__(self, name: str, unit_of_measurement: str = 'unit', quantity: float = 0, **kwargs) -> None:
        self.name = name
        self.unit_of_measurement = unit_of_measurement
        self.quantity = quantity
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit_of_measurement}"

    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity}, {self.unit_of_measurement})"

class Recipe:
    def __init__(self):
        self.ingredients = []
        self.instructions = ""

    def add_ingredient(self, product: Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id: int, new_quantity: float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id: int):
        if 0 <= ingredient_id < len(self.ingredients):
            self.ingredients.pop(ingredient_id)
        else:
            print("Invalid ingredient ID.")

class Smart_Fridge:
    def __init__(self, user_name: str, pin_code: str, temperature: int = 5, fridge_content: dict = {}):
        self.user_name = user_name
        self.__pin = pin_code
        self.__temperature = temperature
        self.fridge_content = fridge_content

    def __str__(self):
        return f'{self.user_name}: {self.__pin}: {self.__temperature}: {self.fridge_content}'

    def check_product(self, product_name: str) -> (int, Product):
        for product_id, product in enumerate(self.fridge_content):
            if product['name'] == product_name:
                return product_id, product
        return None, None

    def check_product_quantity(self, product: Product, quantity: float):
        return product.quantity - quantity

    def add_product(self, category, product: Product):
        if category in self.fridge_content:
            self.fridge_content[category].append({'name': product.name, 'quantity': product.quantity, 'unit_of_measurement': product.unit_of_measurement})
        else:
            self.fridge_content[category] = [{'name': product.name, 'quantity': product.quantity, 'unit_of_measurement': product.unit_of_measurement}]
        self._update_json_file()
        print(f"Added {product.quantity} of '{product.name}' to '{category}'")

    def remove_product(self, category, product: Product, quantity=None):
        if category in self.fridge_content:
            if any(prod['name'] == product.name for prod in self.fridge_content[category]):
                updated_items = []
                for prod in self.fridge_content[category]:
                    if prod['name'] == product.name:
                        if quantity is None or quantity >= prod['quantity']:
                            continue
                        else:
                            updated_items.append({'name': prod['name'], 'quantity': prod['quantity'] - quantity, 'unit_of_measurement': prod['unit_of_measurement']})
                    else:
                        updated_items.append(prod)
                self.fridge_content[category] = updated_items
                self._update_json_file()
                if quantity is None:
                    print(f"Removed '{product.name}' entirely from '{category}'")
                else:
                    print(f"Removed {quantity} {'units' if quantity > 1 else 'unit'} of '{product.name}' from '{category}'")
            else:
                print(f"Product '{product.name}' does not exist in '{category}'. Removal failed.")
        else:
            print(f"Category '{category}' does not exist. Removal failed.")

    def print_contents(self):
        print(self.fridge_content)

    def check_recipe(self, recipe: Recipe):
        pass

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

    def write_user_data_to_file(self):
        with open('user_data.txt', 'w') as file:
            file.write(f"user_name = {self.user_name}\n")
            file.write(f"pin_code = {self.__pin}")

    def create_fridge_content_file(self):
        file_name = 'fridge_content.json'
        with open(file_name, 'w') as file:
            json.dump(self.fridge_content, file, indent=4)

    def extract_fridge_content(self):
        file_name = 'fridge_content.json'
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data

    def _update_json_file(self):
        file_name = 'fridge_content.json'
        with open(file_name, 'w') as file:
            json.dump(self.fridge_content, file, indent=4)

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

    def set_attributes_from_input_user(self):
        user_name, pin_code = self.get_user_input()
        self.user_name = user_name
        self.__pin = pin_code

    def confirm_pin(self):
        while True:
            confirm_pin = input("Please confirm your PIN code: ")
            if confirm_pin == self.__pin:
                print("PIN code confirmed.")
                break
            else:
                print("PIN code does not match. Please try again.")
    
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
        {'name': 'chicken', 'quantity': 2},
        {'name': 'beef', 'quantity': 3},
        {'name': 'tofu', 'quantity': 4}
    ],
    'dairy': [
        {'name': 'milk', 'quantity': 1},
        {'name': 'cheese', 'quantity': 2},
        {'name': 'yogurt', 'quantity': 3}
    ],
    'starch': [
        {'name': 'rice', 'quantity': 2},
        {'name': 'pasta', 'quantity': 3},
        {'name': 'potato', 'quantity': 4}
    ],
    'fruits/vegetables': [
        {'name': 'apple', 'quantity': 5},
        {'name': 'broccoli', 'quantity': 2},
        {'name': 'banana', 'quantity': 3}
    ],
    'fats': [
        {'name': 'avocado', 'quantity': 2},
        {'name': 'olive oil', 'quantity': 3},
        {'name': 'nuts', 'quantity': 4}
    ]
}

if __name__ == "__main__":
    fridge = Smart_Fridge("", "", 5, fridge_content)
    fridge.main()
    print(fridge)

    fridge.create_fridge_content_file()
    fridge_data = fridge.extract_fridge_content()
    product_to_add = Product('butter', quantity=2, unit_of_measurement='kg')
    product_to_remove = Product('milk', quantity=1, unit_of_measurement='L')

    fridge.add_product('dairy', product_to_add)
    fridge.remove_product('dairy', product_to_remove)
    fridge.print_contents()
