#!/usr/bin/env python
# -*- coding: utf8 -*- 


def kelime(cumle):
  liste1=[]
  liste=cumle.split()
  
  for i in liste:
    i=str(i)
    a=len(i)
    liste1.append(a)
    b=max(liste1)
    c=liste1.index(b)
  print liste[c]
