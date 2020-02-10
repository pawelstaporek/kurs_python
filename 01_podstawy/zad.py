x, y = 90, 101
if x > 100 or y > 100 or x < 0 or y < 0:
    print("poza planszą")
elif x <= 10:
    if y <= 10:
        print("LD")
    elif y < 90:
        print("LK")
    else: print("LG")
elif x < 90:
    if y <= 10:
        print("DK")
    elif y < 90:
        print("C")
    else: print("GK")
else:
    if y <= 10:
        print("PD")
    elif y < 90:
        print("LK")
    else: print("PG")
