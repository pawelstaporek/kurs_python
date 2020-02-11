"""
stwórz tabliczkę mnożenia - listę list
dla liczb od 1 do 10
zrób to przy pomocy pętli
powtórz przy pomocy wyrazenia listowego

"""
tabliczka = []

for i in range(1,11):
    row = []
    for j in range(1,11):
        row.append(i * j)
    tabliczka.append(row)
print (tabliczka)

tablica = [[i*j for j in range(1,11)] for i in range (1,11)]
print(tablica)

print(tabliczka==tablica)