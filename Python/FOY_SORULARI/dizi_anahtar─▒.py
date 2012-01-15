#!/usr/bin/env python
# -*- coding: utf8 -*- 


def anahtar(dizgi):
    liste=dizgi.split("-")
    liste2=[]

    for i in liste:
        i=int(i)
        liste2.append(i)
        liste2.sort()

    if len(liste2)%2==0:
        a=0

        for i in liste2:
            a=a+i
            b=a/len(liste2)
       
            c=((len(liste2))-2)/2
            orta=liste2[c:c+2]
            son1=(sum(orta)/2)*b

        print son1

    else:
        e=0
        for i in liste2:
            e=e+i
            f=e/len(liste2)

            k=((len(liste2))-1)/2
            orta2=liste2[k]
            son=orta2*f

        print son
