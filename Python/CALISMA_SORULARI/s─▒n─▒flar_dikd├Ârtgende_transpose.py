#!/usr/bin/env python
# -*- coding: utf8 -*- 

class nokta:
    def __init__(self,eni,boyu):
        self.en=eni
        self.boy=boyu

    def cevre(self):
        sekil=""
        for i in range(self.en):
            sekil=sekil+"*"

        for j in range(self.boy):
            print sekil

    def dondur(self):
        print "İLK ŞEKLİMİZ"
        sekil2=""
        for i in range(self.boy):
            sekil2+="*"

        for j in range(self.en):
           print sekil2
        print "İKİNCİ ŞEKLİMİZ"
        dikdortgen.cevre()

dikdortgen=nokta(5,2)

