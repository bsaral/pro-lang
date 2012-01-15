#!/usr/bin/env python
# -*- coding: utf8 -*-
class karakter:
    def __init__(self,karakter):
        self.kdizi=karakter
       
    def birlestir(self,kelime):
        return self.kdizi+kelime

    def kesital(self,bas,son):
        return self.kdizi[bas:son+1]

    def tekrarla(self ,sayi):
        return self.kdizi*sayi

    def birlestir_tut(self,kelime):
        a=self.kdizi+kelime
        self.kdizi=a
        return a

    def kesital_tut(self,bas,son):
        a=self.kdizi[bas:son+1]
        self.kdizi=a
        return a

    def tekrarla_tut(self,sayi):
         a=self.kdizi*sayi
         self.kdizi=a
         return a
