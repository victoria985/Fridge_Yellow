import json

class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product_name: str, quantity: float):
        product = Product(product_name, quantity)
        self.ingredients.append((product, quantity))

    def change_ingredient_quantity(self, product_name: str, new_quantity: float):
        for i, (ingredient, old_quantity) in enumerate(self.ingredients):
            if ingredient.name == product_name:
                self.ingredients[i] = (ingredient, new_quantity)
                break

    def remove_ingredient(self, product_name: str):
        self.ingredients = [(ingredient, quantity) 
        for ingredient, quantity in self.ingredients 
             if ingredient.name != product_name]

    def print_recipe_contens(self):
        if isinstance(self.ingredients, list):
            print("Recipe Ingredients:")
            for ingredient, quantity in self.ingredients:
                print(f"{ingredient.name}: {quantity}")
        else:
            print("No ingredients in the recipe.")

class Fridge:
    contents = []

    def __init__(self):
        with open('fridge.json', 'r', encoding='utf-8') as fridge_file:
          self.contents = json.load(fridge_file)

    def save(self):
        with open('fridge.json', 'w', encoding='utf-8') as fridge_file:
            json.dump(self.contents, fridge_file)

        

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

 
def main():
    fridge = Fridge()
    recipe = Recipe()

    while True:
        print('---Fridge world---')
        print('0: exit')
        print('1: Add product')
        print('2: Remove product')
        print('3: Print fridge contents')
        print('4: Check recipe')
        print('5: Add ingredients to recipe')
        print('6: Print recipe ingredients')
        choice = input('Choice 0-6: ')
        if choice == "0":
            break
        elif choice == "1":
            product_name = input('Product name: ')
            quantity = float(input('Product quantity: '))
            fridge.add_product(product_name, quantity)
        elif choice == "2": 
            product_name = input('Product name: ')
            quantity = float(input('Product quantity: '))
            fridge.remove_product(product_name, quantity) 
        elif choice == '3':
            fridge.print_contents()
        elif choice == '4':
            fridge.check_recipe(recipe)
        elif choice == '5':
            product_name = input("Product name: ")
            quantity = float(input("Product quantity: "))
            recipe.add_ingredient(product_name, quantity)
        elif choice == "6":  
            recipe.print_recipe_contens()
        else:    
            print("Bad choice, try again") 

fridge = Fridge()
fridge.add_product('milk', 1)
fridge.add_product('mayonnaise', 2)
fridge.add_product('egg', 15)
fridge.add_product('cheese', 3)

recipe = Recipe()
recipe.add_ingredient('mayonnaise', 1)
recipe.add_ingredient('cheese', 1)
recipe.add_ingredient('egg', 5)

main()

              






    


    



    # meniukas | vartotojo sasaja

# apple = Product('apple', 1)
# another_apple = Product('apple', 1)

# print(apple == another_apple)
