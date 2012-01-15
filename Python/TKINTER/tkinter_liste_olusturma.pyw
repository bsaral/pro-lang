# -*- coding: cp1254 -*-

from Tkinter import *

pencere=Tk()
pencere.title("LISTEM")

liste_pen=Listbox(bg="#ffcc99",fg="black",font="Arial 15 bold")
liste_pen.pack()

bosluk=Frame()
bosluk.pack(pady=5)

giris=Entry(bg="#66ccff",fg="black",width=30)
giris.pack(side=TOP,expand=YES)



def ekle():
    liste_pen.insert(END,giris.get())
    giris.delete(0,END)

def sil():
    liste_pen.delete(ACTIVE)

bosluk=Frame()
bosluk.pack(pady=5)

dugme=Button(pencere,text="YAZDIR",command=ekle)
dugme.pack(side=LEFT,expand=YES)

dugme2=Button(pencere,text="TEMIZLE",command=sil)
dugme2.pack(side=RIGHT,expand=YES)
    






mainloop()
