#!/usr/bin/env python
# -*- coding: utf8 -*- 


print "\nLÜTFEN BİRDEN FAZLA SAYI GİRİNİZ"

sayi=input("\nlisteye eklenecek sayıları giriniz = ")
liste=[]
liste.extend(sayi)

print "\nLİSTEMİZ", liste

print "\nLİSTEDEKİ EN BÜYÜK DEĞER=", max(liste)

print "\nLİSTENİN TERSTEN YAZILMIŞ HALİ",liste[::-1]
