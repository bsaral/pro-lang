#-*-coding:utf-8-*-
# http://www.serbestdoviz.com/

from Tkinter import *
from tkMessageBox import *
import urllib2

win=Tk()
win.title("BİRİM ÇEVİRİCİ")
win.geometry("650x400+200+200")
win.tk_setPalette("#ffcccc")

yazi=Label(text="Çevirmek istediğiniz birimleri kutucuklara giriniz.",
            fg="#660066",font="Helvatica 15 bold")
yazi.pack()


yazi1=Label(text="LİRA",fg="#660066",font="Helvatica 15 bold")
yazi1.pack(side=LEFT)

pen1=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen1.pack(side=LEFT)
pen1.focus_set()

pen2=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen2.pack(side=RIGHT)

yazi2=Label(text="EURO",fg="#660066",font="Helvatica 15 bold")
yazi2.pack(side=RIGHT)


page=urllib2.urlopen("http://www.serbestdoviz.com/")
text=page.read()

def cevir(event):
    a=text.find('"euro"')
    b=text.find(">",a)+1
    c=text.find("<",b)
    kur=float(text[b:c])

    para=int(pen1.get())
    son=para/kur

    pen2.insert(0,son)

def sil():
    pen1.delete(0,END)
    pen2.delete(0,END)


pen1.bind("<Return>",cevir)

dugme1=Button(text="TEMİZLE",bg="white",fg="#660066",font="Helvatica 12 bold",
             command=sil)
dugme1.pack(side=BOTTOM)

dugme2=Button(text="KAPAT",bg="white",fg="#660066",font="Helvatica 12 bold",
             command=win.destroy)
dugme2.pack(side=BOTTOM)



mainloop()
