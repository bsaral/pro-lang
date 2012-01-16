#!/usr/bin/env python
# -*- coding: utf8 -*-



def dizgi_yazdir(kelime):
    #dizgi elemanlarını yazdırır.
    a=-1
    for i in kelime :
        a=a+1
        print "kelime[",a,"]=",i

#-------------------------------------------------------------------------------

def sesli_sessiz(kelime):
    #dizgideki sesli ve sessiz harf sayısını ekrana yazdırır.
    sesliler="aeuioAEUIO"
    sesli,sessiz=0,0
    for i in kelime:
        if i in sesliler:
            sesli+=1

        else:
            sessiz+=1
    print "sesli harfler =",sesli,"sessiz harfler =",sessiz


#-------------------------------------------------------------------------------

def sessiz_buyut(kelime):
    #dizgi içindeki sesiz harfleri büyültür
    sesliler="aeuioAEUIO"
    dizgi=""
    for i in kelime:
        if i not in sesliler:
            a=i.upper()
            dizgi+=a

        else:
            dizgi+=i
    print dizgi

    
#-------------------------------------------------------------------------------

def str_find(s1,s2):
    #s1 stringi içindeki s2 stringini arayan fonksiyon tasarlama
    dizgi=""
    for i in s1:
        for a in s2:
            if i==a:
                dizgi+=i
            else:
                pass
    print dizgi


#-------------------------------------------------------------------------------

def histogram(kelime):
    #kelime içindeki harf sıklığına bakar(histogram)
    
    kume=set(kelime)
    for i in kume:
        print "%s harfinden ==> %s tane"%(i,kelime.count(i))


#-------------------------------------------------------------------------------

def is_whitespace(dizgi):
    #dizgi içinde boşluk olup olmadığını kontol eder.
    for i in dizgi:
        if ord(i)==32:
            return "true"
    return"false"


#-------------------------------------------------------------------------------


def harf_degistir(kelime,eski_harf,yeni_harf):
    #dizgi içindeki harflerin belirli karakterlerle değişimi
    dizgi=""
    for i in kelime:
        if eski_harf==i:
            dizgi+=yeni_harf
        else:
            dizgi+=i
    print dizgi
    
    
#-------------------------------------------------------------------------------

def harf_degistir_kisa_yol(kelime,eski,yeni):
    #harf_degistir() fonksiyonunun kısa yoludur.
    
    print kelime.replace(eski,yeni)
    

