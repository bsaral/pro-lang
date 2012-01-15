#!/usr/bin/env python
# -*- coding: utf8 -*- 

import random,string

def rastgele(cumle):
    dizgi=""
    liste=cumle.split()
    
    
    for i in liste:
        random.shuffle(liste)
        cumle=string.join(liste, " ")
        print cumle
