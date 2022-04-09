import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

import colorgram

from random import randint

# from turtle import *
# #The * imports everything from the turtle module.

# import random as rd - Giving alias to a module.

Tom = Turtle()
Tom.shape('turtle')
# Tom.color("blue")


# Challenge 1 - Drawing a square

# for _ in range(4):
#     Tom.forward(190)
#     Tom.right(90)

# Challenge 2 - Draw a dotted line.

# for _ in range(50):
#     Tom.forward(10)
#     Tom.penup()
#     Tom.forward(10)
#     Tom.pendown()

# Challenge 3 - draw shapes of different sides:

colors = ["red", "green", "yellow", "orange", "blue", "black", "CornflowerBlue", "DarkOrchid", "IndianRed",
          "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def shape(sides):
#     angle= 360 / sides
#     for _ in range(sides):
#         Tom.forward(100)
#         Tom.right(angle)
#
#
# for i in range(3, 11):
#     Tom.color(random.choice(colors))
#     shape(i)

# Challenge 4 - Random Walk
# check thickness , speed,


# def move(dist, angl):
#     """moves by defined distance and turns to the defined angle"""
#     Tom.forward(dist)
#     Tom.right(angl)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     colour = (r, g, b)
#     return colour
#
# for i in range(90):
#     Tom.pensize(random.randint(5, 50))
#     Tom.speed(random.randint(0, 10))
#     #Tom.color(random.choice(colors))
#     Tom.pencolor(random_color())
#     angle = random.randint(0, 3)*90
#     distance = random.randint(50, 200)
#     move(distance, angle)


# Challenge 5 - Make a Spirograph

Tom.speed("fastest")

# def draw_spirograph(size_of_gap):
#     """Size of gap is the angle of tilt"""
#     for i in range(int(360/size_of_gap)):
#         Tom.pencolor(random_color())
#         Tom.circle(100)
#         #Tom.right(2)
#         Tom.setheading(Tom.heading()+ size_of_gap)


# draw_spirograph(10)

# Project - The Hirst painting

color_list = colorgram.extract('Hirst.jpeg', 60)
color_palette = []

for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_palette.append(new_color)

# for count in range(len(color_list)):
#     rgb = color_list[count]
#     color = rgb.rgb
#     color_palette.append(color)

# print(color_palette)

Tom.color(random.choice(color_palette))

# Tom.dot(20,random.choice(color_palette))

Tom.penup()
Tom.setheading(225)
Tom.forward(300)
Tom.setheading(0)


# My code


def filled_circle(size):
    colour = random.choice(color_palette)
    Tom.color(colour)
    Tom.fillcolor(colour)
    Tom.begin_fill()
    Tom.circle(size)
    Tom.end_fill()


def u_turn(radius, direction):
    for i in range(2):
        Tom.right(90 * direction)
        Tom.forward(radius * 10)


# def hirst(rows, columns, radius):
#     for row in range(rows):
#         for column in range(columns):
#             filled_circle(radius)
#             Tom.penup()
#             Tom.forward(radius * 10)
#         if row % 2 == 0:
#             u_turn(radius, 3)
#             Tom.right(90)
#             Tom.forward(radius*10)
#             Tom.left(90)
#         else:
#             u_turn(radius, 1)

def hirst(rows, columns, radius):
    for row in range(rows):
        for column in range(columns):
            Tom.dot(radius, random.choice(color_palette))
            # filled_circle(radius)
            # Tom.penup()
            Tom.forward(radius * 3.5)
        # Tom.penup()
        Tom.setheading(90)
        Tom.forward(radius * 3.5)
        Tom.setheading(180)
        Tom.forward(2.5 * radius ** 2 + radius)
        Tom.setheading(0)

        #
        # if row % 2 == 0:
        #     u_turn(radius, 3)
        #     Tom.right(90)
        #     Tom.forward(radius*10)
        #     Tom.left(90)
        # else:
        #     u_turn(radius, 1)


hirst(4, 4, 20)

screen = Screen()
screen.screensize(800, 800, "white")
screen.exitonclick()
