import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
colors =['DeepSkyBlue','DarkOliveGreen']

for number in range(400):
    t.speed(3000)
    t.forward(number+1)
    t.right(89)
    t.pencolor(colors[number%2])

turtle.done()