#!/usr/bin/env python
# -*- coding: utf8 -*-
def fibo(sayi):
     fibonacci = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8,
               7: 13, 8: 21, 9: 34, 1: 55, 10: 89}

     if sayi<0 or type(sayi) !=int:
         return "pozitif bir tamsayı girin."

     elif sayi <=10:
         return fibonacci[sayi]

     else :
         sayi-=10
         i,j=55,89
         while sayi > 1:
             sayi-=1
             i,j=j,i+j

         return j

