#utwórz listę zawierającą liczbę i jej sześcian z zakresu od 0 do 100
#jeżeli liczby są podzielne przez 5
liczby = []

for i in range(101):
    if i % 5 == 0:
        liczby.append([i, i**3])

liczby = [[i, i**3] for i in range(101) if i % 5 == 0]


print(liczby)

#utworzyć słownik który zawiera takie pary

liczby = {i: i**3 for i in range(101) if i % 5 == 0}
print(liczby)

kolekcja = (i for i in range(10))
print(kolekcja)
print(tuple(kolekcja))