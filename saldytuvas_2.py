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
    ingridientai = []
    instrukcijos = []

    def prideti_produktus(self, produktas: Produktas, kiekis: float ):
        self.ingridientai.append((produktas, kiekis))

    def patikrinti_ingridientu_kiekius(self, ingridientu_id: int, naujas_kiekis: float):
        self.ingridientai[ingridientu_id].kiekis = naujas_kiekis

    def istraukti_ingridientus(self, ingridientu_id: int):
        self.ingridientai.pop(ingridientu_id)


    def print_turini(self):
        if isinstance(self.ingridientai, list):
            print("Recepto ingridientai:")
        for ingridientas, kiekis in self.ingridientai:
            print(f"{ingridientas}: {kiekis}")
        else:
            print("Nera tokio ingridiento recepte")



class Saldytuvas:
    turinys = []

    def patikrinti_produkta(self, produktas: str) -> (int, Produktas):
        for produkto_id, produktas in enumerate(self.turinys):
         if produktas == produktas:
          return produkto_id, produktas
         else:
          return None, None
    
    def patikrinti_produkto_kieki(self, produktas: Produktas, kiekis: float):
        return produktas.kiekis - kiekis

    def prideti_produkta(self, produktas: str, kiekis: float):
        produktas = self.patikrinti_produkta(produktas) 
        if produktas is not None:
            self.turinys[produktas][kiekis] += kiekis
            print(f"{produktas} buvo saldytuve, bet pridejome dar {kiekis} daugiau.")
        else:
            self.turinys.append(Produktas(produktas, kiekis))
            print(f"{produktas}, {kiekis} buvo pridetas i saldytuva.")

    def print_saldytuvo_turini(self):
        for indeksas, eilute in enumerate(self.turinys, pradzia = 1):
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

        for ingridientas, kiekis in esami_ingridientai.items():
            esamas_ingridientas = self.esami_ingridientas(ingridientas)
            if  esamas_ingridientas is None or esamas_ingridientas['kiekis'] < kiekis:
                 visi_ingridientai_prieinami = False
                 break

        if visi_ingridientai_prieinami:
            print(f"Pakankamas kiekis ingredientų recepto gaminimui.")
        else:
            print(f"Nepakankamas kiekis šių ingredientų saldytuve.")
                
        
   
def main():
    saldytuvas = Saldytuvas()
    receptas = Receptas()

    while True:
        print('---Saldytuvas---')
        print('0: iseiti is programos')
        print('1: prideti produktus')
        print('2: isimti produktus ')
        print('3: pasirinkti produkta')
        print('4: pasirinkti kieki')
        print('5: saldytuvo turinys')
        print('6: pasirinkti recepta')
        choice = input('Choice 0-6')
        if choice == "0":
           break
        elif choice == "1":
            produktas = input('Pridetas produktas:')
            kiekis = float(input('Prideto produkto kiekis:'))
            saldytuvas.prideti_produktus(produktas, kiekis)
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
             kiekis = input('Produkto kiekis:')
             kiekis = saldytuvas.patikrinti_produkto_kieki(kiekis)
             if kiekis is not None:
                print(f'{produktas} {kiekis}')
             else:
                print(f'{produktas} nerastas šaldytuve')
        elif choice == "5":   
                print('Saldytuvo turinys')
                saldytuvas.print_saldytuvo_turini()    
        elif choice == "6":  
             saldytuvas.patikrinti_recepto_ingridientus(receptas)
        else:
                print("Bad choice, try again") 


saldytuvas = Saldytuvas()
saldytuvas.prideti_produkta('pienas', 1)
saldytuvas.prideti_produkta('majonezas', 2)
saldytuvas.prideti_produkta('kiausiniai', 15)
saldytuvas.prideti_produkta('suris', 3)

receptas = Receptas()
receptas.ingridientai(Produktas('majonezas', 1), 1)
receptas.ingridientai(Produktas('suris', 1), 1)
receptas.ingridientai(Produktas('kiausiniai', 5), 1)

main()                     
              






    


    



    # meniukas | vartotojo sasaja

# apple = Product('apple', 1)
# another_apple = Product('apple', 1)

# print(apple == another_apple)
