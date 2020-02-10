"""
z podanych w pętli liczb, wybierz największą i najmniejszą
k kończy pętlę

x = None
"""

max = None
min = None

while True:
    x = input('podaj liczbę lub "k" aby zakończyć: ')
    if x == 'k':
        break
    x = int(x)
    if max is None or max < x:
        max = x
    if min is None or min > x:
        min = x
print(f'Maksymalna wartość to: {max}. Minimalna wartość to: {min}')