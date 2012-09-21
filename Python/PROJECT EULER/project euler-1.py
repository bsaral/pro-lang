#!/usr/bin/env python
#-*- coding: utf-8 -*-

##################################################################################################
# PROJECT EULER 1                                                                                #
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.#
# The sum of these multiples is 23.                                                              #
# Find the sum of all the multiples of 3 or 5 below 1000.                                        #   
#                                                                                                #
# 1000 altında olan 3 ve 5 bölünebilen doğal sayılar toplamı ?                                   #
#                                                                                                #
##################################################################################################

numbers = range(1, 1000, 1)
print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))

if __name__ == "__main__":
    import doctest
    doctest.testmod()    

