import turtle
import random

turtle.bgcolor('black')
t = turtle.Turtle()

def read_color_file():

    colors = []

    with open('colors.txt') as f:
        colors = f.readlines()

    # clearnup (remove \n in each color)
    new_colors = []
    for color in colors:
        new_colors.append(color.strip())

    return new_colors

def get_colors():

    total_colors = read_color_file()
    random_colors = random.sample(total_colors, 2)

    print(f'random_colors: {random_colors}')

    return random_colors

colors = get_colors()

for number in range(400):
    t.speed(3000)
    t.forward(number+1)
    t.right(89)
    t.pencolor(colors[number%2])

turtle.done()