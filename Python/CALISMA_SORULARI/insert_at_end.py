#!/usr/bin/env python
# -*- coding: utf8 -*-

def insert_at_end(val,seq):
    if type(seq)==list:
        seq.append(val)
        print seq

    elif type(seq)==str:
        print seq+val

    elif type(seq)==tuple:
        print seq[:]+(val,)

    else:
        print "yazım yanlışı bulunmaktadır."
