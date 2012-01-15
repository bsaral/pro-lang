#!/usr/bin/env python
# -*- coding: utf8 -*-

def histogram(kelime):
    sozluk={}
    for i in kelime:
        sozluk[i]=sozluk.get(i,0)+1
        a=sozluk.items()
        a.sort()
    print a
