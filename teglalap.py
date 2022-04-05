from tkinter import *
bekeres = Tk()

def adatok():
    kiiratas = Tk()

    terfogatszoveg = Label(kiiratas, text = "Térfogat (cm3): ")
    terfogatszoveg.grid(column = 0, row = 0)
    terfogat = Entry(kiiratas)
    terfogat.grid(column = 1, row = 0)

    felszinszoveg = Label(kiiratas, text = "Felszín (cm2): ")
    felszinszoveg.grid(column = 0, row = 1)
    felszin = Entry(kiiratas)
    felszin.grid(column = 1, row = 1)

    Aadat = int(A.get())
    Badat = int(B.get())
    Cadat = int(C.get())

    terfogatszamitas = Aadat * Badat * Cadat
    terfogat.insert(0, terfogatszamitas)

    felszinszamitas = 2 * (Aadat * Badat) * (Aadat * Cadat) * (Badat * Cadat) / 100
    felszin.insert(0, felszinszamitas)

    kiiratas.mainloop()


#szövegek
cim = Label(text = "Téglalap számítások", width = 20, height = 2)
cim.grid(column = 1, row = 0)

Aoldal = Label(text = "A:")
Aoldal.grid(column= 0, row = 2)

Boldal = Label(text = "B:")
Boldal.grid(column= 0, row = 3)

Coldal = Label(text = "C:")
Coldal.grid(column= 0, row = 4)

#bekeres

A = Entry()
A.grid(column = 1, row = 2)

B = Entry()
B.grid(column = 1, row = 3)

C = Entry()
C.grid(column = 1, row = 4)


#gomb

kiszamit = Button(text = "Kiszámítás",  command = adatok)
kiszamit.grid(column = 1, row = 5)

bekeres.mainloop()