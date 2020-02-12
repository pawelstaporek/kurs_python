import csv
import matplotlib.pyplot as plt
import pandas as pd

with open("log.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')

    czas_ostatniego_zalogowania = dict()
    czas_przebywania_w_systemie = dict()
    for row in reader:
        login = row[0]
        akcja = row[1]
        czas = row[2]
        if akcja == "LOGIN":
            czas_ostatniego_zalogowania[login] = int(czas)
        elif akcja == "LOGOUT":
            czas_przebywania_w_systemie[login] = (czas_przebywania_w_systemie.get(login,0) + int(czas) - czas_ostatniego_zalogowania[login])
        

wyniki = sorted(czas_przebywania_w_systemie.items(), key=lambda x: x[1], reverse=True)

df = pd.DataFrame(wyniki)
df.columns = ["login", "time"]
df.plot(kind="bar")
plt.show()

# print(df)
# df.to_excel("czas.xlsx", index=False, header=False)

with open("wyniki.csv", "w", newline="") as outcsv:
    writer = csv.writer(outcsv, delimiter=";")
    #for row in wyniki:
    #    writer.writerow(row)
    writer.writerows(wyniki)