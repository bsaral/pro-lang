#!/usr/bin/env python
# -*- coding: utf8 -*- 

from __future__ import division 

def base2base(a, gt, ct):

    if gt==10 and ct==2 :
        f=""
        
        while a>0 :
            r=a/2
            r=int(r)
            c=r+r
            d=a-c
            e=str(d)
            a=r
            f=e+f
            
        print "\nGİRDİĞİNİZ SAYININ İKİLİK SİSTEMDEKİ KARŞILIĞI : ",f

    if gt==10 and ct==16 :
        print "\nSAYININ HEXADECİMAL(16 LIK) KARŞILIĞI = %X"%(a)

    if gt ==10 and ct==8 :
         print "\nSAYININ HEXADECİMAL(16 LIK) KARŞILIĞI = %o"%(a)

    if gt==2 and ct==10 :
        sonu=0
        a=str(a)
        b=len(a)
        say=b
        for c in a:
            say=say-1
            son=int(c)*2**say
            sonu=sonu+son
        print "\nGİRDİĞİNİZ SAYININ DECİMAL(ONLUK) KARŞILIĞI : ",sonu

    else :
        print "\nBU İŞLEM HENÜZ SİSTEME EKLENMEMİŞTİR."
        
base2base(a, gt, ct)
raw_input()

