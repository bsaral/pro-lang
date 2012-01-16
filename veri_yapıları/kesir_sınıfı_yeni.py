# -*- coding: cp1254 -*-

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

class Fraction:
   
    def __init__(self,pay,payda):
        son=gcd(pay,payda)
        self.py=pay/son
        self.pyd=payda/son
        

    def __str__(self):
        return str(self.py)+"/"+str(self.pyd)
    

    def __add__(self,f):
        newpy=(self.py*f.pyd)+(self.pyd*f.py)
        newpyd=self.pyd*f.pyd
        print Fraction(newpy,newpyd)

    def __pow__(self,n):
        newpy=self.py**n
        newpyd=self.pyd**n
        print Fraction(newpy,newpyd)

    def __abs__(self):
        newpy=abs(self.py)
        newpyd=abs(self.pyd)
        print Fraction(newpy,newpyd)
        
    def __float__(self):
       return float(self.py)/float(self.pyd)

    def __cmp__(self,other):
        new1=self.py*other.pyd
        new2=self.pyd*other.py
        if new1==new2:
            print -1
        elif new1<new2:
            print 0
        else:
            print 1
            
            
    def __eq__(self,other):

        #iki kesrin eşit olup olmadığına bakar.
        
        new1=self.py*other.pyd
        new2=self.pyd*other.py
        if new1==new2:
            print -1
        else:
            print 0

            
    def min_max(self,liste):

        #liste içerisindeki min,max kesir değerlerini bulur.
        
        liste.append(self)
        liste2=[]
        for i in liste:
            liste2.append(float(i))
        print "listedeki en büyük eleman = ",liste[liste2.index(max(liste2))]
        print "listedeki en küçük eleman = ",liste[liste2.index(min(liste2))]

       
        
        
   
            
        
       

f1=Fraction(-1,4)
f2=Fraction(1,2)
f4=Fraction(3,8)
f3=f1+f2
f3=f1**3
f3=f2**5
f3= abs(f1)
f3=float(f2)
f3=f1.__cmp__(f2)
f3=f1==f2
f3=f1.min_max([f2,f4])

        

