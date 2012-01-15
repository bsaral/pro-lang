#!/usr/bin/env python
# -*- coding: utf8 -*-

def make_empty(seq):
   if type(seq)==list:
       print []
   elif type(seq)==str:
       print "' '"

   elif type(seq)==tuple:
        print ()

   else:
        print "yazım yanlışı bulunmaktadır."
