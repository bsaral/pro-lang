#!/usr/bin/env python
# -*- coding: utf8 -*-
import os

def say(yol):
    a,b=0,0
    
    for dosya in os.walk(yol):
        a+=1
       
        for f in dosya:
            
            
            if f ==[] or f==yol or f==["desktop.ini"]:
                pass
            
            else:
                for i in f :
                    if i.endswith(".py")  or i.endswith(".txt") or i.endswith(".docx"):
                        b+=1
                    if i.endswith(".rtf")or i.endswith(".jnt"):
                        b+=1

    print "klasör sayısı=",a,"dosya sayısı=",b
   
               
               
                
            

        
              
        
    

            
        
        
