# -*- coding: cp1254 -*-
class Stack:
    def __init__(self):
        self.liste=[]
    def push(self,* eleman):
        self.liste.extend(eleman)
        if len(self.liste)>=4:
            print "bu yığıt en fazla 4 elemandan oluşur"
        else:
            print self.liste


    def pop(self):
        try:
            self.liste.pop()
        except IndexError:
            print "liste zaten boş"

       
s=Stack()
s.push("4","5",True,False,"betul")
        
