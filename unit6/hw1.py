side=int(input("Enter the number of sides of the polygon: "))
length=int(input("Enter the length of each side: "))
angle=int(360/side)
import turtle
s =turtle.Screen()
t = turtle.Turtle()
for i in range (side):
    t.forward(length)
    t.right(angle)
t.exitonclick()