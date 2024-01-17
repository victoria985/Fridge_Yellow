from recipe import Recipe

class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product: Product, quantity: float ):
        self.ingredients.append((product, quantity))

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


    def print_contents(self):
        if isinstance(self.ingredients, list):
            print("Recipe Ingredients:")
        for ingredient, quantity in self.ingredients:
            print(f"{ingredient.name}: {quantity}")
        else:
            print("No ingredients in the recipe.")
