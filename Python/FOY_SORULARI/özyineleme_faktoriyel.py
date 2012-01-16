#!/usr/bin/env python
# -*- coding: utf8 -*-
import math
def fakt(sayi):
    if sayi>=0:
        if sayi==0:
            return 1
        else:
            return sayi*fakt(sayi-1)

    else:
        return "negatif tamsayilarin faktoriyel hesabi yapilmaz."
