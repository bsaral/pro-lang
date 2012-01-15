#-*-coding:utf-8-*-

from Tkinter import *

win=Tk()
win.title("KİTAPLAR LİSTESİ")

win.geometry("650x400+100+100")
win.tk_setPalette("#ffcccc")

etiket=Label(text="Aşağıdaki pencere içerisinde bulunan ögelerin üzerine tıklayın",
             fg="black",font="Arial 15 bold")
etiket.pack()

liste=["insancıklar","ana","asla vazgeçme","karanlık öyküler","kaşağı"]

liste_win=Listbox(bg="#ccccff",fg="darkblue",font="Arial 15 bold")
liste_win.pack(expand=YES)


def ekle():
    for i in liste:
        liste_win.insert(END,i)

def goster(event):
    global win2
    win2=Toplevel()
    yaz=Label(win2,fg="darkblue",font="Arial 15 bold")

    d=liste_win.curselection()
    a=int(d[0])
    i=liste[a]
    if a == 0:
            yaz["text"]="%s kitabı dünya klasiklerindendir.kitabın yazarı DOSTOYEVSKI"%i
            yaz.pack()
    

    if a == 1:
            yaz["text"]="%s kitabı dünya klasiklerindendir.kitabın yazarı MAKSIM GORKI"%i
            yaz.pack()
    if a == 2:
            yaz["text"]="%s kitabının yazarı HARLAN COBEN"%i
            yaz.pack()
    if a == 3:
            yaz["text"]="%s kitabının yazarı STEPHEN KING"%i
            yaz.pack()

    if a== 4:
            yaz["text"]="%s kitabının yazarı ÖMER SEYFETTIN"%i
            yaz.pack()

   
           
    cik2= Button(win2,text="KAPAT",command=win2.destroy,bg="white",fg="black",width=10,font="Arial 10 bold")
    cik2.pack()       

liste_win.bind("<Double-Button-1>",goster)



bas=Button(text="BASLA",command=ekle,bg="white",fg="black",width=15,font="Arial 10 bold")
bas.pack(expand=YES,side=LEFT)
        
cik=Button(text="KAPAT",command=win.destroy,bg="white",fg="black",width=15,font="Arial 10 bold")
cik.pack(expand=YES,side=RIGHT)

mainloop()        
