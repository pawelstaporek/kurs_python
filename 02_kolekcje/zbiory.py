
a = {3, 2, 31}
b = set([3, 4, 5])

c = {1,1,1,2,2,3,3,3}
c.add(4) #doda 4 do zbioru. nie ma tu kolejności
print(c)
print(a | b) #suma zbiorów
print(a - b) #różnica zbiorów
print(a & b) #część wspólna zbiorów, iloczyn
print(a ^ b) #różnica symetryczna. są w a lub b ale nie w ich iloczynie

print(set([1, 1, 2, 2, 3]))
print(set((1, 1, 2, 2, 3)))
print(set("Ala ma kota burego"))

print(set({"a": 1, "b": 2}))