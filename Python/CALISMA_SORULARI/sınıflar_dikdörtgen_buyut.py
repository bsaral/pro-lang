#!/usr/bin/env python
# -*- coding: utf8 -*- 

class nokta:
    def __init__(self,eni,boyu):
        self.en=eni
        self.boy=boyu
        
    def ciz(self):
        sekil=""
        for i in range(self.en):
            sekil=sekil+"*"

        for j in range(self.boy):
            print sekil

    def buyut(self,sayi):
        print "ilk şekil"
        dikdortgen.ciz()
        
        print "son şekil"
        self.en=self.en*sayi
        self.boy=self.boy*sayi
        dikdortgen.ciz()
        


dikdortgen=nokta(5,2)

