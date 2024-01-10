import json

class FridgeContent:
    def __init__(self, items_dict):
        self.items_dict = items_dict

    def create_fridge_content_file(self):
        file_name = 'fridge_content.json'

        with open(file_name, 'w') as file:
            json.dump(self.items_dict, file, indent=4)

    def extract_fridge_content(self):
        file_name = 'fridge_content.json'

        with open(file_name, 'r') as file:
            data = json.load(file)
            return data

# Example dictionary containing categories and items
items_dict = {
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

# Creating an instance of FridgeContent and calling methods to create the JSON file and extract its contents
fridge = FridgeContent(items_dict)
fridge.create_fridge_content_file()

# Extracting the contents of the JSON file and using it
extracted_data = fridge.extract_fridge_content()
print("Extracted data from JSON file:")
print(extracted_data)
