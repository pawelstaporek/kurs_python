"""
napisz program, który będzie przyjmował od użytkownika liczby (input)
Jeśli wpiszemy k - to zakończy działanie pętli i wypisze średnią z podanych liczb

"""
i, s = 0, 0


while True:
    wartosc = input('podaj liczbę lub "k" aby zakończyć: ')
    if wartosc == 'k':
        break
    i += 1
    s += int(wartosc)

print(f'Średnia wartość to: {s/i:.2f}')