from tkinter import *

main_window = Tk()
main_window.title("A téglatest adatai")
main_window.geometry("300x100")

def ujablak():
    window2 = Toplevel(main_window)
    window2.geometry("300x100")
    
    felszin_szoveg = Label(window2, text="Felszín:")
    felszin_szoveg.grid(row=0)
    felszin = Entry(window2)
    felszin.grid(row=0, column=1)

    terfogat_szoveg = Label(window2, text="Térfogat:")
    terfogat_szoveg.grid(row=1)
    terfogat = Entry(window2)
    terfogat.grid(row=1, column=1)

    a = int(a_input.get())
    b = int(b_input.get())
    c = int(c_input.get())

    teglatest_felszine = 2*(a*b+a*c+b*c)
    teglatest_terfogata = a*b*c

    felszin.delete(0, END)
    terfogat.delete(0, END)
    felszin.insert(0, teglatest_felszine)
    terfogat.insert(0, teglatest_terfogata)

    felszin.configure(state="readonly")
    terfogat.configure(state="readonly")

    window2.mainloop()

a_szoveg = Label(main_window, text="a:")
a_szoveg.grid(row=0)

a_input = Entry(main_window)
a_input.grid(row=0, column=1)

b_szoveg = Label(main_window, text="b:")
b_szoveg.grid(row=1)

b_input = Entry(main_window)
b_input.grid(row=1, column=1)

c_szoveg = Label(main_window, text="c:")
c_szoveg.grid(row=2)

c_input = Entry(main_window)
c_input.grid(row=2, column=1)

szamitas_gomb = Button(main_window, text="Számítás", command=ujablak)
szamitas_gomb.grid(row=3, column=1)

main_window.mainloop()