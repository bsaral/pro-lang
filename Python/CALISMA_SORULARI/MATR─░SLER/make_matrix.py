#!/usr/bin/env python
# -*- coding: utf8 -*- 
import doctest

def make_matrix(satir,sutun):
    
    """
    >>> make_matrix(3, 5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> make_matrix(4, 2)
    [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    return [[0]*sutun]*satir
 
doctest.testmod()
