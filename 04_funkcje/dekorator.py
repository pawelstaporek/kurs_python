import time

def zmierz_czas(func):

    def wrapper(*arcs, **kwargs):
        start = time.time()
        result = func(*arcs, **kwargs)
        print(f"czas wykonania {func.__name__}: ",time.time() - start)
        return result
    
    return wrapper

def dane():
    return [i for i in range(100000)]

dane = zmierz_czas(dane)

@zmierz_czas
def do_kwadratu(lista):
    return [x**2 for x in lista]

#do_kwadratu = zmierz_czas(do_kwadratu) -> równoważne @zmierz_czas na górze

d = dane()

do_kwadratu(d)

dane()

