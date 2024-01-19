import os
import pickle
from saldytuvas_2 import Saldytuvas
from saldytuvas_2 import Receptas


SALDYTUVO_FAILAS = "saldytuvas.pkl"


def load_saldytuvas(SALDYTUVO_FAILAS = SALDYTUVO_FAILAS):
    if os.path.exists(SALDYTUVO_FAILAS):
        with open(SALDYTUVO_FAILAS, 'rb') as file:
            return pickle.load(file)
    else:
        return Saldytuvas()
    
def save_fridge(saldytuvas, SALDYTUVO_FAILAS = SALDYTUVO_FAILAS):
    with open(SALDYTUVO_FAILAS, 'wb') as file:
        pickle.dump(saldytuvas, file)

def main():
    saldytuvas = Saldytuvas()
    receptas = Receptas()
    saldytuvas = load_saldytuvas()

    while True:
        print('---Saldytuvas---')
        print('0: iseiti is programos')
        print('1: prideti produktus')
        print('2: isimti produktus ')
        print('3: patikrinti produkta ar yra saldytuve')
        print('4: prideti produkta i recepta')
        print('5: saldytuvo turinys')
        print('6: pasirinkti recepta')
        print('7: recepto turinys')
        choice = input('Choice 0-7')
        if choice == "0":
           save_fridge(saldytuvas)
           break
        elif choice == "1":
            produktas = input('Pridetas produktas:')
            kiekis = float(input('Prideto produkto kiekis:'))
            saldytuvas.prideti_produkta(produktas, kiekis)
        elif choice == "2": 
             produktas = input('Išimtas produktas:')
             kiekis= float(input('Išimto produkto kiekis:'))
             saldytuvas.istraukti_produktus(produktas, kiekis) 
        elif choice == "3": 
             produktas = input('Produkto pavadinimas:')
             produktas = saldytuvas.patikrinti_produkta(produktas)
             if produktas is not None:
                  print(f'{produktas} yra šaldytuve')
             else:
                  print(f'{produktas} nerastas šaldytuve') 
        elif choice == "4": 
             produktas = input('Produkto pavadinimas:')
             kiekis = float(input('Prideto produkto kiekis:'))
             receptas.prideti_produktus(produktas, kiekis)
        elif choice == "5":   
                print('Saldytuvo turinys')
                saldytuvas.print_saldytuvo_turini()    
        elif choice == "6":  
             produktas = input('Produkto pavadinimas:')
             kiekis = float(input('Prideto produkto kiekis:'))
             receptas.patikrinti_ingridientu_kiekius(produktas, kiekis)
        elif choice == "7":
                print('Recepto turinys')
                receptas.print_turini()    
        else:
                print("Bad choice, try again") 


saldytuvas = Saldytuvas()
saldytuvas.prideti_produkta('milk', 1.0)
saldytuvas.prideti_produkta('majonezas', 2.0)
saldytuvas.prideti_produkta('kiausiniai', 15.0)
saldytuvas.prideti_produkta('suris', 3.0)

receptas = Receptas()
receptas.prideti_produktus('majonezas', 1.0)
receptas.prideti_produktus('suris', 1.0)
receptas.prideti_produktus('kiausiniai', 5.0)

main()                     
              