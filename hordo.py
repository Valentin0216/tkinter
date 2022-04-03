'''
Van egy henger alakú hordónk, melybe nem tudjuk, hogy belefér-e a rendelkezésre
álló bor. Kérd be a bor mennyiségét literben, majd a hordó összes szükséges adatát cmben.
Adj tájékoztatást, hogy hány literes a hordó, és hogy belefér-e a hordóba a bor! Ha
belefér, akkor add meg, hogy mennyi férne még bele! Írd ki százalékosan is a
telítettséget! Az adatokat egészre kerekítve írd ki!
'''
from dis import disassemble
from gzip import READ
from tkinter import *
from math import pi
from tkinter.messagebox import showerror, showinfo

def szamitas():
    try:
        hordod_litere_liter.configure(state=NORMAL)
        hordod_litere_liter.delete(0, END)
        r = kor_sugara.get()
        r = int(r)
        m = henger_magassaga.get()
        m = int(m)
        bekert_liter = bor_mennyiseg.get()
        bekert_liter = int(bekert_liter)
        alapkor_terulete = r*r*pi
        cm3_terfogata = alapkor_terulete*m
        dm3 = cm3_terfogata / 1000
        hordo_liter = dm3
        hordo_liter = round(hordo_liter, 0)
        hordo_liter = int(hordo_liter)
        hordod_litere_liter.insert(0, "{:.0f}".format(hordo_liter) + " literes!")
        hordod_litere_liter.configure(state="readonly")
        if bekert_liter > hordo_liter:
            showerror("Hiba!", "Nem fér a hordóba ez a mennyiség!")
        else:
            belefer_meg = hordo_liter - bekert_liter
            szazalek = 100 / hordo_liter * belefer_meg
            showinfo("Belefér!", f"Belefér a hordóba a megadott mennyiség! Ezen kívül marad még {belefer_meg} liter szabadon! (A hordó {szazalek}%-a üres!)")
    except:
        showerror("Hiba!", "Csak számokat adj meg, és minden mezőbe írj valamit!")

window = Tk()
window.title("Hordó")

bor_mennyiseg_szoveg = Label(window, text="Bor mennyisége (literben):")
bor_mennyiseg_szoveg.grid(row=0, column=0)

bor_mennyiseg = Entry(window)
bor_mennyiseg.grid(row=0, column=1)

kor_sugara_szoveg = Label(window, text="Kör sugara (cm-ben):")
kor_sugara_szoveg.grid(row=1, column=0)

kor_sugara = Entry(window)
kor_sugara.grid(row=1, column=1)

henger_magassaga_szoveg = Label(window, text="Magasság (cm-ben):")
henger_magassaga_szoveg.grid(row=2, column=0)

henger_magassaga = Entry(window)
henger_magassaga.grid(row=2, column=1)

szamitas_gomb = Button(window, text="Számítás!", command=lambda:szamitas())
szamitas_gomb.grid(row=3, column=1)

hordod_litere = Label(window, text="A te hordód: ")
hordod_litere.grid(row=4, column=0)

hordod_litere_liter = Entry(window, state=DISABLED)
hordod_litere_liter.grid(row=4, column=1)

window.mainloop()