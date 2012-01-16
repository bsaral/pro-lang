#!/usr/bin/env python
# -*- coding: utf8 -*- 

import random

def rastgele(cumle):
  liste=cumle.split()
  for i in liste:
    k=random.randint(0,len(liste)-1)
    print liste[k]
    del liste[k]
