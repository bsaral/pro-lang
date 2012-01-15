#!/usr/bin/env python
#-*-coding:utf-8-*-
isim=raw_input("isminizi giriniz = ")

print "merhaba",isim

numara=raw_input("numaranızı giriniz = ")
if numara == "019" :
    print "bu numara ali ye aittir."

elif numara == "043" :
    print "bu numara mehmet e aittir."

elif numara == "126" :
    print "bu numara ayşeye aittir."

else :
    print "hoşgeldin",numara,isim
