#!/usr/bin/env python
# -*- coding: utf8 -*- 
from __future__ import division
import math

def yuvarlama(sayi):
    if sayi-int(sayi)>=0.5:
        print math.ceil(sayi)

    else :
        print math.floor(sayi)
        
        
        
    
