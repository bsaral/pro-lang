#!/usr/bin/env python
# -*- coding: utf8 -*- 

from __future__ import division

def yarilar_toplami(sayi):
    a=0
    if sayi>0:
    
        for i in  range(sayi):

            sayi=sayi/2
            a=a+sayi

        print a
            
            
    else:
        print "lütfen pozitif bir sayı giriniz."
