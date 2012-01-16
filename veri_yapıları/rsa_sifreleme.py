# -*- coding: cp1254 -*-
import random
import string
import math

def gcd (a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
   

def ext_gcd(x,y):
    if y==0:
        return (x,1,0)
    else:
        (d,a,b)=ext_gcd(y,x%y)
        return (d,b,a-(x/y)*b)

def modexp(number,exp,mod):
    if exp == 0:
        return 1
    elif not exp % 2:
       return modexp((number**2)%mod,exp/2,mod) % mod
    else:
        return number*modexp(number,exp-1,mod) % mod

def RSAgenkeys(p,q,m,size):
    #p ve q ile e,d,t,n bulunması
    n=p*q
    t=(p-1)*(q-1)
    e=int(random.random()*n)
    while True:
        if gcd(t,e)==1:
            break
        else:
            e=int(random.random()*n)
    d,a,b=ext_gcd(t,e)
    if b<0:
        d=t+b
    else:
        d=b
    print ((e,d,n))
    
    #karakter dizisi olarak girilen bölümün şifrelenmesi
    #chunk bölümü
    liste,liste2=[],[]
    for i in m:
        liste.append(str(ord(i)))
    dizi=string.join(liste,"")
    for i in range((len(dizi)/size)):
        bas=i*size
        son=bas+size
        liste2.append(int(dizi[bas:son]))
    sifreli_liste=[]
    for i in liste2:
        sifreli_liste.append(str(modexp(float(i),e,n)))
    sifreli_metin=string.join(sifreli_liste,"")
    print sifreli_metin


RSAgenkeys(8,7,"helloworld",5)

    

