# -*- coding: cp1254 -*-
import math

class Fraction:
    def __init__(self,pay,payda):
        self.pay=pay
        self.payda=payda

    def topla(self,f):
        pay1=self.pay*f.payda+self.payda*f.pay
        payda1=self.payda*f.payda
        a=float(pay1)/float(payda1)
        if a-int(a)< 0.5 :
            b=math.floor(a)
        else:
            b=math.ceil(a)
        print "kesirler toplami=", b
    def kare(self):
        c=(self.pay**2)
        d=(self.payda**2)
        tam=c/d
        print "karesi alinmis kesrin sekli=",c,"/",d
        if tam-int(tam)< 0.5 :
            b=math.floor(tam)
        else:
            b=math.ceil(tam)
        print "tam hali = ",b
        
        

        
f1=Fraction(12,8)
f2=Fraction(1,2)
f3=f1.topla(f2)
f1.kare()
