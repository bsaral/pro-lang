#-*-coding:utf-8-*-
# http://www.serbestdoviz.com/

from Tkinter import *
from tkMessageBox import *
import urllib2

win=Tk()
win.title("KUR HESAPLAMA")
win.geometry("680x600+50+25")
win.tk_setPalette("#ffcccc")

baslik=Label(text="SARAL KUR HESAPLAMA",fg="#660066",font="Helvatica 15 bold")
baslik.pack()

baslik2=Label(text="kur bilgileri internet sayfasından alınmaktadır",
              fg="#660066",font="Helvatica 10 bold")
baslik2.pack(side=BOTTOM)

yazi=Label(text="Çevirmek istediğiniz birimleri kutucuklara giriniz.",
            fg="#660066",font="Helvatica 15 bold")
yazi.pack()
yazi.place(relx=0.19, rely=0.1)

yazi1=Label(text="LİRA",fg="#660066",font="Helvatica 15 bold")
yazi1.pack()
yazi1.place(relx=0.0001, rely=0.3)

pen1=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen1.pack()
pen1.place(relx=0.12, rely=0.3)
pen1.focus_set()

pen2=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen2.pack()
pen2.place(relx=0.68, rely=0.3)

yazi2=Label(text="EURO",fg="#660066",font="Helvatica 15 bold")
yazi2.pack()
yazi2.place(relx=0.58, rely=0.3)

pen3=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen3.pack()
pen3.place(relx=0.12, rely=0.45)

yazi3=Label(text="LİRA",fg="#660066",font="Helvatica 15 bold")
yazi3.pack()
yazi3.place(relx=0.0001, rely=0.45)

pen4=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen4.pack()
pen4.place(relx=0.68, rely=0.45)

yazi4=Label(text="DOLAR",fg="#660066",font="Helvatica 15 bold")
yazi4.pack()
yazi4.place(relx=0.56, rely=0.45)

pen5=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen5.pack()
pen5.place(relx=0.12, rely=0.6)

yazi5=Label(text="DOLAR",fg="#660066",font="Helvatica 15 bold")
yazi5.pack()
yazi5.place(relx=0.0, rely=0.6)

pen6=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen6.pack()
pen6.place(relx=0.68, rely=0.6)

yazi6=Label(text="EURO",fg="#660066",font="Helvatica 15 bold")
yazi6.pack()
yazi6.place(relx=0.58, rely=0.6)

pen7=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen7.pack()
pen7.place(relx=0.12, rely=0.75)

yazi7=Label(text="EURO",fg="#660066",font="Helvatica 15 bold")
yazi7.pack()
yazi7.place(relx=0.0, rely=0.75)

pen8=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=15)
pen8.pack()
pen8.place(relx=0.68, rely=0.75)

yazi8=Label(text="DOLAR",fg="#660066",font="Helvatica 15 bold")
yazi8.pack()
yazi8.place(relx=0.56, rely=0.75)


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
    pen3.delete(0,END)
    pen4.delete(0,END)
    pen5.delete(0,END)
    pen6.delete(0,END)
    pen7.delete(0,END)
    pen8.delete(0,END)
    
def cevir2(event):
    d=text.find('"usd"')
    e=text.find(">",d)+1
    f=text.find("<",e)
    kur2=float(text[e:f])

    para2=int(pen3.get())
    son2=para2/kur2

    pen4.insert(0,son2)


def cevir3(event):
    g=text.find('"usd2eur"')
    h=text.find(">",g)+1
    i=text.find("<",h)
    kur3=float(text[h:i])

    para3=int(pen5.get())
    son3=para3*kur3

    pen6.insert(0,son3)


def cevir4(event):
    j=text.find('"eur2usd"')
    k=text.find(">",j)+1
    l=text.find("<",k)
    kur4=float(text[k:l])

    para4=int(pen7.get())
    son4=para4*kur4

    pen8.insert(0,son4)
    

pen1.bind("<Return>",cevir)
pen3.bind("<Return>",cevir2)
pen5.bind("<Return>",cevir3)
pen7.bind("<Return>",cevir4)

dugme1=Button(text="TEMİZLE",bg="white",fg="#660066",font="Helvatica 12 bold",
             command=sil)
dugme1.pack()
dugme1.place(relx=0.3, rely=0.9)

dugme2=Button(text="KAPAT",bg="white",fg="#660066",font="Helvatica 12 bold",
             command=win.destroy)
dugme2.pack(side=BOTTOM)
dugme2.place(relx=0.6, rely=0.9)


mainloop()



                            #BETÜL SARAL
