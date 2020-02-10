moja_lista = list()
moja_lista = [1, 2, 3, 4, 5, 6, 'a']
#print(dir(moja_lista))

#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

moja_lista.append(10)
print(moja_lista)

x = [1, 2, 3]
y = x
x.append(5)
print(x,y)

y = x[:]
y = x.copy()

z = [1, 2]
x = [1, 2, z]

print(x)

y = x.copy()
print(y)

z.append(4)
print(x, y)

import copy

y = copy.deepcopy(x)
print(y)

z.append(4)
print(x, y)

x = (4, 12, 1, 100, -6)
print(max(x))
print(min(x))
print(sum(x))