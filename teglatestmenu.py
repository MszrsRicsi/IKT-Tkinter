from tkinter import *
foablak = Tk()


#névjegy

def nevjegyablak():
    nevjegy = Tk()
    
    uzenet = Message(nevjegy, text = "Készítette: Valaki \n 2022.04.05", width = 300)
    uzenet.grid(column = 1, row = 1)

    gomb2 = Button(nevjegy, text = "Kilépés", command = nevjegy.destroy)
    gomb2.grid(column = 1, row = 6)

    nevjegy.mainloop()


#térfogat számítás

def terfogatszamitas():
    terfogatablak = Tk()

    terfogatszoveg = Label(terfogatablak, text = "Térfogat (cm3): ")
    terfogatszoveg.grid(column = 0, row = 0)
    terfogat = Entry(terfogatablak)
    terfogat.grid(column = 1, row = 0)

    A = Entry(terfogatablak)
    A.grid(column = 1, row = 2)

    B = Entry(terfogatablak)
    B.grid(column = 1, row = 3)

    C = Entry(terfogatablak)
    C.grid(column = 1, row = 4)

    kiszamit = Button(terfogatablak, text = "Kiszámítás", command = szamitas)
    kiszamit.grid(column = 1, row = 5)

    eredmeny = Entry(terfogatablak)
    eredmeny.grid(column = 1, row = 6)

    def szamitas():
        Aadat = int(A.get())
        Badat = int(B.get())
        Cadat = int(C.get())
        terfogatkiszamitas = Aadat * Badat * Cadat
        terfogat.insert(0, terfogatkiszamitas)



    terfogatablak.mainloop()


#felszín számítás

def felszinszamitas():
    felszinablak = Tk()
    felszinszoveg = Label(felszinablak, text = "Felszín (cm2): ")
    felszinszoveg.grid(column = 0, row = 1)
    felszin = Entry(felszinablak)
    felszin.grid(column = 1, row = 1)

    A = Entry(felszinablak)
    A.grid(column = 1, row = 2)

    B = Entry(felszinablak)
    B.grid(column = 1, row = 3)

    C = Entry(felszinablak)
    C.grid(column = 1, row = 4)



    Aadat = int(A.get())
    Badat = int(B.get())
    Cadat = int(C.get())

    felszinkiszamitas = 2 * (Aadat * Badat) * (Aadat * Cadat) * (Badat * Cadat) / 100
    felszin.insert(0, felszinkiszamitas)

    kiszamit = Button(felszinablak, text = "Kiszámítás")
    kiszamit.grid(column = 1, row = 5)

    felszin.mainloop()


#főablak

foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)

menu1 = Menubutton(menusor, text = "Fájl", underline = 0)
menu1.pack(side = LEFT)
fajl = Menu(menu1)
fajl.add_command(label = "Névjegy", command = nevjegyablak, underline = 0)
fajl.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu1.config(menu = fajl)

menu2 = Menubutton(menusor, text = "Téglatest", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszin", command = felszinszamitas, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogatszamitas, underline = 0)
menu2.config(menu = teglatest)



foablak.mainloop()