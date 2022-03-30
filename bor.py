from tkinter import *
import math
ablak = Tk()

def belefer():
    pi = math.pi
    r = float(hordosugar.get())
    m = float(hordomagassag.get())
    b = float(borunk.get())

    if b > 0 and r > 0 and m > 0:
        V = float((r * r) * pi * m)
        Vdm3 = float(V / 1000)
        szazalek = (b / Vdm3) * 1000
        if szazalek <= 100:
            eredmeny.delete(0, END)
            eredmeny.insert(0, "Eddig van teli:  " +str(round(szazalek, 2)) +str("%"))
        elif szazalek > 100:
            eredmeny.delete(0, END)
            eredmeny.insert(0, "Nem fér bele")
    else:
        eredmeny.delete(0, END)
        eredmeny.insert(0, "Érvénytelen szám: 0")

    

hordomagker = Label(text = "Hordó magassága (cm):  ")
hordomagker.grid(column = 0, row = 0)
hordomagassag = Entry()
hordomagassag.grid(column = 1, row = 0)

hordosugker = Label(text = "Hordó sugara (cm): ")
hordosugker.grid(column = 0, row = 1)
hordosugar = Entry()
hordosugar.grid(column = 1, row = 1)

borkerdes = Label(text = "Mennyi bor van? (l)")
borkerdes.grid(column = 0, row = 4)
borunk = Entry()
borunk.grid(column = 1, row = 4)

belefergomb = Button(text = "Belefér?", command = belefer)
belefergomb.grid(column = 1, row = 6)

eredmeny = Entry()
eredmeny.grid(column = 1, row = 7)


ablak.mainloop()