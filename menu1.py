from tkinter import *
from tkinter import messagebox
from math import pi

def nevjegy():
    ablak2 = Toplevel(foablak)
    szoveg2 = Label(ablak2, text="Készítette: Simon Valentin\n2022.04.06", width=20)
    kilepes = Button(ablak2, text="Kilépés", command=ablak2.destroy)
    szoveg2.pack()
    kilepes.pack()
    ablak2.mainloop()

def felszin():
    def szamitas():
        a = int(a_input.get())
        b = int(b_input.get())
        c = int(c_input.get())

        if a <= 0:
            messagebox.showerror("Hiba!", "Ne adj meg mínuszt, vagy 0-át. Megértését köszönjük!")
        elif b <= 0:
            messagebox.showerror("Hiba!", "Ne adj meg mínuszt, vagy 0-át. Megértését köszönjük!")
        elif c <= 0:
            messagebox.showerror("Hiba!", "Ne adj meg mínuszt, vagy 0-át. Megértését köszönjük!")
        else:
            teglatest_felszine = 2*(a*b+a*c+b*c)

            eredmeny_jelzo.configure(state=NORMAL)
            eredmeny_jelzo.delete(0, END)
            eredmeny_jelzo.insert(0, teglatest_felszine)
            eredmeny_jelzo.configure(state='readonly')

    felszin_ablak = Toplevel(foablak)
    felszin_ablak.title("A téglatest felszíne")

    a_szoveg = Label(felszin_ablak, text="a:")
    a_szoveg.grid(row=0)

    a_input = Entry(felszin_ablak)
    a_input.grid(row=0, column=1)

    b_szoveg = Label(felszin_ablak, text="b:")
    b_szoveg.grid(row=1)

    b_input = Entry(felszin_ablak)
    b_input.grid(row=1, column=1)

    c_szoveg = Label(felszin_ablak, text="c:")
    c_szoveg.grid(row=2)

    c_input = Entry(felszin_ablak)
    c_input.grid(row=2, column=1)

    szamitas_gomb = Button(felszin_ablak, text="Számítás", command=szamitas)
    szamitas_gomb.grid(row=3, column=1)

    eredmeny = Label(felszin_ablak, text="Eredmény:")
    eredmeny.grid(row=4)

    eredmeny_jelzo = Entry(felszin_ablak, state='readonly')
    eredmeny_jelzo.grid(row=4, column=1)

    kilepes_gomb = Button(felszin_ablak, text="Kilépés", command=felszin_ablak.destroy)
    kilepes_gomb.grid(row=5, column=1)

    felszin_ablak.mainloop()

def terfogat():
    def szamitas():
        a = int(a_input.get())
        b = int(b_input.get())
        c = int(c_input.get())

        if a <= 0:
            messagebox.showerror("Hiba!", "Ne adj meg mínuszt, vagy 0-át. Megértését köszönjük!")
        elif b <= 0:
            messagebox.showerror("Hiba!", "Ne adj meg mínuszt, vagy 0-át. Megértését köszönjük!")
        elif c <= 0:
            messagebox.showerror("Hiba!", "Ne adj meg mínuszt, vagy 0-át. Megértését köszönjük!")
        else:
            teglatest_terfogata = a*b*c

            eredmeny_jelzo.configure(state=NORMAL)
            eredmeny_jelzo.delete(0, END)
            eredmeny_jelzo.insert(0, teglatest_terfogata)
            eredmeny_jelzo.configure(state='readonly')

    terfogat_ablak = Toplevel(foablak)
    terfogat_ablak.title("A téglatest térfogata")

    a_szoveg = Label(terfogat_ablak, text="a:")
    a_szoveg.grid(row=0)

    a_input = Entry(terfogat_ablak)
    a_input.grid(row=0, column=1)

    b_szoveg = Label(terfogat_ablak, text="b:")
    b_szoveg.grid(row=1)

    b_input = Entry(terfogat_ablak)
    b_input.grid(row=1, column=1)

    c_szoveg = Label(terfogat_ablak, text="c:")
    c_szoveg.grid(row=2)

    c_input = Entry(terfogat_ablak)
    c_input.grid(row=2, column=1)

    szamitas_gomb = Button(terfogat_ablak, text="Számítás", command=szamitas)
    szamitas_gomb.grid(row=3, column=1)

    eredmeny = Label(terfogat_ablak, text="Eredmény:")
    eredmeny.grid(row=4)

    eredmeny_jelzo = Entry(terfogat_ablak, state='readonly')
    eredmeny_jelzo.grid(row=4, column=1)

    kilepes_gomb = Button(terfogat_ablak, text="Kilépés", command=terfogat_ablak.destroy)
    kilepes_gomb.grid(row=5, column=1)

    terfogat_ablak.mainloop()

