#!/usr/bin/env python
# -*- coding: utf8 -*- 

# http://www.serbestdoviz.com/

import urllib2

sor=raw_input("hangisinin kur bilgisini öğrenmek istiyorsunuz (EURO/DOLAR): ")

page=urllib2.urlopen("http://www.serbestdoviz.com/")
text=page.read()


if sor == "euro" or sor == "EURO":
    a=text.find('"usd"')
    b=text.find(">",a)+1
    c=text.find("<",b)

    kur=float(text[b:c])

    print "EURO = %f tl"%(kur)

    if kur>=1.4:
        print "\nBEKLEMEYE DEVAM"
    else:
        print "\nDOLAR ALMANIN TAM ZAMANI"

elif sor == "dolar" or sor == "DOLAR":
    d=text.find('"euro"')
    e=text.find(">",d)+1
    f=text.find("<",e)

    kur=float(text[e:f])

    print "DOLAR = %f tl"%(kur)

    if kur>=1.4:
        print "\nBEKLEMEYE DEVAM"
    else:
        print "\nEURO ALMANIN TAM ZAMANI"
