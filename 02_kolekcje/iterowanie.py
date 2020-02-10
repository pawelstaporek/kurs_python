lista = [10, 20, 30, 40, 50]

i = 0
while i < len(lista):
    print(lista[i])
    i += 1

print("-" * 40)

for el in lista:
    print(el)

print("-" * 40)

for i, el in enumerate(lista):
    print(i, el)