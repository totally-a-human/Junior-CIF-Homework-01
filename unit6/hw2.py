import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
t.fillcolor("red")
t.shape('circle')
t.shapesize(1.5)
t.speed(4)

t.penup()
t.goto(200,-200)
t.pendown()

t.begin_fill()
for i in range (4):
    t.forward(100)
    t.right(90)
t.end_fill()

turtle.fillcolor("white")
t.penup()
t.forward(50)
t.pendown()
t.left(90)
t.speed(10)
for i in range (50):
    t.forward(8)
    t.left(1)
t.done()