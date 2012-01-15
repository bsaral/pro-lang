#!/usr/bin/env python
#-*- coding: utf-8 -*-

def sifre(kelime):
    #verilen kelimeyi rot13 e göre şifreler.
    for i in kelime:
       a=ord(i)
       if 65<=a<78 or 97<=a<110:
           b=chr(a+13)
           print b


       else:
           b=chr(a-13)
           print b

    
def sifresiz(kelime):
    #şifrelenmiş kelimenin bulunmasını sağlar.
    for i in kelime:
        a=ord(i)
        if 110<=a<123 or 78<=a<91:
            b=chr(a-13)
            print b

        else:
            b=chr(a+13)
            print b



    
        
