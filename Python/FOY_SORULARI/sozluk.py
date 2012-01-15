#!/usr/bin/env python
# -*- coding: utf8 -*-
def sozluk(arg):
    sehirler={'Samsun': 'Karad', 'Antalya': 'Akd',
                'Tokat': 'Karad', 'Manisa': 'Ege'}

    for i in sehirler:
        if sehirler.get(i)==arg:
            print i
