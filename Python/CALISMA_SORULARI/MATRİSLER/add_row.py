#!/usr/bin/env python
# -*- coding: utf8 -*- 

import doctest

def add_row(matris):
     """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """


    print matris+[[0]*len(matris[0])]

doctest.testmod()
