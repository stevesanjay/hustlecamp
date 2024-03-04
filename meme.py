import turtle

# Setting up the screen
screen = turtle.Screen()
screen.title("Vadivelu Meme Style Cartoon")

# Creating turtle object
t = turtle.Turtle()
t.speed(1)

# Drawing a simple face
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# Drawing the eyes
for eye in (-35, 35):
    t.penup()
    t.goto(eye, 50)
    t.pendown()
    t.circle(10)

# Drawing a smile
t.penup()
t.goto(-40, 20)
t.pendown()
t.setheading(-60)
t.circle(40, 120)

# Finishing up
t.hideturtle()
turtle.done()
