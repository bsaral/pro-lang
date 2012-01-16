# -*- coding: cp1254 -*-
class Stack():
    def __init__(self):
        self.liste=[]

    def bos(self):
        return self.liste==[]
    def ekle(self,n):
        self.liste.append(n)
    def pop(self,n=None):
       self.liste.pop()

def checker(s):
    a=Stack()
    deger=True
    say=0
    for i in range(len(s)):
        if deger:
            if s[i]=="(":
                say+=1
                a.ekle(s[i])
            else:
                if a.bos():
                    deger=False
                    break
                else:
                    a.pop()
                    say+=1
    if deger and a.bos():
        print "parantezler eşit"
    else:
        print say,". yerde hata var !!!"
        if s[say-1]=="(":
            print "açılan parantez kapatılmamış."
        else:
            print "parantez açılmadan kapatılmış."

checker("()()))(()")
                
            
        
    
