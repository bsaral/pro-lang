#!/usr/bin/env python
# -*- coding: utf8 -*- 


def filtre(dosya_adi,karakter):
    ac=open(dosya_adi)
    liste=[]
    for i in ac:
        sade=i.strip()
        liste.append(sade)
    print liste
    

    for kelime in liste:
        if karakter in kelime:
            liste.remove(kelime)
    print liste

       
        
        

    
            
