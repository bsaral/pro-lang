#!/usr/bin/env python
# -*- coding: utf8 -*- 

def add_sparse_matrix():
    sozluk1={(0, 3): 1, (2, 1): 2, (4, 3): 3}
    sozluk2={(0, 1): 5, (2, 2): 8, (1, 1): 5}
    toplam=0
    for i in sozluk1.values():
        toplam+=i
    for j in sozluk2.values():
        toplam+=j
    print toplam
