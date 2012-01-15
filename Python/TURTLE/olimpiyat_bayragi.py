#!/usr/bin/env python
# -*- coding: utf8 -*-
import turtle
t=turtle
t.pensize(10)
t.speed("fast")
t.penup()
t.goto(-180,90)
t.pendown()

def cember(yaricap ,aci,renk):
    t.pencolor(renk)
    t.circle(yaricap,aci)

cember(yaricap=100, aci=360,renk="blue")

t.penup()
t.goto(60,90)
t.pendown()

cember(yaricap=100,aci=360,renk="black")

t.penup()
t.goto(300,90)
t.pendown()
cember(yaricap=100,aci=360,renk="red")
        

t.penup()
t.goto(-60,-30)
t.pendown()
cember(yaricap=100, aci=360,renk="yellow")

t.penup()
t.goto(180,-30)
t.pendown()
cember(yaricap=100,aci=360,renk="green")
import time
time.sleep(5)

                            #BETÜL SARAL     09.03.2011

