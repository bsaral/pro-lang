#-*-coding:utf-8-*-
# http://www.serbestdoviz.com/

###################################
## İNTERNET OLMADAN ÇALIŞMAZ !!! ##
###################################

from Tkinter import *
from tkMessageBox import *
import urllib2

win=Tk()
win.title("KUR HESAPLAMA")
win.geometry("600x500+50+15")
win.tk_setPalette("#cccccc")
win.resizable(width=FALSE, height=FALSE)


page=urllib2.urlopen("http://www.serbestdoviz.com/")
text=page.read()


pen1=Entry(bg="#ffffcc",fg="#333333",font="Helvatica 12 bold",width=14)
pen1.pack()
pen1.place(relx=0.03, rely=0.1)
pen1.focus_set()


yazi1=Label(text="TL",fg="#333333",font="Helvatica 12 bold")
yazi1.pack()
yazi1.place(relx=0.09, rely=0.05)


pen2=Entry(bg="#ffffcc",fg="#333333",font="Helvatica 12 bold",width=14)
pen2.pack()
pen2.place(relx=0.4, rely=0.1)


yazi2=Label(text="DOLAR",fg="#333333",font="Helvatica 12 bold")
yazi2.pack()
yazi2.place(relx=0.44, rely=0.05)


pen3=Entry(bg="#ffffcc",fg="#333333",font="Helvatica 12 bold",width=14)
pen3.pack()
pen3.place(relx=0.75, rely=0.1)


yazi2=Label(text="EURO",fg="#333333",font="Helvatica 12 bold")
yazi2.pack()
yazi2.place(relx=0.79, rely=0.05)


yazi3=Label(text="SONUÇ",fg="#333333",font="Helvatica 12 bold")
yazi3.pack()
yazi3.place(relx=0.2, rely=0.35)

pen4=Entry(bg="#ccccff",fg="#333333",font="Helvatica 13 bold",width=30)
pen4.pack()
pen4.place(relx=0.32, rely=0.35)




def tl_dolar():
    d=text.find('"usd"')
    e=text.find(">",d)+1
    f=text.find("<",e)
    kur2=float(text[e:f])

    for i in pen1.get():
        i=str(i)
        if i == ",":
            showerror("HATA","LÜTFEN SAYILAR ARASINA VİRGÜL DEĞİL NOKTA KOYUNUZ")
            pen1.delete(0,END)
        else:
            pass
        
    para2=float(pen1.get())
    son2=para2/kur2
    son2="%.2f"%son2
    son3=para2, "TL =" ,son2, "$"

    pen1.delete(0,END)
    pen4.delete(0,END)
    #son3 değeri tuple olarak çıktığı için
    #for döngüsüne alıp str olarak yazılmasını sağladık.
    for i in son3:
        i=str(i)
        pen4.insert(END,i)
    
    
def tl_euro():
    a=text.find('"euro"')
    b=text.find(">",a)+1
    c=text.find("<",b)
    kur=float(text[b:c])

    for i in pen1.get():
        i=str(i)
        if i == ",":
            showerror("HATA","LÜTFEN SAYILAR ARASINA VİRGÜL DEĞİL NOKTA KOYUNUZ")
            pen1.delete(0,END)
        else:
            pass

    
    para=float(pen1.get())
    son=para/kur
    son="%.2f"%son
    son2=para,"TL =",son,"€"

    pen1.delete(0,END)
    pen4.delete(0,END)
    for i in son2:
        i=str(i)
        pen4.insert(END,i)
        

def dolar_tl():
    a=text.find('"usd2"')
    b=text.find(">",a)+1
    c=text.find("<",b)
    kur=float(text[b:c])

    for i in pen2.get():
        i=str(i)
        if i == ",":
            showerror("HATA","LÜTFEN SAYILAR ARASINA VİRGÜL DEĞİL NOKTA KOYUNUZ")
            pen2.delete(0,END)
        else:
            pass
    
    para=float(pen2.get())
    son=para*kur
    son="%.2f"%son
    son2=para,"$ =",son,"TL"

    pen2.delete(0,END)
    pen4.delete(0,END)
    for i in son2:
        i=str(i)
        pen4.insert(END,i)

def dolar_euro():
    d=text.find('"usd2eur"')
    e=text.find(">",d)+1
    f=text.find("<",e)
    kur2=float(text[e:f])

    for i in pen2.get():
        i=str(i)
        if i == ",":
            showerror("HATA","LÜTFEN SAYILAR ARASINA VİRGÜL DEĞİL NOKTA KOYUNUZ")
            pen2.delete(0,END)
        else:
            pass
    
    para2=float(pen2.get())
    son4=para2*kur2
    son4="%.2f"%son4
    son2=para2,"$ =",son4,"€"

    pen2.delete(0,END)
    pen4.delete(0,END)
    for i in son2:
        i=str(i)
        pen4.insert(END,i)


