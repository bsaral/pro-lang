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


    print sum(map(lambda i,j:i*j,liste1,liste2))

doctest.testmod()
