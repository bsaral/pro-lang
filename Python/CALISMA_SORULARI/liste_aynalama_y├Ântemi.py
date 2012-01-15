#!/usr/bin/env python
# -*- coding: utf8 -*- 



def aynala(poz,karakter):

    #girilen karakterler arasına virgül konulmamalıdır.

    liste=[]
    liste.extend(karakter)
    a=liste[poz+1::1]+liste[poz::-1]
    print a
