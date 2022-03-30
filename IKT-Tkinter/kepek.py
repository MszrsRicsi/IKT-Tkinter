from tkinter import *
ablak1 = Tk()
def click():
    print("Clickeltem")
gyoker = "H:\\IKT Projekt munka\\Python\\Kepek\\"
ablak1.geometry("600x600")
ablak1.title("IKT Tkinter")
icon = PhotoImage(file = gyoker+"pineapple.png")
ablak1.iconphoto(True, icon)
ablak1.config(background = "black")
kep = PhotoImage(file = gyoker+"homokora.png")
cimke = Label(ablak1,
                text = "Üdvözlet!",
                fg = "#423434",
                bg = "#976562",
                font = ("Arial", 45, "bold"),
                bd = 10,
                relief = RAISED,
                padx = 25,
                pady = 30,
                image = kep,
                compound = "bottom"
            ).pack()

gomb = Button(ablak1,
            text = "Kattints!",
            font = 20,
            fg = "blue",
            bg = "yellow",
            padx = 20,
            pady = 20,
            command = click,
            activebackground = "green",
            activeforeground = "yellow",
            state = ACTIVE
            ).pack()

ablak1.mainloop()