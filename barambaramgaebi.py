import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def baram(size):
    for i in range(1,9,1):
        t1.fd(size)
        t1.rt(90)
        t1.fd(size)
        t1.penup()
        t1.home()
        t1.setheading(45*i)
        t1.pendown()
baram(100)
   
