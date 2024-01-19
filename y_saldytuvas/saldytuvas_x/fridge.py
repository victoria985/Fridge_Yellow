from product import Product
from recipe import Recipe
import json


class Fridge:
    def __init__(self):
        try:
            with open('fridge.json', 'r', encoding='utf-8') as fridge_file:
                self.contents = json.load(fridge_file)
        except FileNotFoundError:
            self.contents = []

    def save(self):
        with open('fridge.json', 'w', encoding='utf-8') as fridge_file:
            json.dump(self.contents, fridge_file)

    def check_product(self, name: str):
        for product in self.contents:
            if product['name'] == name:
                return product
        return None

    def check_product_quantity(self, product, quantity: float):
        return product['quantity'] - quantity

    def add_product(self, name: str, quantity: float):
        product = self.check_product(name)

        if product is not None:
            product['quantity'] += quantity
        else:
            print(f"{name} is not in the fridge.")
            product = {'name': name, 'quantity': quantity}
            self.contents.append(product)

    def remove_product(self, name: str, quantity: float):
        product = self.check_product(name)

        if product is not None:
            if product['quantity'] >= quantity:
                product['quantity'] -= quantity
                if product['quantity'] == 0:
                    self.contents.remove(product)
            else:
                print(f"Not enough {name} in the fridge.")
        else:
            print(f"{name} is not in the fridge.")

    def print_contents(self):
        print("Fridge Contents:")
        for product in self.contents:
            print(f"{product['name']}: {product['quantity']}")

    def check_recipe(self, recipe: Recipe):
        for ingredient, quantity in recipe.ingredients:
            product = self.check_product(ingredient.name)
            if product is None or product['quantity'] < quantity:
                print(f"Not enough {ingredient.name} in the fridge.")
                return
        print("All recipe ingredients are in the fridge.")

    def print_recipe_ingredients(self):
        if self.contents:
            print("Recipe ingredients:")
            for ingredient, quantity in self.contents:
                print(f"{ingredient['name']}: {ingredient['quantity']}")
        else:
            print("No ingredients in the recipe.")
