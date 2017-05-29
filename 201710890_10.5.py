import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

x1=0.0-320
x2=0.0
x3=0.0+320

def drawTriangleAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(300)
    t1.pendown()
    t1.fd(size)
    t1.setheading(180)
    t1.fd(size)
    t1.setheading(60)
    t1.fd(size)
 
def drawPentagon(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.pendown()
    t1.setheading(288)
    t1.fd(size)
    t1.setheading(216)
    t1.fd(size)
    t1.setheading(144)
    t1.fd(size)
    t1.setheading(72)
    t1.fd(size)
    t1.setheading(0)
    t1.fd(size)

def drawStarAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.pendown()
    for i in range(5):
        t1.fd(100)
        t1.rt(144)

drawTriangleAt(100,x1)
drawPentagon(100,x2)
drawStarAt(100,x3)

