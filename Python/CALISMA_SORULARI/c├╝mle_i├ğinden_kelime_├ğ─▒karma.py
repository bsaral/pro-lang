#!/usr/bin/env python
# -*- coding: utf8 -*- 
def diziden_arindir(kisa_dizi,uzun_dizi):
    
    bul=uzun_dizi.find(kisa_dizi)
    uzunluk=len(kisa_dizi)
    
    print uzun_dizi[:bul]+uzun_dizi[bul+uzunluk:]
