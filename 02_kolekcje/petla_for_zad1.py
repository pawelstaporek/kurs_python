"""
mamy zadaną listę:
np [1, 2, 3, -6, 5, 7, -8, 9, 12, 34]

zliczyć liczby dodatnie i liczby ujemne.
wypisz osobne sumy liczb dodatnich i ujemnych

"""

lista = [1, 2, 3, -6, 5, 7, -8, 9, 12, 34]

ujemne = 0
dodatnie = 0
suma_ujemne = 0
Suma_dodatnie = 0

for el in lista:
    if el < 0:
        ujemne += 1
        suma_ujemne += el
    else:
        dodatnie += 1
        Suma_dodatnie += el

print(f"""
ujemnych: {ujemne}, suma: {suma_ujemne}
dodatnich: {dodatnie}, suma: {Suma_dodatnie}
""")