import os
import time

# Importing the classes from the main code
from classy_fridge import Product, Recipe, SmartFridge

# Prefix for test files
test_prefix = 'test_'

def run_tests():
    try:
        # Test parameters
        fridge = SmartFridge()
        print("Testing SmartFridge class...")
        time.sleep(0.5)

        # Test Product class
        print("\nTesting Product class...")
        milk = Product('milk', 20, 'l', 'dairy')
        print(milk)
        time.sleep(0.5)

        # Test Recipe class
        print("\nTesting Recipe class...")
        recipe_dict = {
            'apple': [5, 'pieces', 'fruits'],
            'milk': [1, 'liter', 'dairy'],
            'cheese': [500, 'grams', 'dairy'],
            'bread': [1, 'loaf', 'bakery'],
        }
        new_recipe = Recipe(recipe_dict)
        print(new_recipe.ingredients)
        time.sleep(0.5)

        # Test SmartFridge class
        print("\nTesting SmartFridge class...")
        fridge.get_user_input = lambda: ('TestUser', '1234')  # Mocking user input
        extracted_content = fridge.main()
        fridge.print_contents()
        time.sleep(0.5)

        # All tests passed
        print("\nAll tests passed!")

    finally:
        # Delete test files
        for filename in os.listdir():
            if filename.startswith(test_prefix):
                os.remove(filename)

# Run the tests
run_tests()








productas(name, value, categorija)


productas(name) # value = 0, cuategory = ''