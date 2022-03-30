from tkinter import *
ablak = Tk()

cimke1 = Label(ablak, text = "Első mező:")
cimke1.grid(column = 0, row = 0)

mezo1 = Entry(ablak)
mezo1.grid(column = 1, row = 0)

cimke2 = Label(ablak, text = "Második:")
cimke2.grid(column = 0, row = 1)

mezo2 = Entry(ablak)
mezo2.grid(column = 1, row = 1)

cimke3 = Label(ablak, text = "Harmadik:")
cimke3.grid(column = 0, row = 2)

mezo3 = Entry(ablak)
mezo3.grid(column = 1, row = 2)

can = Canvas(ablak, width = 160, height = 160, bg = "white")
photo = PhotoImage(file = "H:\IKT Projekt munka\Python\Kepek\lightbulb-gif-7.gif")
item = can.create_image(250, 250, image = photo)
can.grid(column = 3, row = 1)



ablak.mainloop()