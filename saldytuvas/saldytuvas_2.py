class Produktas:
    def __init__(self, pavadinimas:str, kiekis:float, **kwargs) -> None:
        self.pavadinimas = pavadinimas
        self.kiekis = kiekis
        self.matavimo_vienetas = 'vienetas' # galemybes: kg, g, L, ml
        for raktas, reiksme in kwargs.items():
            setattr(self, raktas, reiksme)

    def __str__(self) -> str:
        return f"{self.pavadinimas}: {self.kiekis}"
    
    def __repr__(self) -> str:
        return f"({self.pavadinimas}, {self.kiekis})"


class Receptas:
    def __init__(self):
        self.ingridientai = []
        self.instrukcijos = []

    def prideti_produktus(self, produktas: Produktas, kiekis: float):
        self.ingridientai.append((produktas, kiekis))

    def patikrinti_ingridientu_kiekius(self, ingridientu_id: int, naujas_kiekis: float):
        self.ingridientai_kiekis = naujas_kiekis

    def istraukti_ingridientus(self, ingridientu_id: int):
        self.ingridientai.pop(ingridientu_id)

    def print_turini(self):
        if self.ingridientai:
            print("Recepto ingridientai:")
            for ingridientas, kiekis in self.ingridientai:
                print(f"{ingridientas}: {kiekis}")
        else:
            print("Nera tokio ingridiento recepte")



class Saldytuvas:
    turinys = []

    def patikrinti_produkta(self, produktas_pavadinimas: str) -> Produktas:
        for produktas in self.turinys:
           if produktas.pavadinimas == produktas_pavadinimas:
            return produktas
        print(f"Produktas {produktas_pavadinimas} nerastas.")
        return None

    
    def patikrinti_produkto_kieki(self, produktas: Produktas, norimas_kiekis: float, papildomas_kiekis: float):
        if produktas.kiekis >= norimas_kiekis:
            print(f"{produktas.pavadinimas} kiekis pakankamas ({produktas.kiekis} >= {norimas_kiekis}).")
            return True
        else:
            print(f"{produktas.pavadinimas} kiekis nepakankamas ({produktas.kiekis} < {norimas_kiekis}).")

    def prideti_produkta(self, produktas_pavadinimas: str, kiekis: float):
        produktas = self.patikrinti_produkta(produktas_pavadinimas)
        if produktas is not None:
            produktas.kiekis += kiekis
            print(f"{produktas_pavadinimas} buvo saldytuve, bet pridėjome dar {kiekis} daugiau.")
        else:
            naujas_produktas = Produktas(produktas_pavadinimas, kiekis)
            self.turinys.append(naujas_produktas)
            print(f"{naujas_produktas.pavadinimas}, {kiekis} buvo pridėtas į saldytuvą.")


    def print_saldytuvo_turini(self):
        for indeksas, eilute in enumerate(self.turinys):
            print(f"{indeksas} - {eilute}")


    def istraukti_produktus(self, isimamas_produktas: str, kiekis: float):
        produkto_id, isimamas_produktas = self.isimamas_produktas(isimamas_produktas)
        if isimamas_produktas is not None:
           if kiekis > 0:
              self.turinys[produkto_id]['kiekis'] -= kiekis
              if self.turinys[produkto_id]['kiekis'] <= 0:
                 self.turinys.pop(produkto_id)
              else:
                  print(f"{isimamas_produktas} kiekis sumažintas: {kiekis}")
           else:
                print("Kiekis turi būti didesnis už 0.")
        else:
          print(f"Produktas {isimamas_produktas} nerastas.")

            
    def print_turini(self):
            print("Saldytuvo turinys:")
            for produktas in self.turinys:                   
                print(produktas)

    def patikrinti_recepto_ingridientus(self, esami_ingridientai: Receptas):
        visi_ingridientai_prieinami = True
        for ingridientas, kiekis in esami_ingridientai.ingridientai:
            esamas_ingridientas = self.patikrinti_produkta(ingridientas.pavadinimas)[1]
            if esamas_ingridientas is None or esamas_ingridientas.kiekis < kiekis:
                visi_ingridientai_prieinami = False
                break
        if visi_ingridientai_prieinami:
            print("Pakankamas kiekis ingredientų recepto gaminimui.")
        else:
            print("Nepakankamas kiekis šių ingredientų saldytuve.")            


    def recepto_turinys(self, turinys):
        if self.turinys:
            print('---Receptas---')       
            for ingridientas, kiekis in self.turinys:
                print(f"{ingridientas['produktas']}: {kiekis['kiekis']}")
        else:
            print("Recepte nera siu ingridientu.")
                
        
   
def main():
    saldytuvas = Saldytuvas()
    receptas = Receptas()

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
              






    


    



    # meniukas | vartotojo sasaja

# apple = Product('apple', 1)
# another_apple = Product('apple', 1)

# print(apple == another_apple)
