#!/usr/bin/env python
# -*- coding: utf8 -*-

def say2(yol,kaynak,kaynak2):
    ac=open(yol)
    ac2=open(kaynak, "w")
    ac3=open(kaynak2,"w")

    for i in ac:
        if "#" in i:
            ac2.write(i)
        else:
            ac3.write(i)
            
    ac2.close()
    ac3.close()

say2("deneme.txt","kop.txt","yaz.txt")
