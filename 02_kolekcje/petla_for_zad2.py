"""
napisz program który wypisze tabliczkę mnożenia NxN

Np. N=3

    0 1 2 3
    
  0 0 0 0 0
  1 0 1 2 3
  2 0 2 4 6
  3 0 3 6 9

list(range(100))
range(1, 30, 5)
for i in range(1, 30, 5)
print("A", end="")
print("B")
print("C")
"""

#N = input("podaj N: ")
#N = int(N)
#listax = list(range(0, N+1, 1))
#listay = list(range(0, N+1, 1))

#for el in listax:
#    for i in listay:
#        print(f'{el*i:5}', end="")
#    print()

N = 10

print(" ", end="")

for i in range(N+1):
    print(f"{i:4}", end="")

print()
print()

for i in range(N+1):
    print(i, end="")
    for j in range(N+1):
        print(f"{i*j:4}", end="")
    print()

    