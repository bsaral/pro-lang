# -*- coding: cp1254 -*-

class Stack:
    def __init__(self):
        self.eleman = []

    def isEmpty(self):
        return self.eleman == []

    def push(self, eleman):
        return self.eleman.append(eleman)
       

    def pop(self):
        return self.eleman.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.eleman)

liste=[]    
def taban_cevir(sayi,taban):
    s=Stack()
    dizi="0123456789ABCDEF"
    
    if sayi < taban:
        s.push(dizi[sayi])
        
    else:
        s.push(dizi[sayi%taban])
        taban_cevir(sayi/taban,taban)

    while(s.size()):
        liste.append(s.pop())
    dizi="".join(liste)
    return dizi
   
   

taban_cevir(25,16)
taban_cevir(25,8)
taban_cevir(25,10)
taban_cevir(25,2)
        
        
