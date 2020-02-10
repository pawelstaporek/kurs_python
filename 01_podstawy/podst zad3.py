"""
- pobierz napis od użytkownika - funkcja input
- wypisz długość napisu
- zmień napis na liczbę - co gdy się nie da?
- wypisz kwadrat tej liczby
"""

x = input("podaj x: ")
print("Długość:", len(x))
print("Długość {}".format(len(x)))
print(f"Długość {len(x)}")
#ask for permission
if x.isnumeric():
    print("kwadrat x to", int(x) ** 2)
# beg for forgiveness
try:
    liczba = int(x)
except ValueError:
    pass
print("Koniec")