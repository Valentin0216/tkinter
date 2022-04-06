from tkinter import *

ablak = Tk()

def ujablak():
    ablak2 = Toplevel(ablak)
    szoveg2 = Label(ablak2, text="Készítette: Simon Valentin\n2022.04.06", width=20)
    kilepes = Button(ablak2, text="Kilépés", command=ablak2.destroy)
    szoveg2.pack()
    kilepes.pack()
    ablak2.mainloop()

szoveg = Label(ablak, text="Kattints a gombra!")
gomb = Button(ablak, text="Névjegy", command=ujablak)

szoveg.pack()
gomb.pack()

ablak.mainloop()