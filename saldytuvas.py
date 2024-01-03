""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* User inputo, terminalo meniu, iseiga.
* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float). Yra
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais. Yra
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas. Yra
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve. Yra
* Išspausdinti visą šaldytuvo turinį su kiekiais. Reikia

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
*** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""


def add_product(fridge_content, product, quantity = 0):
    if product in fridge_content.keys():
        fridge_content[product] = fridge_content[product] + quantity
        print(f'{quantity} of {product} has been added to the fridge.')
        print(fridge_content)
    else:
        fridge_content[product] = quantity
        print(f'{quantity} of {product} has been added to the fridge.')
        print(fridge_content)
    
    return fridge_content

def remove_product(fridge_content, name):
    
    if name in fridge_content.keys():
        print(f'Would you like to remove all {name} form the fridge?')
        condition = input('y/n: ')
        if condition.lower() == 'y':
            del fridge_content[name]
            print(f'Item {name} has been removed from the fridge')
            print(f'Fridge now has: {fridge_content}')
        elif condition.lower() == 'n':
            print(f'Type amount of {name} you would like to remove')
            r_product = float(input())
            fridge_content[name] = fridge_content[name] - r_product
            print(f'{r_product} {name} has been removed from the fridge')
    else:
        print('Item has not been found in the fridge, maybe you have already removed it from the fridge')
    
    return fridge_content

def check_product(fridge_content, name):
    if name in fridge_content.keys():
        print(f'{name} is in the fridge')
        print(f'There is {fridge_content[name]} of {name} in the fridge')
    else:
        print(f'Product {name} is not in the fridge')

def print_content_fridge(fridge_content):
    
    for key, value in fridge_content.items():
        print(f'* {key} : {value}')

# Bonus tasks

def recepy_create(input_string):
    recepy = {}    
    pairs = input_string.split(',')
    
    for pair in pairs:
        key_value = pair.strip().split(':')
        
        if len(key_value) == 2:
            key = key_value[0].strip()
            value = key_value[1].strip()
            
            try:
                recepy[key] = float(value)
            except ValueError:
                recepy[key] = value  
        else:
            print(f"Ignoring invalid pair: {pair}")
    
    print('Recepy has beed created:')
    for key in recepy:
        print(f'{key} : {recepy[key]}')
    
    return recepy
    

def check_recepy(fridge_content, recepy):
    
    missing_ammount = {}
    recepy_ammount = {}
    missing_items = []

    for key, value in recepy.items():
        if key in fridge_content:
            if recepy[key] <= fridge_content[key]:
                missing_ammount[key] = recepy[key] - fridge_content[key]
            else:
                recepy_ammount[key] = recepy[key]
        else:
            missing_items.append(key)
    
    if missing_ammount == {} and missing_items == []:
        print('Recepy has all ingreadients in the fridge')
        return recepy_ammount
    else:
        if missing_items != []:
            print('Products that are not in the fridge:')
            for i in missing_items:
                print(f'*** {i}')
        if missing_ammount != {}:
            print('Products that are nor enough in the fridge:')
            for key, value in missing_ammount.items():
                print(f'*** {key}: {value}')

# Main function

def main(fridge_content):

    while True:


        print("Yellow Submerged Fridge")
        print("0: Exit")
        print("1: Add to the fridge")
        print("2: Remove from the fridge")
        print("3: Check for Product")
        print("4: Show conntent of the fridge")
        print("5: Recepy creation")
        print("6: Recepy check")
        choice = input("Choice: ")
        if choice == "0":
            break
        if choice == '1':
            product = input('What product would you like to add?: ')
            quantity = float(input('Ammount of product you want to add: '))
            fridge_content = add_product(fridge_content, product, quantity)
        if choice == '2':
            name = input('What product would you like to remove?: ')
            fridge_content = remove_product(fridge_content, name)
        if choice == '3':
            name = input('What product you are looking for?')
            check_product(fridge_content, name)
        if choice == '4':
            print_content_fridge(fridge_content)
        if choice == '5':
            recepy_input = input('Please write items needed for recepy: ')
            recepy = recepy_create(recepy_input)
        if choice == '6':
            check_recepy(fridge_content, recepy)
        

# check test for the fridge

fridge_content = {}
print(fridge_content)

fridge_content = add_product(fridge_content, 'pienas', 1.5)
fridge_content = add_product(fridge_content, 'pienas', 2.3)
fridge_content = add_product(fridge_content, 'pomidoras', 7.58)
fridge_content = add_product(fridge_content, 'kiausiniai', 50)
check_product(fridge_content, 'pienas')
print_content_fridge(fridge_content)

main(fridge_content)