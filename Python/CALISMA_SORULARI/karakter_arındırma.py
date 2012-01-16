#!/usr/bin/env python
# -*- coding: utf8 -*- 



def karakterden_arindir(karakter,kar_dizisi):
    liste=[]
    dizgi=""

    for i in kar_dizisi:
        liste.append(i)

    for a in karakter:
        if a in liste:
            liste.remove(a)

    for i in liste:
        i=str(i)
        dizgi+=i

    print dizgi

