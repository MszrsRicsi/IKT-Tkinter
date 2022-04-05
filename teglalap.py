from tkinter import *
bekeres = Tk()

def adatok():
    kiiratas = Tk()

    felszinszoveg = Label(kiiratas, text = "Felszín: ")
    felszinszoveg.grid(column = 0, row = 1)
    felszin = Entry(kiiratas)
    felszin.grid(column = 1, row = 1)

    terfogatszoveg = Label(kiiratas, text = "Térfogat: ")
    terfogatszoveg.grid(column = 0, row = 0)
    terfogat = Entry(kiiratas)
    terfogat.grid(column = 1, row = 0)

    Aadat = int(A.get())
    Badat = int(B.get())
    Cadat = int(C.get())

    terfogatszamitas = Aadat * Badat * Cadat
    terfogat.insert(terfogatszamitas)




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