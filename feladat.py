from tkinter import *

window = Tk()
window.title("Feladat")

kep = "villanykorte.png"

elso_mezo = Label(window, text="Első mező:")
elso_mezo.grid(row=0, column=0, pady=5)

elso_input = Entry(window)
elso_input.grid(row=0, column=1)

masodik_mezo = Label(window, text="Második mező:")
masodik_mezo.grid(row=1, column=0, pady=5)

masodik_input = Entry(window)
masodik_input.grid(row=1, column=1)

harmadik_mezo = Label(window, text="Harmadik mező:")
harmadik_mezo.grid(row=2, column=0, pady=5)

harmadik_input = Entry(window)
harmadik_input.grid(row=2, column=1)

villanykorte = PhotoImage(file="villanykorte.png")

canvas = Canvas(window, width=150, height=150)
canvas.grid(row=0, column=2, rowspan=3)

canvas.create_image(150, 150,image=villanykorte, anchor=SE)

# kep = Label(window, image=villanykorte)
# kep.grid(row=0, column=2, rowspan=3)

window.mainloop()