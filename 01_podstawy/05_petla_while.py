
i = 0
while i < 10:
    if i  == 5:
        i += 1
        continue
    print(i)
    i += 1

i = 35
while True:
    i += 1
    if i % 17 == 0:
        print(i)
        break