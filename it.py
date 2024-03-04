import turtle

# Initialize Turtle Screen
screen = turtle.Screen()
screen.title("Timeline Bar Chart")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(1)

def draw_axis():
    # Draw the timeline axis
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()
    pen.forward(400)
    pen.penup()

def draw_bar(x, height, label):
    # Draw a single bar
    pen.goto(x, 0)
    pen.pendown()
    pen.left(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(40)  # Width of the bar
    pen.right(90)
    pen.forward(height)
    pen.left(90)
    pen.penup()
    
    # Label the bar
    pen.goto(x + 20, height + 10)
    pen.write(label, align="center")

# Draw the axis
draw_axis()

# Example data: (position, height, label)
data = [(-150, 100, 'Event 1'), (-50, 150, 'Event 2'), (50, 120, 'Event 3'), (150, 80, 'Event 4')]

# Draw bars
for x, height, label in data:
    draw_bar(x, height, label)

# Hide turtle and finish
pen.hideturtle()
turtle.done()
