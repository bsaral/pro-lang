
#-*-coding:utf-8-*-

from Tkinter import *
from tkMessageBox import *


win=Tk()
win.title("FİHRİST")
win.geometry("650x400+200+200")
win.tk_setPalette("#ffcccc")


yazi=Label(text="Aşağıdaki kutucuğa isim ve numarayı ayrı ayrı giriniz.",
           fg="#660066",font="Helvatica 15 bold")
yazi.pack()


yazi2=Label(text="silmek istediğiniz öğenin üstüne tıklayıp DELETE tuşuna basınız",
           fg="#660066",font="Helvatica 10 bold")
yazi2.pack()


liste1=Listbox(bg="#ffffcc",fg="#660066",font="Helvatica 12 bold")
liste1.pack(expand=YES,side=RIGHT)

liste2=Listbox(bg="#ffffcc",fg="#660066",font="Helvatica 12 bold")
liste2.pack(expand=YES,side=LEFT)


def kaydet():
    ac=open("fihrist.txt","w")
    for i in liste2.get(0,END):
        ac.write(i)
    for a in liste1.get(0,END):
        ac.write(a)
    showinfo("BİLGİLENDİRME", "BİLGİLER MASAÜSTÜNÜZDE FİHRİST ADLI\
 BELGEYE KAYDEDİLMİŞTİR.")  


dugme=Button(text="KAPAT",bg="white",fg="#660066",font="Helvatica 12 bold",
             command=win.destroy)
dugme.pack(side=BOTTOM)


dugme2=Button(text="KAYDET",bg="white",fg="#660066",font="Helvatica 12 bold",
             command=kaydet)
dugme2.pack(side=BOTTOM)


yaz=Entry(bg="#ffffcc",fg="#660066",font="Helvatica 18 bold",width=80)
yaz.pack(side=BOTTOM)



def ekle(event):
    dizi=""
    
    for i in yaz.get():
        dizi+=i
        
    if dizi.isalpha()== True:
        liste2.insert(0,dizi)
    if dizi.isdigit()== True:
        liste1.insert(0,dizi)
    if dizi.isalpha()== False and dizi.isdigit()== False:
        showerror("HATA!", "İsimle beraber numara girmeyiniz yada isim yazarken\
arada boşluk bırakmayınız!",type=OK) 
    yaz.delete(0,END)

    
def sil(event):
    d=liste2.curselection()
    a=int(d[0])
    liste2.delete(0,a)

    
def sil2(event):
    b = liste1.curselection()
    c=int(b[0])
    liste1.delete(0,c)
    

liste2.bind("<Delete>",sil)
liste1.bind("<Delete>",sil2)
   
yaz.bind("<Return>",ekle)

mainloop()


                                    #BETÜL SARAL

