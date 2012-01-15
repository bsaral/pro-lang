#!/usr/bin/env python
# -*- coding: utf8 -*- 

def kimlik(karakter):
    karakter=str(karakter)
    b,c,e=0,0,0

    if len(str(karakter))==11:
           for a in karakter[0:9:2]:
           a=int(a)
           b=b+a     #1.toplam
          
       for i in karakter[1:8:2]:
           i=int(i)
           c=c+i    #2.toplam
           
       d=((b*7)-c)%10
       d=str(d)

       if d==karakter[9]:

           for i in karakter[:10]:
               i=int(i)
               e=e+i          #son toplam
               son_basamak=e%10
               
               son_basamak=str(son_basamak)
               
               if son_basamak==karakter[10]:
                   print "TC KİMLİK NUMARASI GEÇERLİDİR."

       else:
            print "TC KİMLİK NUMARASI GEÇERLİ DEĞİLDİR."

    else:
        print "LÜTFEN 11 BASAMAKLI BİR TAMSAYI GİRİNİZ."
