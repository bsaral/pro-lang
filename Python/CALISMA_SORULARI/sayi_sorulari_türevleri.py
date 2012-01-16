#!/usr/bin/env python
# -*- coding: utf8 -*- 

def basamak_toplami(sayi):
    #basamaktaki sayıların toplamı
    liste=[]
    for i in str(sayi):
        liste.append(int(i))
    print sum(liste)

#-------------------------------------------------------------------------------

def basamak_tek(sayi):
    #tek basamaklı sayıların toplamı
    toplam=0
    for i in str(sayi):
        if int(i)%2==1:
            toplam+=int(i)
    print toplam

    
#----------------------------------------------------------------------------------


def basamak_ters(sayi):
    #basamakları sondan başa yazdıran
    sayi=str(sayi)
    a=sayi[::-1]
    print int(a)

#-----------------------------------------------------------------------------------    

def fark(sayi):
    #ters ve düz yazılmış sayıların arasındaki farkı hesaplama
    sayi=str(sayi)
    a=sayi[::-1]
    print int(a)-int(sayi)
    

#-----------------------------------------------------------------------------------

def say(sayi):
    #basamaktaki 0 ve 5 rakamalarını saymak
    toplam=0
    for i in str(sayi):
        i=int(i)
        if i==0 or i==5:
            toplam+=1
    print toplam
    
#------------------------------------------------------------------------------------

def deger(sayi):
    #sayının basamaklarıdndan en büyüğünün değeri
    liste=[]
    for i in str(sayi):
        liste.append(int(i))
        b=max(liste)
        a= liste.index(b)
    print b*(10**(len(liste)-(a+1)))
    
#-------------------------------------------------------------------------------------

def basamak(sayi):
    #sayının en büyük değernin bulunduğu basamağı gösterme
    liste=[]
    for i in str(sayi):
        liste.append(int(i))
        b=max(liste)
        a= liste.index(b)
    print 10**(len(liste)-(a+1)),"ler basamağı
