class Czlowiek:

    gatunek = "homo sapiens"
    def __init__(self, imie):
        self.imie = imie
    @property #sprawia że nie trzeba dodawać wywołania funkcji ()
    def dlugosc_imienia(self):
        return len(self.imie)

    def __str__(self):
        return f"<Osoba {self.imie}>"

c1 = Czlowiek("Rafał")
c2 = Czlowiek("Paweł")
print(type(c1))

print(c1.imie)
print(c2.imie)
print(c2.gatunek)

Czlowiek.gatunek = "homo erectus"
print(c2.gatunek)
print(c2.dlugosc_imienia)

print(c1)