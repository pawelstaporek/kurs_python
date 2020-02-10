"""
Korzystając z pętli while wypisz dla 100 pierwszych liczb parzystych tę liczbę, jej kwadrat i sześcian
Zrób krok co 1.
Jeśli liczba jest równa 33 to też ją wypisz
"""

i = 0

while i < 201:
    i += 1
    if i % 2 == 0 or i == 33:
        print(f'{i:7} {i**2:7} {i**3:9}')
        #continue
