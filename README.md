![](smart_fridge_gif.gif)

Naujas protingas geltonas šaldytuvas (Release 1.00)

Pagrindinės šaldytuvo užduotys:

1) Turėti atmintyje userio informacija, ty, user_name, pin_kodas.
2) Tvarkyti šaldytuvo turini.
3) Struktūringai pateikti šaldytuvo turinį pagal kategorijas, kategorijų apibrėžimai (matavimo vienetai, laikymo salygos)
4) Receptų kūrimas, jų laikymas pagal pavadinimą, spausdinimas receptų su galimu jų aprašymu, receptų trinimas, automatinis gaminimo būklė (kai yra išimami arba visi produktai arba po vieną, bonusas jeigu pagal receptūra)
5) Valymo funkcija



Old version:

$${\color{yellow}Šaldytuvas}$$


Šaldytuvas yra pythono programa, kuri veikia terminale:

Instaliavimas:

Instaliavimui užtanka parsisiunti kodą paleisti jį naudojant bet kokį python interpretatoriu

Šaldytuvas naudoja python 3.12 versiją

Pagrindinės Šaldytuvo funkcijos:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Produkto įdėjimas į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Produkto išimimas iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

Recepto kūrimas:

* Galima kurti recepta pagal kurį yra tikrinama šaldytuvo turinys.
* Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
* Jeigu receptas neišeina, išvardina kiek ir kokių produktų trūksta.

Bonus:

* Yra programos testavimas, reikia įvesti test terminale