def euro_tl():
    a=text.find('"eur2o"')
    b=text.find(">",a)+1
    c=text.find("<",b)
    kur=float(text[b:c])

    for i in pen3.get():
        i=str(i)
        if i == ",":
            showerror("HATA","LÜTFEN SAYILAR ARASINA VİRGÜL DEĞİL NOKTA KOYUNUZ")
            pen3.delete(0,END)
        else:
            pass
    
    para=float(pen3.get())
    son=para*kur
    son="%.2f"%son
    son2=para,"€ =",son,"TL"

    pen3.delete(0,END)
    pen4.delete(0,END)
    for i in son2:
        i=str(i)
        pen4.insert(END,i)
        

def euro_dolar():
    a=text.find('"eur2usd"')
    b=text.find(">",a)+1
    c=text.find("<",b)
    kur=float(text[b:c])

    for i in pen3.get():
        i=str(i)
        if i == ",":
            showerror("HATA","LÜTFEN SAYILAR ARASINA VİRGÜL DEĞİL NOKTA KOYUNUZ")
            pen3.delete(0,END)
            
        else:
            pass

    para=float(pen3.get())
    son=para*kur
    son="%.2f"%son
    son2=para,"€ =",son,"$"

    pen3.delete(0,END)
    pen4.delete(0,END)
    for i in son2:
        i=str(i)
        pen4.insert(END,i)


def silemezsin(event=None):
    if event.keysym == "BackSpace" or event.keysym == "Delete":
        return "break"
pen4.bind("<Key>", silemezsin)

yazi_tr=Label(fg="#333333",font="Helvatica 10 bold")
yazi_tr.pack()
yazi_tr.place(relx=0.7, rely=0.0)

def tarih():
    a=text.find('"tarih"')
    b=text.find(">",a)+1
    c=text.find("<",b)

    kur=str(text[b:c])
    yazi_tr["text"]=kur
tarih()
    



dugme1=Button(text="TL/EURO",bg="white",fg="#333333",font="Helvatica 10 bold",
             command=tl_euro)
dugme1.pack()
dugme1.place(relx=0.067, rely=0.17)

dugme2=Button(text="TL/DOLAR",bg="white",fg="#333333",font="Helvatica 10 bold",
             command=tl_dolar)
dugme2.pack()
dugme2.place(relx=0.061, rely=0.24)

dugme3=Button(text="DOLAR/TL",bg="white",fg="#333333",font="Helvatica 10 bold",
             command=dolar_tl)
dugme3.pack()
dugme3.place(relx=0.43, rely=0.17)


dugme4=Button(text="DOLAR/EURO",bg="white",fg="#333333",font="Helvatica 10 bold",
             command=dolar_euro)
dugme4.pack()
dugme4.place(relx=0.42, rely=0.24)


dugme5=Button(text="EURO/TL",bg="white",fg="#333333",font="Helvatica 10 bold",
             command=euro_tl)
dugme5.pack()
dugme5.place(relx=0.8, rely=0.17)

dugme6=Button(text="EURO/DOLAR",bg="white",fg="#333333",font="Helvatica 10 bold",
             command=euro_dolar)
dugme6.pack()
dugme6.place(relx=0.785, rely=0.24)
    

def pen(x,y,birim):
    pen5=Entry(bg="#ffffcc",fg="#333333",font="Helvatica 12 bold",width=12)
    pen5.pack()
    pen5.place(relx=x, rely=y)
    a=text.find(birim)
    b=text.find(">",a)+1
    c=text.find("<",b)

    kur=float(text[b:c])
    pen5.insert(0,kur)
    

def yazi(yaz,x,y):
    yazi2=Label(text=yaz,fg="#333333",font="Helvatica 12 bold")
    yazi2.pack()
    yazi2.place(relx=x, rely=y)

yazi("SERBEST PİYASA DÖVİZ KURLARI",0.25,0.45)
yazi("ALIŞ",0.3,0.5)
yazi("SATIŞ",0.55,0.5)

pen(0.25,0.6,'"euro"')
yazi("Euro",0.0,0.6)
pen (0.51,0.6,'"eur2o"')

pen(0.25,0.65,'"usd"')
yazi("Amerikan Doları",0.0,0.65)
pen (0.51,0.65,'"usd2"')


pen(0.25,0.7,'"chf"')
yazi("İsviçre Frangı",0.0,0.7)
pen (0.51,0.7,'"chf2"')


pen(0.25,0.75,'"gbp"')
yazi("İngiliz Sterlini",0.0,0.75)
pen (0.51,0.75,'"gbp2"')


pen(0.25,0.8,'"dkk"')
yazi("Danimarka Kron",0.0,0.8)
pen (0.51,0.8,'"dkk2"')

yazi_son=Label(text="http://www.serbestdoviz.com/",fg="#336666",
               font="Helvatica 9 bold")

yazi_son.pack(side=BOTTOM)

yazi_son2=Label(text="BETÜL SARAL",fg="#333333",
               font="Helvatica 9 bold")

yazi_son2.pack(side=BOTTOM)



mainloop()



                                #BETÜL SARAL
