from tkinter import *


#névjegy

def nevjegy():
    abl2 = Toplevel(foablak)
    uz2 = Message(abl2, text = "Készítette: Mészáros Richárd")
    gomb2 = Button(abl2, text = "Kilép", command = abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()


#felszín

def felszin():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        if a > 0 and b > 0 and c > 0:
            felszin = 2*(a*b+a*c+b*c)
            mezo4.delete(0, END)
            mezo4.insert(0,str(felszin))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, "Nem jó adat! (x < 0)")
    
    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)
        mezo3.delete(0, END)
        mezo4.delete(0, END)

    abl3 = Toplevel(foablak)
    abl3.title("Téglatest felszíne")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    
    gomb1 = Button(abl3, text = "Számít", command= szamit)

    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    
    gomb1.grid(row = 4, column = 2, sticky = W)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)

    felszinkilep = Button(abl3, text = "Kilépés", command = abl3.destroy)
    felszinkilep.grid(row = 6, column = 3, sticky = W)

    felszin_adattorles = Button(abl3, text = "Törlés", command = torles)
    felszin_adattorles.grid(row = 6, column = 1, sticky = W)
    
    abl3.mainloop()


#térfogat

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        if a > 0 and b > 0 and c > 0:
            terfogat = a*b*c
            mezo4.delete(0, END)
            mezo4.insert(0,str(terfogat))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, "Nem jó adat! (x < 0)")

    def torles():
        mezo1.delete(0, END)
        mezo2.delete(0, END)
        mezo3.delete(0, END)
        mezo4.delete(0, END)

    abl4 = Toplevel(foablak)
    abl4.title("Téglatest térfogata")
    abl4.minsize(width = 300, height = 100)
    szoveg1 = Label(abl4, text = "a:")
    szoveg2 = Label(abl4, text = "b:")
    szoveg3 = Label(abl4, text = "c:")
    szoveg4 = Label(abl4, text = "Eredmény:")
    
    gomb1 = Button(abl4, text = "Számít", command= szamit)

    mezo1 = Entry(abl4)
    mezo2 = Entry(abl4)
    mezo3 = Entry(abl4)
    mezo4 = Entry(abl4)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    
    gomb1.grid(row = 4, column = 2, sticky = W)

    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)

    terfogatkilep = Button(abl4, text = "Kilépés", command = abl4.destroy)
    terfogatkilep.grid(row = 6, column = 3, sticky = W)

    terfogat_adattorles = Button(abl4, text = "Törlés", command = torles)
    terfogat_adattorles.grid(row = 6, column = 1, sticky = W)
    
    abl4.mainloop()


#foablak

foablak = Tk()
foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side= TOP, fill = X)

menu1 = Menubutton(menusor, text = "Fájl", underline = 0)
menu1.pack(side = LEFT)
fajl = Menu(menu1)
fajl.add_command(label = "Névjegy", command = nevjegy, underline = 0)
fajl.add_command(label = "Kiépés", command = foablak.destroy, underline = 0)
menu1.config(menu = fajl)

menu2 = Menubutton(menusor, text = "Téglatest", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
menu2.config(menu = teglatest)

gomb3 = Button(foablak, text = "Kilépés", command = foablak.destroy)
gomb3.pack(side = BOTTOM)

foablak.mainloop()