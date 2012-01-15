#!/usr/bin/env python
# -*- coding: utf8 -*- 


def ingilizce(dosya):
    ac=open(dosya)
    liste=[]
   
    for i in ac:
        a=i.strip()
        liste.append(a)
        liste.sort()
    for i in liste:
        
        print i
   
        

       
        
        

    
            
