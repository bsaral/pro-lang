#!/usr/bin/env python
# -*- coding: utf8 -*- 



liste= [ [1,2,3 ] , [4,5 ] , 9 , [6,7,8,9 ] , 7 , [0 ] ]

for i in liste:

    if type(i)==int:
        pass

    else:
         print "liste[",liste.index(i),"]","toplam", sum(i)
