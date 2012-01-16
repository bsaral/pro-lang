#!/usr/bin/env python
# -*- coding: utf8 -*- 

import doctest

def mult_lists(liste1,liste2):
     """
      >>> mult_lists([1, 1], [1, 1])
      2
      >>> mult_lists([1, 2], [1, 4])
      9
      >>> mult_lists([1, 2, 1], [1, 4, 3])
      12
    """


    yeni=[]
    for i in range(len(liste1)):
        yeni.append(liste1[i]*liste2[i])
    print sum(yeni)

doctest.testmod()
