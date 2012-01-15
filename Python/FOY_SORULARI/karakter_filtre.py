#!/usr/bin/env python
# -*- coding: utf8 -*- 


def kopyala():
    
    ac = open("deneme2.py", "r")
    copy = open("deneme2.txt","w")
    
    for i in ac:
        copy.write(i)
    copy.close()

kopyala()

       
        
        

    
            
