"""
napisz funkcję max_difference
która przyjmie listę liczb
i zwróci największą różnicę pomiędzy tymi liczbami

przykład:

    max_difference([1, 11, 9, 10, 8]) == 10
"""

def max_difference(lista):
    if lista:
        return max(lista) - min(lista)
    return 0

#print(__name__)
if __name__ == '__main__':
    print("wykonuję testy")
    assert max_difference([1, 11, 9, 10, 8]) == 10
    assert max_difference([11, 111, 9, 10, 8]) == 103
    print("jest OK")

