import turtle as t
import colorgram
import random

colors = colorgram.extract('image_hirst.jpg',25)

pen4o = t.Turtle()
my_screen = t.Screen()
my_screen.screensize(600,600)


all_colours = []
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb_color = (r, g, b)
    all_colours.append(rgb_color)

all_usable_colours = [(239, 229, 213), (203, 161, 18), (217, 155, 70), (242, 230, 236), (49, 104, 158), (207, 151, 182), (226, 207, 135), (187, 66, 39), (162, 29, 36), (29, 28, 69), (232, 240, 234), (36, 79, 40), (28, 67, 32), (143, 161, 183), (168, 43, 50), (76, 104, 77), (151, 30, 27), (150, 169, 152), (193, 93, 76), (219, 172, 193), (229, 174, 165), (181, 96, 102), (105, 125, 159), (51, 51, 88)]

def turn_into_rgb(color_list):
    right_colors = []
    for colour in all_colours:
        r1 = colour[0] / 255
        r2 = colour[1] / 255
        r3 = colour[2] / 255
        right_combo_colour = (r1, r2, r3)
        right_colors.append(right_combo_colour)
    return right_colors


make_rgb = turn_into_rgb(all_usable_colours)

# pen4o.hideturtle()
# pen4o.penup()
# pen4o.right(90)
# pen4o.forward(220)
# pen4o.right(90)
# pen4o.forward(230)
# pen4o.setheading(0)
# pen4o.speed("fastest")

# for i in range(1, 101):
#     random_colour = random.randint(0, len(all_usable_colours))
#     pen4o.dot(20,make_rgb[random_colour])
#     pen4o.forward(50)
#     if i % 10 == 0:
#         pen4o.penup()
#         pen4o.back(500)
#         pen4o.left(90)
#         pen4o.forward(50)
#         pen4o.right(90)


def draw_dot_matrix(dot_size, separation):
    pen4o.penup()
    pen4o.speed("fastest")
    pen4o.hideturtle()

    screen_width = my_screen.window_width()
    screen_length = my_screen.window_height()

    columns = screen_width // separation
    rows = screen_length // separation

    start_x = -screen_width // 2 + separation // 2
    start_y = screen_length // 2 - separation // 2

    for row in range(rows):
        for col in range(columns):
            x = start_x + col * separation
            y = start_y - row * separation
            pen4o.goto(x, y)
            pen4o.dot(dot_size, make_rgb[random.randint(0, len(all_usable_colours))])

draw_dot_matrix(20,50)


my_screen.exitonclick()