#!/usr/bin/env python
# -*- coding: utf8 -*-

def say3(yol):
    ac=open(yol)
    dizi=""
    dizi1=""
    for i in ac:
        for a in i:
            if a== "(" : 
               dizi+="("
               
            if a==")":
               dizi1+=")"
              

    if len(dizi)==len(dizi1):
        print "true"
    else:
        print "false"
           
        
        
say3("yeni.txt")
