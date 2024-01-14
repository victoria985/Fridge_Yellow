import json
from class_product import Product

class Recipe:

    # defining class
    def __init__(self, ingredients: list = [], instruction:str = ''):
        self.ingredients = ingredients
        self.instruction = instruction
    
    # ingredient check, used in later functions
    def check_ingredient(self, product: Product):
        return product in self.ingredients
    
    # check product from name
    def check_ingredient_name(self, product_name:str):
        for product in self.ingredients:
            if product.name == product_name:
                return product
        return  None

    # add function
    def add_ingredient(self, product: Product):
        self.ingredients.append(product)

    # change value fucntion
    def change_ingredient_quantity(self, product:Product, new_quantity):
        product.recipe_quantity = new_quantity
            
    
    # remove ingredient function
    def remove_ingredient(self, product: Product):
        if self.check_ingredient(product) is True:
            self.ingredients.remove(product)
        else:
            print(f'You are trying to remove what does not exist in recipe')
    
    # create json file for recipe
    def save_to_json(self, filename):
        recipe_file = f'{filename}.json'
        data = []
        for product in self.ingredients:
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
        with open(recipe_file, 'w') as json_file:
            json.dump(data, json_file, indent=2)
    
    def load_from_json(self, filename):
        # Initialize an empty list to store the loaded data
        recipe_file = f'{filename}.json'
        loaded_products = []

        try:
            # Load data from the JSON file
            with open(recipe_file, 'r') as json_file:
                loaded_data = json.load(json_file)

            # Create Product objects from the loaded data
            loaded_products = [Product(**product_data) for product_data in loaded_data]

        except FileNotFoundError:
            print(f"File '{recipe_file}' not found.")

        # Always update self.contents, even if it's an empty list
        self.ingredients = loaded_products

        return loaded_products
    
    # extract recipy from json file
    def extract_recipe(self, recipe_name):
        file_name = f'{recipe_name}.json'
        with open(file_name, 'r') as file:
            print('extracting file')
            recipe_data = json.load(file)
            return recipe_data