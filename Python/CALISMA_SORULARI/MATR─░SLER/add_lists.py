#!/usr/bin/env python
# -*- coding: utf8 -*- 
import doctest

def add_lists(*listeler):
    
    """
      >>> add_lists([1, 1], [1, 1])
      [2, 2]
      >>> add_lists([1, 2], [1, 4])
      [2, 6]
      >>> add_lists([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
    """


    print map (sum, zip(*listeler))

doctest.testmod()
