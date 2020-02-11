"""
napisz program, który:
- wypisze dostępne produkty (oraz ich ceny). Produkty te powinny się znajdować w słowniku
- na podstawie dialogu z użytkownikiem wylicz cenę za wybrany towar

np.:

Oferujemy:

<lista produktów>: <cena> PLN

co chcesz kupić? ziemniaki
ile chcesz kupić (ziemniaki)? 5

do zapłaty: x PLN
"""

slownik = {
    "pomidory": 8.99,
    "ziemniaki": 3.20,
    "jabłka": 3,
    "banany": 4}

magazyn = {
    "pomidory": 10,
    "ziemniaki": 10,
    "jabłka": 10,
    "banany": 10}


while True:
    opcja = input("Zakup [z] czy magazyn [m], koniec [k]: ")
    if opcja == "k":
        break
    elif opcja == "z":
        print("Oferujemy: ")
        for towar, cena in slownik.items():
            #print(towar+" po "+str(cena)+" PLN")
            print(f' - {towar} w cenie: {cena} PLN/kg')
        print()

        zakup = input("Co chcesz kupić?: ")
        ilosc = float(input("Ile kg chcesz kupić?: "))
        cena_za_kg = slownik.get(zakup)
        #if suma is None
        if not cena_za_kg:
            print("Nie mamy takiego produktu")
        else:
            if magazyn.get(zakup) >= ilosc:
                suma = cena_za_kg * ilosc
                print(f"do zapłaty: {float(suma)} PLN")
                magazyn[zakup] = magazyn.get(zakup) - ilosc
            else:
                print(f'Niestety mamy tylko {magazyn.get(zakup)} kg {zakup}')
    elif opcja == 'm':
        towar = input("Co przywiozłeś?: ")
        ilosc = int(input("Ile kg przywiozłeś?: "))
        if towar in magazyn:
            magazyn[towar] += ilosc
        else:
            cena = float(input("Jaka jest cena? [PLN/kg]: "))
            magazyn[towar] = ilosc
            slownik[towar] = cena
        print(f"Pomyślnie dodatko {ilosc} kg {towar}'ów")

#for klucz 

#input