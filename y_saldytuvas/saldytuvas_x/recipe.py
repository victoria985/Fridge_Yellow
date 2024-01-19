from product import Product

class Recipe:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, name: str, quantity: float):
        product = Product(name, quantity)
        self.ingredients.append((product, quantity))

    def change_ingredient_quantity(self, name: str, new_quantity: float):
        for i, (ingredient, old_quantity) in enumerate(self.ingredients):
            if ingredient.name == name:
                self.ingredients[i] = (ingredient, new_quantity)
                break

    def remove_ingredient(self, name: str):
        self.ingredients = [
            (ingredient, quantity) for ingredient, quantity in self.ingredients
            if ingredient.name != name
        ]

    def print_recipe_contents(self):
        if self.ingredients:
            print("Recipe Ingredients:")
            for ingredient, quantity in self.ingredients:
                print(f"{ingredient.name}: {quantity}")
        else:
            print("No ingredients in the recipe.")