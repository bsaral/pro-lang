#-*-coding:utf-8-*-
from __future__ import division
from Tkinter import *
from tkMessageBox import *
import math

win=Tk()
win.title("HESAP MAKİNAM")
win.geometry("350x300+50+15")
win.resizable(width=FALSE, height=FALSE)
win.tk_setPalette("#cccccc")

pen=Entry(bg="#ffffcc",fg="#333333",font="Helvatica 15 bold",width=8)
pen.pack()
pen.place(relx=0.02, rely=0.2)
pen.focus_set()

liste=Listbox(bg="#cccccc",fg="#333333",font="Helvatica 15 bold",
              width=1,height=4)
liste.pack()
liste.place(relx=0.43,rely=0.1)

pen2=Entry(bg="#ffffcc",fg="#333333",font="Helvatica 15 bold",width=8)
pen2.pack()
pen2.place(relx=0.66, rely=0.2)

pen3=Entry(bg="#ffffcc",fg="#333333",font="Helvatica 15 bold",width=15)
pen3.pack()
pen3.place(relx=0.25, rely=0.7)

yazi=Label(text="SONUÇ",fg="#333333",font="Helvatica 12 bold")
yazi.pack()
yazi.place(relx=0.05,rely=0.7)

listem=["+","-","*","/"]
def ekle():
    for i in listem:
        liste.insert(END,i)

ekle()

def islem(event):
    global a
    d=liste.curselection()
    a=int(d[0])


def sonuc(event):
    global a
    if a==0:
        sonuc=float(pen.get())+float(pen2.get())
        pen3.delete(0,END)
        pen3.insert(0,sonuc)
    if a==1:
        sonuc2=float(pen.get())-float(pen2.get())
        pen3.delete(0,END)
        pen3.insert(0,sonuc2)
    if a==2:
        sonuc3=float(pen.get())*float(pen2.get())
        pen3.delete(0,END)
        pen3.insert(0,sonuc3)
    if a==3:
        sonuc4=float(pen.get())/float(pen2.get())
        pen3.delete(0,END)
        pen3.insert(0,sonuc4)
        
def sil():
    pen.delete(0,END)
    pen2.delete(0,END)
    pen3.delete(0,END)

dugme=Button(text="TEMİZLE",fg="#333333",font="Helvatica 10 bold",command=sil)
dugme.pack()
dugme.place(relx=0.4,rely=0.9)
liste.bind("<Double-Button-1>",islem)
pen2.bind("<Return>",sonuc)
mainloop()
