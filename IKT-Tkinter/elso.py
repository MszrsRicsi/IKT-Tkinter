from tkinter import *
import math
foablak = Tk()
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: " +str(c))

def kivonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a - b
    mezo3.delete(0, END)
    mezo3.insert(0, "Különbség: " +str(c))

def szorzas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a * b
    mezo3.delete(0, END)
    mezo3.insert(0, "Szorzat: " +str(c))

def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    if a or b == 0:
        mezo3.delete(0, END)
        mezo3.insert(0, "0-val nem osztható!")
    c = a / b
    mezo3.delete(0, END)
    mezo3.insert(0, "Eredmény: " +str(c))


def oszthatoe():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a % b
    if c == 0:
        mezo3.delete(0, END)
        mezo3.insert(0, "Osztható")
    else:
        mezo3.delete(0, END)
        mezo3.insert(0, "Nem osztható")
def negyzet():
    a = int(mezo1.get())
    c = a * a
    mezo3.delete(0, END)
    mezo3.insert(0, "Négyzete: " +str(c))

def gyok():
    a = int(mezo1.get())
    if a <= 0:
        mezo3.delete(0, END)
        mezo3.insert(0, "A szám < 0")
    c = math.sqrt(a)
    mezo3.delete(0, END)
    mezo3.insert(0, "A győke: " +str(c))

cimke = Label(foablak, text = "Üdvözlet", fg = "red")
cimke.grid(column = 1, row = 1)
cimke1 = Label(foablak, text = "Első mező:")
cimke1.grid(column = 0, row = 2)
cimke2 = Label(foablak, text = "Második mező:")
cimke2.grid(column = 0, row = 3)
gomb3 = Button(foablak, text = "Kilépés", command = foablak.destroy)
gomb3.grid(column = 5, row = 15)
mezo1 = Entry(foablak)
mezo1.grid(column = 1, row = 2)
mezo2 = Entry(foablak)
mezo2.grid(column = 1, row = 3)
gomb4 = Button(foablak, text = "Összead", command = osszeg)
gomb4.grid(column = 1, row = 4)
gomb5 = Button(foablak, text = "Kivonás", command = kivonas)
gomb5.grid(column = 1, row = 5)
gomb6 = Button(foablak, text = "Szorzás", command = szorzas)
gomb6.grid(column = 1, row = 6)
gomb7 = Button(foablak, text = "Osztás", command = osztas)
gomb7.grid(column = 1, row = 7)
gomb8 = Button(foablak, text = "Osztható maradék nélkül?", command = oszthatoe)
gomb8.grid(column = 1, row = 8)
gomb8 = Button(foablak, text = "Négyzetre emelés", command = negyzet)
gomb8.grid(column = 1, row = 9)
gomb9 = Button(foablak, text = "Gyökvonás", command = gyok)
gomb9.grid(column = 1, row = 10)
mezo3 = Entry(foablak)
mezo3.grid(column = 1, row = 12)


can1 = Canvas(foablak, width = 500, height = 500, bg = "white")
photo = PhotoImage(file = "H:\IKT Projekt munka\Python\Kepek\lightbulb-gif-7.gif")
item = can1.create_image(250, 250, image = photo)
can1.grid(column = 1, row = 20)

foablak.mainloop()