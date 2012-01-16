#!/usr/bin/env python
# -*- coding: utf8 -*- 

def add_column(*matris):
     """
>>> m = [[0, 0], [0, 0]]
>>> add_column(m)
[[0, 0, 0], [0, 0, 0]]
>>> n = [[3, 2], [5, 1], [4, 7]]
>>> add_column(n)
[[3, 2, 0], [5, 1, 0], [4, 7, 0]]
>>> n
[[3, 2], [5, 1], [4, 7]]
"""


     for i in matris:
        for j in i:
            j.append(0)
     print matris

#--------------------------------------------------------------------------


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


#-----------------------------------------------------------------------------


def add_matrices(m1,m2):
    yeni1=[]
    for i in m1:
        c=m1.index(i)
    for j in m2:
        d=m2.index(j)

        if c==0 or d==0:
            ilk=map(sum,zip(m1[0],m2[0]))
       
        elif c==d:
            iki= map(sum,zip(m1[c],m2[d]))
            print [ilk,iki]
   
       
            
            
m1=[[1,2],[3,4]]
m2=[[2,3],[5,6]]
add_matrices(m1,m2)


#------------------------------------------------------------------------------



def add_row(matris):
     """
>>> m = [[0, 0], [0, 0]]
>>> add_row(m)
[[0, 0], [0, 0], [0, 0]]
>>> n = [[3, 2, 5], [1, 4, 7]]
>>> add_row(n)
[[3, 2, 5], [1, 4, 7], [0, 0, 0]]
>>> n
[[3, 2, 5], [1, 4, 7]]
"""


     print matris+[[0]*len(matris[0])]



#------------------------------------------------------------------------------


def make_matrix(satir,sutun):
    
    """
>>> make_matrix(3, 5)
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
>>> make_matrix(4, 2)
[[0, 0], [0, 0], [0, 0], [0, 0]]
"""
    
    return [[0]*sutun]*satir



#-----------------------------------------------------------------------------

def mult_lists_kisa_yol(liste1,liste2):
     """
>>> mult_lists([1, 1], [1, 1])
2
>>> mult_lists([1, 2], [1, 4])
9
>>> mult_lists([1, 2, 1], [1, 4, 3])
12
"""


     print sum(map(lambda i,j:i*j,liste1,liste2))


#------------------------------------------------------------------------------


def mult_lists_uzun_yol(liste1,liste2):
     """
>>> mult_lists([1, 1], [1, 1])
2
>>> mult_lists([1, 2], [1, 4])
9
>>> mult_lists([1, 2, 1], [1, 4, 3])
12
"""


     yeni=[]
     for i in range(len(liste1)):
        yeni.append(liste1[i]*liste2[i])
     print sum(yeni)



#------------------------------------------------------------------------------
