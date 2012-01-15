#!/usr/bin/env python
# -*- coding: utf8 -*- 

def max_sparse_matrix(matris):
    sozluk={(0, 3): 1, (2, 1): 2, (4, 3): 3}
    liste=[]
    for i in sozluk.values():
        liste.append(i)
    print "matristeki en büyük eleman :",max(liste)



max_sparse_matrix([[0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0],
                   [0, 2, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 3, 0]])

