#!/usr/bin/env python
# -*- coding: utf8 -*- 


def bul(cumle):
    
    liste2=[]
    liste=cumle.split()
    for i in liste:
        liste2.append(len(i))
        
    a,b=max(liste),min(liste)
    c,d=liste.index(a),liste.index(b)
    
    print "en uzun kelime :",liste[c],"\tkelimenin sırası:",c
    print "en kısa kelime :",liste[d],"\tkelimenin sırası",d
    

