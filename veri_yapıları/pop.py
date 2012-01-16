# -*- coding: cp1254 -*-
class Stack:
    def __init__(self):
        self.liste=[]
    def push(self,eleman):
        self.liste.append(eleman)
        print self.liste

    def pop(self):
        try:
            self.liste.pop()
        except IndexError:
            print "liste zaten boş"

       
s=Stack()
s.pop()
        
