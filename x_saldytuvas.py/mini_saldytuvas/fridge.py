from product import Product
from recipe import Recipe
import json


class Fridge:
    contents = []

    def __init__(self):
        self.contents = []
        with open('fridge.json', 'r', encoding='utf-8') as fridge_file:
            contents = json.load(fridge_file)
        if contents and len(contents) > 0:    
            for content_dict in contents:
                self.contents.append(Product(product_dict['name'], product_dict['quantity'], product_dict['unit_of_measurementf']))   

    def save(self):
        with open('fridge.json', 'w', encoding='utf-8') as fridge_file:
            contents = []
            for product in self.contents:   
                contents.append({'name': product name,
                                'quantity': product quantity,
                                'unit_of_measurementf': product unit_of_measurement
                                }) 
            json.dump(contents, fridge_file)

        

    def check_product(self, product_name: str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product.name, product
        return None, None

    def check_product_quantity(self, product: Product, quantity: float):
        return product.quantity - quantity

    def add_product(self, product_name: str, quantity: float):
        product_id, product = self.check_product(product_name)
        
        if product is not None:
            product.quantity += quantity
        else:
            print(f"{product_name} is in the fridge.")
            product = Product(product_name, quantity)
            self.contents.append(product)

    def remove_product(self, product_name: str, quantity: float):
        product_name, product = self.check_product(product_name)
        
        if product is not None:
            if product.quantity >= quantity:
                product.quantity -= quantity
                if product.quantity == 0:
                    self.contents.remove(product)
            else:
                print(f"There is not {product_name} in the fridge.")
        else:
            print(f"{product_name} is not in the fridge.")

    def print_contents(self):
        print("Fridge Contents:")
        for index, product in enumerate(self.contents, start=1):
            print(f"{index} - {product.name}: {product.quantity}")

    def check_recipe(self, recipe: Recipe):
        for ingredient, quantity in recipe.ingredients:
            product_name, product = self.check_product(ingredient.name)
        if  product is None or product.quantity < quantity:
            print(f"Not enough {ingredient.name} in the fridge.")
        else:
            print(f"All recipe ingredients are in the fridge.")   
                
    def print_recipe_ingredients(self):
        if isinstance(self.ingredients, list):
            print("Recipe ingredients:")
        for ingredient, quantity in self.ingredients:
            print(f"{ingredient.name}: {quantity}")
        else:
            print("No ingredients in the recipe.")
