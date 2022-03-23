from tkinter import *
from math import pi
from tkinter import messagebox

def szamitas():
    try:
        vas_suruseg = 7.8
        fa_suruseg = 0.70
        sugara = int(sugar.get())
        magassaga = int(magassag.get())
        vegeredmeny = pi * sugara * sugara * magassaga
        terfogat.delete(0, END)
        vashenger.delete(0, END)
        fahenger.delete(0, END)
        terfogat.insert(0, "{:.2f}".format(vegeredmeny) + " cm3")
        vashenger_tomeg = vas_suruseg * vegeredmeny
        vashenger.insert(0, "{:.2f}".format(vashenger_tomeg) + " g")
        fahenger_tomeg = fa_suruseg * vegeredmeny
        fahenger.insert(0, "{:.2f}".format(fahenger_tomeg) + " g")
    except:
        messagebox.showerror("Hiba!", "Csak számot adj meg!")


window = Tk()
window.title("Henger")

sugar_szoveg = Label(window, text="Sugár (cm):")
sugar_szoveg.grid(row=0, column=0)

sugar = Entry(window)
sugar.grid(row=0, column=1)

magassag_szoveg = Label(window, text="Magasság (cm):")
magassag_szoveg.grid(row=1, column=0)

magassag = Entry(window)
magassag.grid(row=1, column=1)

szamol_gomb = Button(window, text="Kiszámít", command=szamitas)
szamol_gomb.grid(row=3, column=1)

terfogat_szoveg = Label(window, text="Térfogat:")
terfogat_szoveg.grid(row=4, column=0)

terfogat = Entry(window)
terfogat.grid(row=4, column=1)

vashenger_szoveg = Label(window, text="Vashenger:")
vashenger_szoveg.grid(row=5, column=0)

vashenger = Entry(window)
vashenger.grid(row=5, column=1)

fahenger_szoveg = Label(window, text="Fahenger:")
fahenger_szoveg.grid(row=6, column=0)

fahenger = Entry(window)
fahenger.grid(row=6, column=1)

window.mainloop()