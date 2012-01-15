#!/usr/bin/env python
# -*- coding: utf8 -*- 



def histogram(dizgi):

    while True:
        kume=set(dizgi)

        for i in kume:
            print "%s harfinden = => %s tane" %(i, dizgi.count(i))
        break

