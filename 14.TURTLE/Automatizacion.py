import turtle
s=turtle.Screen()
t=turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

i=0

while i<=100:
    t.circle(i)
    i+=10

turtle.done()