#-*-coding:utf-8-*-
from Tkinter import *
import random

cam=Tk()

cam.title("ŞANS OYUNU")
cam.geometry("250x250+15+15")
cam.tk_setPalette("#ffcccc")

yazi=Label(text="ŞANSLI SAYILARINIZ",fg="darkblue",font="Arial 15 bold")
yazi.pack()

yazi2=Label(fg="darkblue",font="Arial 15 bold")
yazi2.pack()

liste=[]

def bas():
    global liste
    for i in range(6):
        while len(liste)!=6:
            a=random.randint(1,100)
            if a not in liste:
                liste.append(a)


    

    yazi2["text"]=liste

def yeniden():
    for i in liste:
        liste.remove(i)
    bas()
    
yazi2=Label(fg="darkblue",font="Arial 15 bold")
yazi2.pack()




dugme=Button(text="BAŞLA",bg="white",fg="#660066",font="Helvatica 12 bold",
             command=bas)
dugme.pack(expand=YES)

dugme=Button(text="YENİDEN",bg="white",fg="#660066",font="Helvatica 12 bold",
             command=yeniden)
dugme.pack(expand=YES)

dugme2=Button(text="ÇIK",bg="white",fg="#660066",font="Helvatica 12 bold",
              command=cam.destroy)
dugme2.pack(expand=YES)



mainloop()
