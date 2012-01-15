#!/usr/bin/env python
# -*- coding: utf8 -*-
import turtle

isim=raw_input("\nadınızı giriniz : ")

parola=raw_input("\nparolanızı giriniz : ")

if bool(parola) == True :
	pass
else :
	print "\nPAROLANIZI GİRMENİZ GEREKİYOR."
	quit()


t=turtle
t.pensize(0)
t.penup()
t.goto(-180,0)
t.pendown()
t.speed("slow")

def kenar():
    
    t.forward(100)
    t.right(90)

def kenar2():
    t.forward(50)
    t.right(90)

def dongu():
    for i in range(2):
        kenar()
        kenar2()
		
t.color("white","#00FF00")    
t.begin_fill()
dongu()
t.end_fill()

t.penup()
t.goto(-90,0)
t.pendown()
t.color("white","#868A08")    
t.begin_fill()
dongu()
t.end_fill()

t.penup()
t.goto(0,0)
t.pendown()
t.color("white","#DF7401")    
t.begin_fill()
dongu()
t.end_fill()

t.penup()
t.goto(90,0)
t.pendown()
t.color("white","#DF0101")    
t.begin_fill()
dongu()
t.end_fill()

def git(uzaklik):
    t.penup()
    t.goto(-270,-60)
    t.forward(uzaklik)
    t.left(90)

def durum(puan):
	global durum
	print "parolanızın zorluk derecesi : %s"%(puan)


	
	
sor=parola.isalpha()

if sor == True :

	durum(puan="çok zayıf")
	git(uzaklik=130)
	quit()
	
else:
	pass

sor1=parola.isdigit()

if sor1 == True :
		
	durum(puan="orta")
	git(uzaklik=200)
	quit()
	
else:
	pass


		
liste1=["#","$","½","*","@","~","%","&","/","€","[","]","}","{","<",">","^^","^"]
liste2=["0","1","2","3","4","5","6","7","8","9"]
liste4=["e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","c","v","b","n","m"]



		
for i in parola :		

	if i in liste1  :
		durum(puan="çok zor")
		git(uzaklik=400)
		break
			
	else:
		durum(puan="zor")
		git(uzaklik=300)
		break
raw_input()

												
			# BETÜL SARAL        10.03.2011
