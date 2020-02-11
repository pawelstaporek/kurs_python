"""
range(0, 101, 2)
Napisz program, który będzie zliczał liczbę unikalnych liczb wprowadzanych przez użytkownika.
Zliczanie kończy się gdy użytkownik wpisze "k". W podsumowaniu napisz jak dużo z podanych liczb to
liczby parzyste z zakresy od 0 do 200

len()

"""
a = set()
while True:
    z = input("Wprowadź liczbę lub 'k' aby zakończyć: ")
    if z == "k":
        break
    else:
        a.add(int(z))

print(f"Wprowadzono {len(a)} unikalnych liczb.")

print(f"{len(a & set(range(0, 201, 2)))} z nich to liczby parzyste z zakresu od 0 do 200")