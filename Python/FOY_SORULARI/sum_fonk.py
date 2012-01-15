#!/usr/bin/env python
# -*- coding: utf8 -*-
def sinirsiz_toplam(*sayilar):
    liste=[]
    for i in sayilar:
        liste.append(i)
    print sum(liste)
