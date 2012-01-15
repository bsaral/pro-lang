#!/usr/bin/env python
# -*- coding: utf8 -*- 


print "\nKARAKTERLERİ YAZARKEN TIRNAK İÇİNE ALMAYI UNUTMAYIN"

ekle=input("\nliste içerisine eklenecek kelimeleri yazınız :")
liste=[]
liste.extend(ekle)


sesliler="AEUIOaeiou"



for kelime in liste:
    sonuc=0
    for karakter in kelime:
    
        for i in karakter:
           
            if i in sesliler:
                sonuc+=1
                
    print kelime,"sesli harf sayısı=",sonuc  
