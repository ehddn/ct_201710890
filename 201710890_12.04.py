import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
x1=0.0-320
x2=0.0
x3=0.0+320

y1=0.0-120
y2=0.0
y3=0.0+120

def drawSquareAt(x,y,size,color):
    t1.penup()
    t1.goto(x,y,)
    t1.pendown()
    t1.fillcolor(color)
    t1.begin_fill()
    for i in range(4):
        t1.fd(size)
        t1.rt(90)
        t1.fd(size)
    t1.end_fill()
        
def drawTriangleAt(x,y,size,color):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fillcolor(color)
    t1.begin_fill()
    for i in range(3):
        t1.fd(size)
        t1.rt(120)
    t1.end_fill()
def drawStarAt(x,y,size,color):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fillcolor(color)
    t1.begin_fill()
    for i in range(5):
        t1.fd(size)
        t1.rt(144)
    t1.end_fill()

drawSquareAt(x1,y1,100,"red")
drawTriangleAt(x2,y2,100,"yellow")
drawStarAt(x3,y3,100,"green")




wn.exitonclick()
