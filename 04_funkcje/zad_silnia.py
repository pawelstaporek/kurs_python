"""
Napisz funkcję silnia która rekurencyjne policzy silnie dla zadanej liczby

5! = 5 * 4! = 5 * 4 * 3!
"""
def silnia(n):
    if n <= 1:
        return 1
    else:
        return n * silnia(n-1)

print(silnia(0))