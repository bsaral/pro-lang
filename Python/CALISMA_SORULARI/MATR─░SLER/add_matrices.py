#!/usr/bin/env python
# -*- coding: utf8 -*- 

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


