"""
z podanych w pętli liczb, wybierz największą i najmniejszą
k kończy pętlę

x = None
"""

max_ = None
min_ = None

while True:
    x = input('podaj liczbę lub "k" aby zakończyć: ')
    if x == 'k':
        break
    x = int(x)
    if max_ is None or max_ < x:
        max_ = x
    if min_ is None or min_ > x:
        min_ = x
print(f'Maksymalna wartość to: {max_}. Minimalna wartość to: {min_}')