def henger_felszin():   #2*π*r(r+h)
    def szamitas():
        sugara = int(sugara_bemenet.get())
        magassaga = int(magassag_bemenet.get())
        
        if sugara <= 0 or magassaga <= 0:
            messagebox.showerror("Hiba!", "Ne adj meg 0-át, vagy mínuszos számot!")
        else:
            felszine = 2*pi*sugara*(sugara+magassaga)

            eredmeny_jelzo.configure(state=NORMAL)
            eredmeny_jelzo.delete(0, END)
            eredmeny_jelzo.insert(0, "{:.2f}".format(felszine) + " cm3")
            eredmeny_jelzo.configure(state="readonly")

    henger_felszin_ablak = Toplevel(foablak)
    henger_felszin_ablak.title("Henger felszíne")

    sugara_text = Label(henger_felszin_ablak, text="Henger sugara: ")
    sugara_text.grid(row=0)

    sugara_bemenet = Entry(henger_felszin_ablak)
    sugara_bemenet.grid(row=0, column=1)

    magassag_szoveg = Label(henger_felszin_ablak, text="Magassága:")
    magassag_szoveg.grid(row=1, column=0)

    magassag_bemenet = Entry(henger_felszin_ablak)
    magassag_bemenet.grid(row=1, column=1)

    szamol = Button(henger_felszin_ablak, text="Számol", command=szamitas)
    szamol.grid(row=2, column=1)

    eredmeny = Label(henger_felszin_ablak, text="Eredmény:")
    eredmeny.grid(row=4)

    eredmeny_jelzo = Entry(henger_felszin_ablak, state='readonly')
    eredmeny_jelzo.grid(row=4, column=1)

    kilepes_gomb = Button(henger_felszin_ablak, text="Kilépés", command=henger_felszin_ablak.destroy)
    kilepes_gomb.grid(row=5, column=1)

    henger_felszin_ablak.mainloop()

def henger_terfogat():
    def szamitas():
        sugara = int(sugara_bemenet.get())
        magassaga = int(magassag_bemenet.get())
        
        if sugara <= 0 or magassaga <= 0:
            messagebox.showerror("Hiba!", "Ne adj meg 0-át, vagy mínuszos számot!")
        else:
            terfogata = pi * sugara * sugara * magassaga

            eredmeny_jelzo.configure(state=NORMAL)
            eredmeny_jelzo.delete(0, END)
            eredmeny_jelzo.insert(0, "{:.2f}".format(terfogata) + " cm3")
            eredmeny_jelzo.configure(state="readonly")

    henger_terfogat_ablak = Toplevel(foablak)
    henger_terfogat_ablak.title("Henger térfogata")

    sugara_text = Label(henger_terfogat_ablak, text="Henger sugara: ")
    sugara_text.grid(row=0)

    sugara_bemenet = Entry(henger_terfogat_ablak)
    sugara_bemenet.grid(row=0, column=1)

    magassag_szoveg = Label(henger_terfogat_ablak, text="Magassága:")
    magassag_szoveg.grid(row=1, column=0)

    magassag_bemenet = Entry(henger_terfogat_ablak)
    magassag_bemenet.grid(row=1, column=1)

    szamol = Button(henger_terfogat_ablak, text="Számol", command=szamitas)
    szamol.grid(row=2, column=1)

    eredmeny = Label(henger_terfogat_ablak, text="Eredmény:")
    eredmeny.grid(row=4)

    eredmeny_jelzo = Entry(henger_terfogat_ablak, state='readonly')
    eredmeny_jelzo.grid(row=4, column=1)

    kilepes_gomb = Button(henger_terfogat_ablak, text="Kilépés", command=henger_terfogat_ablak.destroy)
    kilepes_gomb.grid(row=5, column=1)

    henger_terfogat_ablak.mainloop()

foablak = Tk()
foablak.title("Főablak")
foablak.geometry('300x50')

menusor = Frame(foablak)
menusor.pack(side=TOP, fill=X)

menu1 = Menubutton(menusor, text="Fájl", underline=0)
menu1.pack(side=LEFT)
fajl = Menu(menu1)
fajl.add_command(label='Névjegy', command=nevjegy, underline=0)
fajl.add_command(label='Bezárás', command=foablak.destroy, underline=0)
menu1.config(menu=fajl)

menu2 = Menubutton(menusor, text='Téglatest', underline=0)
menu2.pack(side=LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label='Felszín', command=felszin, underline=0)
teglatest.add_command(label='Térfogat', command=terfogat, underline=0)
menu2.config(menu=teglatest)

menu3 = Menubutton(menusor, text="Henger", underline=0)
menu3.pack(side=LEFT)
henger = Menu(menu3)
henger.add_command(label='Felszín', command=henger_felszin, underline=0)
henger.add_command(label='Térfogat', command=henger_terfogat, underline=0)
menu3.config(menu=henger)

foablak.mainloop()