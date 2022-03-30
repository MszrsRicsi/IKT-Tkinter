from tkinter import *
ablak = Tk()

def kiszamit():
    r = int(sugarmezo.get())
    m = int(magassagmezo.get())
    pi = 3.1415926535
    V = (r * r) * pi * m
    terfogatmezo.delete(0, END)
    terfogatmezo.insert(0, str(round(V, 2)) +str(" cm3"))

    qvas = 7.874
    vashengertomeg = round(qvas * V, 2)
    vashengermezo.delete(0, END)
    vashengermezo.insert(0, str(vashengertomeg) + str(" g"))

    qfa = 0.7
    fahengertomeg = round(qfa * V, 2)
    fahengermezo.delete(0, END)
    fahengermezo.insert(0, str(fahengertomeg) + str(" g"))



sugar = Label(ablak, text = "Sugár (cm)")
sugar.grid(column = 0, row = 0)
magassag = Label(ablak, text = "Magasság (cm)")
magassag.grid(column = 0, row = 1)

sugarmezo = Entry(ablak)
sugarmezo.grid(column = 1, row = 0)
magassagmezo = Entry(ablak)
magassagmezo.grid(column = 1, row = 1)

kiszamitgomb = Button(ablak, text = "Kiszámít", command = kiszamit)
kiszamitgomb.grid(column = 1, row = 3)

terfogat = Label(ablak, text = "Térfogat:")
terfogat.grid(column = 0, row = 4)
vashenger = Label(ablak, text = "Vashenger:")
vashenger.grid(column = 0, row = 5)
fahenger = Label(ablak, text = "Fahenger")
fahenger.grid(column = 0, row = 6)

terfogatmezo = Entry(ablak)
terfogatmezo.grid(column = 1, row = 4)
vashengermezo = Entry(ablak)
vashengermezo.grid(column = 1, row = 5)
fahengermezo = Entry(ablak)
fahengermezo.grid(column = 1, row = 6)

ablak.mainloop()