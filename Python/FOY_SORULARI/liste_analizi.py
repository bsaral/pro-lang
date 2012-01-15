#!/usr/bin/env python
# -*- coding: utf8 -*- 


def analiz(karakter):
    liste=[]
    liste.append(karakter)

    kar_dizisi,tam_sayi,ond_sayi,bool_sayi,liste_sayi=0,0,0,0,0

    for a in liste:
        for i in a:
            if type(i)==int:
                tam_sayi+=1

            elif type(i)==str:
                kar_dizisi+=1

            elif type(i)==list:
                liste_sayi+=1

            elif type(i)==float:
                ond_sayi+=1

            else:
                bool_sayi+=1

        print kar_dizisi;print tam_sayi;print ond_sayi;print bool_sayi
        print liste_sayi
