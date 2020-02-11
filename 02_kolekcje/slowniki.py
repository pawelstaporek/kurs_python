slownik = {
    #"klucz": "wartosc" "key" : "value"
    "kot": "cat",
    "pies": "dog",
    "ptak": "bird"}

print(dir(slownik))

print(slownik.keys())
print(slownik.values())
print(slownik.items())

pary = ((1, "a"), (2,"b"))
d = dict(pary)

print(d)   

d3 = dict(ala="kot", ola="pies")
print(d3)
d3.update(d)
print(d3)

for klucz in d3:
    print(klucz)

for klucz, wartosc in d3.items():
    print(klucz, wartosc)

print("a" in d3) #domyślnie wśród kluczy

#zaleta słownika - czas dostępu taki sam - nie przeszukuje całej listy

#print(d3["a"])
print(d3.get("a", "N/A"))

if "a" in d3:
    print(d3["a"])
else:
    print("N/A")