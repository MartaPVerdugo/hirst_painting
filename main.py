import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
rgb_colours = [(220, 219, 214), (222, 61, 89), (132, 64, 77),
               (86, 79, 143), (204, 130, 145), (104, 103, 168), (42, 40, 46), (89, 49, 61), (225, 92, 88),
               (186, 167, 164), (64, 40, 48), (153, 151, 179)]


def set_turtle_position():
    list_y_coordinates = []
    for position in range(-200, 300, 50):
        list_y_coordinates.append(position)
    return list_y_coordinates


def draw_painting():
    for y_coordinate in set_turtle_position():
        print(y_coordinate)
        tim.penup()
        tim.setx(-200)
        tim.sety(y_coordinate)
        for each_dot in range(10):
            tim.dot(20, random.choice(rgb_colours))
            tim.forward(50)


draw_painting()

screen = Screen()
screen.exitonclick()
screen.setup(10, 10)

# import colorgram
# colours = colorgram.extract('spots.jpg', 15)

# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
