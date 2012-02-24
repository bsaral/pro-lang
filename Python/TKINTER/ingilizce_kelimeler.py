#!/usr/bin/env python 
#-*-coding:utf-8-*-


##############################################################################
## DİKKATT !!!!!!                                                           ##
##                                                                          ##
## PROGRAMI ÇALIŞTIRMAK İÇİN ÖNCE BİR DOSYA AÇIN,                           ##  
## PROGRAMI BU DOSYA İÇİNE YERLEŞTİRİN SONRA  ingilizce.txt  VE cevap.txt   ##
## ADINDA İKİ BELGE AÇIN VE BU BELGELERİDE DOSYANIN İÇİNE YERLEŞTİRİN.      ##
## PROGRAM ÇALIŞTIĞINDA İLK OLARAK KULLANIM KILAVUZU TUŞUNA BASIN.          ##                 
##                                                                          ##
##                                                                          ##
##############################################################################


from Tkinter import *
from tkMessageBox import *
import codecs

win=Tk()
win.title("İNGİLİZCE ÖĞRENİYORUM")
win.geometry("600x500+200+15")
win.tk_setPalette("#C5908E")
win.resizable(width=FALSE, height=FALSE)

yazi=Label(fg="#333333",font="Helvatica 18 bold")
yazi.pack()
yazi.place(relx=0.48, rely=0.15)

yazi4=Label(fg="#333333",font="Helvatica 18 bold")
yazi4.pack()
yazi4.place(relx=0.48, rely=0.25)

yazi5=Label(fg="#333333",font="Helvatica 18 bold")
yazi5.pack()
yazi5.place(relx=0.48, rely=0.35)

yazi1=Label(text="İNG", fg="#333333",font="Helvatica 15 bold")
yazi1.pack()
yazi1.place(relx=0.0, rely=0.69)

yazi2=Label(text="TÜRKÇE", fg="#333333",font="Helvatica 15 bold")
yazi2.pack()
yazi2.place(relx=0.5, rely=0.69)

yazi3=Label(text="SONUÇ", fg="#333333",font="Helvatica 15 bold")
yazi3.pack()
yazi3.place(relx=0.12, rely=0.03)

giris=Entry(bg="white",fg="black",width=30)
giris.pack()
giris.place(relx=0.1,rely=0.7)
giris.focus_set()

giris2=Entry(bg="white",fg="black",width=30)
giris2.pack()
giris2.place(relx=0.67,rely=0.7)

liste_bak=Listbox(bg="#EBDDE2",fg="black",font="Arial 12 bold")
liste_bak.pack()
liste_bak.place(relx=0.05, rely=0.1)

liste1,liste2,liste3,liste4,liste5=[],[],[],[],[]


ingilizce=codecs.open("ingilizce.txt","rb",encoding="utf-8")
turkce=codecs.open("cevap.txt","rb",encoding="utf-8")


sozluk = dict(zip([unicode(i.strip()) for i in ingilizce.readlines()],[unicode(i.strip()) for i in turkce.readlines()]))

turkce.close()
ingilizce.close()

def cevap(event=None):
    global liste3,liste4
    dogru,yanlis,uydurma=0,0,0
    if giris.get() in sozluk.keys():
        if sozluk[giris.get()] == giris2.get():
            dogru+=1
            liste4.append(dogru)
            yazi["text"]="TRUE  ✔"
            yaz=giris.get(),"==>",giris2.get(),"✔"
            liste_bak.insert(END,yaz)
            giris.delete(0,END)
            giris2.delete(0,END)
            giris.focus_set()
                
        else:
            yanlis+=1
            liste3.append(yanlis)
            yazi["text"]="FALSE  X"
            yaz2=giris.get(),"==>",giris2.get(),   "X"
            liste_bak.insert(END,yaz2)
            giris.delete(0,END)
            giris2.delete(0,END)
            giris.focus_set()
            
    else:
        uydurma+=1
        liste5.append(uydurma)
        yazi["text"]="böyle bir kelime \nsözlükte \nbulunmamaktadır.\nlütfen kelimeyi \ndosyaya ekleyiniz."
        giris.delete(0,END)
        giris2.delete(0,END)
        giris.focus_set()


giris2.bind("<Return>",cevap)
    
def sonuc_belgen(event=None):
    global liste3,liste4
    yazi["text"]=sum(liste4),"doğru", "✔"
    yazi4["text"]=sum(liste3),"yanlış","X"
    yazi5["text"]=sum(liste5), "uydurma","!"

def bilgilendir(event=None):
    showinfo("BİLGİLENDİRME","1-)program,ingilizce.txt ve cevap.txt aynı dosyada olsun.\
            \n\n2-)LÜTFEN açtığınız text dosyalarını utf-8 olarak kaydediniz.(örn:notepad++ da biçim > kodla(UTF-8)  seçiniz.)\
             \n\n3-)ingilizce.txt bölümüne ingilizce kelimelerinizi ve cevap.txt bölümüne de türkçe karşılıklarını giriniz.\
             \n\n4-)iki belgede de sıra önemlidir. yazdığınız ingilizce kelimenin türkçe karşılığını ingilizce kelimeniz hangi sıradaysa o sırada yazın.\
             \n\n5-)ingilizce kelimeleri şu siteden bakıp text dosyasına kaydedebilirsiniz ==>  http://www.baktabul.net/dil-ve-dilbilimi/165250-en-cok-kullanilan-ingilizce-kelimeler-ve-anlamlari.html\
             \n\n6-)text belgelerine yazdığınız kelimeleri alt alta yazınız.büyük harf-küçük harf ve noktalama işaretlerine duyarlıdır")
    
             
                
        
dugme=Button(text="SONUCUMU GÖSTER",bg="white",fg="#333333",font="Helvatica 10 bold",
             command=sonuc_belgen)
dugme.pack()
dugme.place(relx=0.35, rely=0.82)


dugme2=Button(text="KULLANIM KILAVUZU",bg="white",fg="#333333",font="Helvatica 10 bold",
             command=bilgilendir)
dugme2.pack()
dugme2.place(relx=0.4, rely=0.02)

yazi6=Label(text="BETÜL SARAL", fg="black",font="Helvatica 8 bold")
yazi6.pack()
yazi6.place(relx=0.4, rely=0.96)


mainloop()




                              #BETÜL SARAL
