﻿import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def giyukAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)

def nieunAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.rt(90)
    t1.fd(size)
    t1.lt(90)
    t1.fd(100)

def mieumAt(x,y,size):
    giyukAt(x,y,size)
    t1.lt(90)
    nieunAt(x,y,size)


mieumAt(-50,50,100)