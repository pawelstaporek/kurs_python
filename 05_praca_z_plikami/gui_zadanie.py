"""
Utwórz proste GUI, przy pomocy którego policzymy koszt paliwa na dystansie
3 pola
dystans
spalanie
cena_1l

1 przycisk i pole na wynik


"""

import tkinter


def policz():
   dystans = entry_a.get()
   spalanie = entry_b.get()
   cena = entry_c.get()
   suma = float(dystans)/100 * float(spalanie) * float(cena)
   wynik.configure(text=f"koszt paliwa na tej trasie wynosi {suma:.2f} zł")

root = tkinter.Tk()


label_a = tkinter.Label(master=root, text="dystans [km]")
entry_a = tkinter.Entry(master=root)
label_b = tkinter.Label(master=root, text="spalanie [l/100 km]")
entry_b = tkinter.Entry(master=root)
label_c = tkinter.Label(master=root, text="cena paliwa [zł/l]")
entry_c = tkinter.Entry(master=root)
submit = tkinter.Button(master=root, text="policz", command=policz)
wynik = tkinter.Label(master=root, text="-------------------------------------------------")

label_a.grid(row=1, column=1)
entry_a.grid(row=1, column=2)
label_b.grid(row=2, column=1)
entry_b.grid(row=2, column=2)
label_c.grid(row=3, column=1)
entry_c.grid(row=3, column=2)
submit.grid(row=4, column=2)
wynik.grid(row=5, column=2)

root.mainloop()
