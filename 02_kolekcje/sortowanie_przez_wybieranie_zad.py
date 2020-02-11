"""

napisz program, który posortuje liczby w liście przy pomocy algorytmu
Sortowanie przez wybieranie
"""

lista = [9,1,6,8,4,3,2,0]

for i, eli in enumerate(lista):
    for j, elj in enumerate(lista):
        if eli < elj:
            lista[i], lista[j] = lista[j], lista[i]
        j += 1
    i += 1
print(lista)

for indeks_poczatku in range(len(lista)):
    indeks_min = indeks_poczatku
    for i in range(indeks_poczatku + 1, len(lista)):
        if lista[i] < lista[indeks_min]:
            indeks_min = 1
    lista[indeks_poczatku], lista[indeks_min] = lista[indeks_min], lista[indeks_poczatku]

assert lista == [0, 1, 2, 3, 4, 6, 8, 9]