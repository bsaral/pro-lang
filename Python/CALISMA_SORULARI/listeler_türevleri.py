#!/usr/bin/env python
# -*- coding: utf8 -*-


def say(liste):
    #liste içindeki kelimelerin sesli harf sayısını bulur.
    sesliler="aeuioAEUIO"
    sayi=0
    for kelime in liste:
        for i in kelime:
            if i in sesliler:
                sayi+=1
        print kelime,"içindeki sesli harf sayısı=",sayi
        sayi=0



#------------------------------------------------------------------------------

def ic_ice_listeler(listeler):
    #iç içe listeler halinde verilen bir listenin her bir elemanın eleman
        #sayısının toplamını ve eleman sayısını veren program
    
    sayi=0
    for liste in listeler:
        if type(liste)==list:
            a=sum(liste)
            for i in liste:
                sayi+=1
            print "liste[",listeler.index(liste),"]=",sayi,"eleman,toplam=",a
            sayi=0
        else:
             pass


#------------------------------------------------------------------------------


def deger(liste):
    #listedeki en büyük ve en küçük değerin bulunmasını sağlar.
    print "en büyük değer=",max(liste),"en küçük değer=",min(liste)



#------------------------------------------------------------------------------


def ters_yazdir(liste):
    #listeyi tersten yazdırma
    print liste[::-1]

    

#-------------------------------------------------------------------------------


def en_buyuk_sayi(liste):
    #listedeki rakamlarla en büyük sayıyı oluşturma
    dizgi=""
    for i in range(len(liste)):
        a=max(liste)
        dizgi+=str(a)
        liste.remove(a)
    print int(dizgi)


#-------------------------------------------------------------------------------


import random,string

def rastgele(cumle):
    #cümledeki rastgele seçilen kelimelerle yeniden cümle yapmak
    dizgi=""
    liste=cumle.split(" ")
    for i in range(len(liste)):
        random.shuffle(liste)
        cumle=string.join(liste, " ")
    print cumle
    

#------------------------------------------------------------------------------



def aynalama(pos,liste):
    #girilen pozisyona göre listeyi aynalayan fonksiyon
    print liste[pos+1::1]+liste[pos::-1]
    
    

#-------------------------------------------------------------------------------


def threshold(deger,liste):
    #girilen degerin altındaki sayıları ekrana döken program
    sayi=0
    yeni=[]
    for i in liste:
        if i < deger:
            sayi+=1
            yeni.append(0)
        else:
            yeni.append(1)

    print "eleman sayısı=",sayi,"liste=",yeni
    
   
#-------------------------------------------------------------------------------

def uzun_kisa(cumle):
    #liste yöntemi ile cümledeki en uzun en kısa kelimeyi bulma
    yeni=[]
    liste=cumle.split()
    for i in liste:
        yeni.append(len(i))
    uzun,kisa=max(yeni),min(yeni)
    a,b=yeni.index(uzun),yeni.index(kisa)
    print "en uzun kelime :",liste[a],"\nen kısa kelime :",liste[b]
        


#-------------------------------------------------------------------------------


