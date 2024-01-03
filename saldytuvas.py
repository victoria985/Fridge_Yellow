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


fridge_content = {}

def add_product(key, value = 0):
    if key in fridge_content.keys():
        fridge_content[key] = fridge_content[key] + value
        print(f'{value} of {key} has been added to the fridge.')
        print(fridge_content)
    else:
        fridge_content[key] = value
        print(f'{value} of {key} has been added to the fridge.')
        print(fridge_content)

def remove_product(name):
    
    if name in fridge_content.keys():
        print(f'Would you like to remove all {name} form the fridge?')
        condition = input('y/n: ')
        if condition.lower() == 'y':
            del fridge_content[name]
            print(f'Item {name} has been removed from the fridge')
            print(f'Fridge now has: {fridge_content}')
        elif condition.lower() == 'n':
            print(f'Type amount of {name} you would like to remove')
            r_product = input()
            fridge_content[name] = fridge_content[name] - r_product
    else:
        print('Item has not been found in the fridge, maybe you have already removed it from the fridge')

def check_product(name):
    if name in fridge_content.keys():
        print(f'{name} is in the fridge')
        print(f'There is {fridge_content[name]} of {name} in the fridge')
    else:
        print(f'Product {name} is not in the fridge')

def print_content_fridge():
    
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
    
    for key, value in recepy.items():
        if key in fridge_content:
            if recepy[key] <= fridge_content[key]:
                missing_ammount = {}
                missing_ammount[key] = recepy[key] - fridge_content[key]
            else:
                recepy_ammount = {}
                recepy_ammount[key] = recepy[key]
        else:
            missing_items = []
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
        else:
            pass

# Main function

def main(run = True):

    while run == True:

        print("Yellow Submerged Fridge")
        print("0: Exit")
        print("1: Add to the fridge")
        print("2: Remove from the fridge")
        print("3: Check for Product")
        print("4: Show conntent of the fridge")
        print("5: Recepy creation")
        choice = input("Choice: ")
        if choice == "0":
            run == False
            break
        if choice == '1':
            key = input('What product would you like to add?: ')
            value = input('Ammount of product you want to add: ')
            add_product(key, value)
        if choice == '2':
            name = input('What product would you like to remove?: ')
            remove_product(name)
        if choice == '3':
            name = input('What product you are looking for?')
            check_product(name)
        if choice == '4':
            print_content_fridge
        if choice == '5':
            recepy = input('Please write items needed for recepy: ')
            recepy_create(recepy)
        

# check test for the fridge


add_product('pienas', 1.5)
add_product('pienas', 2.3)
add_product('pomidoras', 7.58)
add_product('kiausiniai', 50)
check_product('pienas')
print_content_fridge()

main()