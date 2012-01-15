#!/usr/bin/env python
# -*- coding: utf8 -*- 


ekle=input("tek basamaklı sayıları giriniz =")

liste=[]
liste.extend(ekle)
dizgi=""

for i in range(len(liste)):

    k=max(liste)
    liste.remove(k)
    k=str(k)
    dizgi+=k

print int(dizgi)
