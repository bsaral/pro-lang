#!/usr/bin/env python
# -*- coding: utf8 -*- 


def basamak(sayi):
   a,b=0,0
   while sayi :
      kalan=sayi%10
      sayi=sayi/10
      if kalan%2!=0:
           a=a+kalan

   print a
