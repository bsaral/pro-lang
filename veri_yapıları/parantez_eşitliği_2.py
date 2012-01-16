# -*- coding: cp1254 -*-
class Stack():
    def __init__(self):
        self.liste=[]

    def bos(self):
        return self.liste==[]
    def ekle(self,n):
        self.liste.append(n)
    def pop(self,n=None):
        return self.liste.pop()



def checker(s):
    a=Stack()
    deger=True
    say=0
    for i in s:
        if deger:
            if i in "([{":
                a.ekle(i)
                say+=1
            else:
                if a.bos():
                    deger=False
                    break
                else:
                    c=a.pop()
                    say+=1
                    if not esle (c,i):
                        deger=False
    if deger and a.bos():
        print "parantezler eşit\n"
    else:
        if (say-1)>=len(s)-1:
            print say-len(s),". yerde hata var"
            if s[say-len(s)] == "(":
                print "açılan parantez kapatılmamış.\n"
            elif s[say-len(s)] == "[":
                print "açılan köşeli parantez kapatılmamış.\n"
            else:
                print "açılan küme parantezi kapatılmamış.\n"
    
        else:
            print (say),". yerde hata var."
            if s[say-len(s)] == "(":
                print "parantez açılmadan kapatılmış\n"
            elif s[say-len(s)] == "[":
                print "köşeli parantez açılmadan kapatılmış\n"
            else:
                print "küme parantezi açılmadan kapatılmış.\n"

def esle(open,close):
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)




checker('(}')
checker('()}')
checker('{()}')
checker('[{()}')
checker('[]{()}')

                
