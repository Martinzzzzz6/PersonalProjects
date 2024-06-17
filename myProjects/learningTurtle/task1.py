import turtle as t
import random

ivo = t.Turtle()
t.colormode(255)

screen = t.Screen()
screen.bgcolor("black")
screen.screensize(100,100)

ivo.color("white")
ivo.shape(None)

def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)

    return random_colour



def dashed_line():
    for i in range(10):
        ivo.forward(10)
        ivo.penup()
        ivo.forward(10)
        ivo.pendown()

directions = [0, 90, 180, 270]

def many_figures(number_sizes):
    angle = round(360 / number_sizes, 1)
    pick_colour = random.choice(colors)
    for i in range(number_sizes):
        ivo.color(pick_colour)
        ivo.forward(100)
        ivo.right(angle)

def random_movements():
    for _ in range(300):
        ivo.pensize(10)
        ivo.color(random_rgb())
        ivo.setheading(random.choice(directions))
        ivo.forward(50)
        ivo.speed(0)

def make_spirograph(set_degree):
    ivo.speed(10.5)
    ivo.shape("turtle")
    iterations = int(360 / set_degree)
    for _ in range(iterations + 1):
        ivo.color(random_rgb())
        ivo.circle(100)
        get_head = ivo.heading()
        ivo.setheading(get_head + set_degree)

make_spirograph(5)
screen.exitonclick()