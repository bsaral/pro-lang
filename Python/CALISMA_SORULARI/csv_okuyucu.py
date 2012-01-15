#!/usr/bin/env python
# -*- coding: utf8 -*-
import csv
def say4(yol):
    ac=open(yol)
    oku=csv.reader(ac)
    for i in oku:
       a=int(i[1])
       d=int(i[2])
       b=a*0.4
       c=d*0.6
       print "isim=",i[0]
       print "not ortalaması=",c+b
    
    
        
say4("yeni.txt")

