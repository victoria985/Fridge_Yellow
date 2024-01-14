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