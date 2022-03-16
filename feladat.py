from tkinter import *

window = Tk()

elso_mezo = Label(window, text="Első mező:")
elso_mezo.grid(row=0, column=0)

elso_input = Entry(window)
elso_input.grid(row=0, column=1)

masodik_mezo = Label(window, text="Második mező:")
masodik_mezo.grid(row=1, column=0)

masodik_input = Entry(window)
masodik_input.grid(row=1, column=1)

harmadik_mezo = Label(window, text="Harmadik mező:")
harmadik_mezo.grid(row=2, column=0)

harmadik_input = Entry(window)
harmadik_input.grid(row=2, column=1)

window.mainloop()