"""
napisz program który w podanym przez użytkownika napisie zliczy liczbę wystąpień każdego znaku

np:

"ala ma kota" -> ('a':4, 'l':1...)

"""

napis = input("podaj zdanie: ")


liczniki = {}
for znak in napis:
    liczniki[znak] = liczniki.get(znak, 0) + 1

print(liczniki)

#####

import collections

liczniki = collections.defaultdict(int)

##albo:

from collections import defaultdict

liczniki = defaultdict(int)


for znak in napis:
    liczniki[znak] += 1
