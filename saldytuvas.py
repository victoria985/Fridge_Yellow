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
        del fridge_content[name]
        print(f'Item {name} has been removed from the fridge')
        print(f'Fridge now has: {fridge_content}')
    else:
        print('Item has not been found in the fridge, maybe you have already removed it from the fridge')

def check_product(name):
    if name in fridge_content.keys():
        print(f'{name} is in the fridge')
        print(f'There is {fridge_content[name]} of {name} in the fridge')
    else:
        print(f'Product {name} is not in the fridge')

def print_content_fridge():
    
    print(fridge_content)

# Bonus tasks

recepy = 0

def check_recepy():
    pass

def input_recepy():
    pass

def recepy_fail():
    pass

# Main function

def main():
    while True:
        print("Yellow Submerged Fridge")
        print("0: Exit")
        print("1: Add to the fridge")
        print("2: Remove from the fridge")
        print("2: Add a task")
        print('3: Mark task done/undone')
        print("4: Remove a task")
        choice = input("Choice: ")
        if choice == "0":
            break
        if choice == '1':
            key = input('What product would you like to add?: ')
            value = input('Ammount of product you want to add: ')
            add_product(key, value)
        if choice == '2':
            name = input('What product would you like to remove?: ')
            remove_product(name)

        
        

# check test for the fridge


add_product('pienas', 1.5)
add_product('pienas', 2.3)
add_product('pomidoras', 7.58)
add_product('kiausiniai', 50)
check_product('pienas')
remove_product('pienas')
print_content_fridge()
print(recepy)
check_recepy()
input_recepy()
recepy_fail()