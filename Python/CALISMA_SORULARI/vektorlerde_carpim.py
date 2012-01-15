#!/usr/bin/env python
# -*- coding: utf8 -*- 

def vektor_nokta_carpimi(a,b):
    #a ve b birer listedir.
    listem=[]
    for i in range(len(a)):
        listem.append(a[i]*b[i])
        son=sum(listem)
    print "nokta çarpımı=",son


def vektor_skaler_carpim(liste,sayi):
    listem2=[]
    for i in liste:
        listem2.append(i*sayi)
    print listem2
