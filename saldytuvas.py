""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""


fridge_content = {}

def add_product(key, value = 0):

    fridge_content[key] = value
    print(fridge_content)

def remove_product(name):
    
    if name in fridge_content.keys():
        del fridge_content[name]
        print(f'Item {name} has been removed from the fridge')
        print(f'Fridge now has: {fridge_content}')
    else:
        print('Item has not been found in the fridge, please try again')

def check_product(name):
    if name in fridge_content.keys():
        print(f'{name} is in the fridge')
        print(f'There is {fridge_content[name]} of {name} in the fridge')
    else:
        print(f'Product {name} is not in the fridge')

def print_content_fridge():
    
    for key, value in fridge_content:
        print(f'{key} :    {value}')

recepy = 0

def check_recepy():
    pass

def input_recepy():
    pass

def recepy_fail():
    pass


# check test for the fridge

add_product('pienas', 1.5)
add_product('pomidoras', 7.58)
check_product('pienas')
remove_product('pienas')
print_content_fridge()
print(recepy)
check_recepy()
input_recepy()
recepy_fail()