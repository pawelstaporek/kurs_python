"""
w zadanej liście zamień element najmniejszy z największym
"""

lista = [10, 1, 3, 17, 4, 8, 25, 2]

index_max = 0
index_min = 0
value_max = max(lista)
value_min = min(lista)

for i, el in enumerate(lista):
    if value_max == el:
        index_max = i
    if value_min == el:
        index_min = i
print(f"max: {index_max} value {value_max} min: {index_min} value {value_min}")

lista[index_max] = value_min
lista[index_min] = value_max

assert lista == [10, 25, 3, 17, 4, 8, 1, 2]