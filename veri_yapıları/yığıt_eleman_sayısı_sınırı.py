# -*- coding: cp1254 -*-
class Stack:
    def __init__(self):
        self.liste=[]
    def push(self,* eleman):
        self.liste.extend(eleman)
        if len(self.liste)>=4:
            print "bu y���t en fazla 4 elemandan olu�ur"
        else:
            print self.liste


    def pop(self):
        try:
            self.liste.pop()
        except IndexError:
            print "liste zaten bo�"

       
s=Stack()
s.push("4","5",True,False,"betul")
        
