#!/usr/bin/env python
# -*- coding: utf8 -*- 
def esik_degeri(liste,anahtar):
    
    toplam=0
    yeni_liste=[]
    
    for i in liste:
        
        if i < anahtar :
            toplam+=1
            i=0
            yeni_liste.append(i)

        else:
            i=1
            yeni_liste.append(i)
            
    print "listedeki", toplam," sayı eşik değerinden küçüktür."
    print yeni_liste
