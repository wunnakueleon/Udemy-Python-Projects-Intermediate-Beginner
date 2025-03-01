# This is a code of block that extracts colors from the image. Then, getting that resulted color list, it is utilized
# in the project below...

from turtle import *
import random

available_colors = [(247, 241, 222), (108, 98, 83), (35, 29, 20), (167, 154, 131), (236, 228, 99), (20, 20, 27), (104, 81, 99), (41, 30, 35), (249, 249, 252), (150, 141, 84), (252, 248, 250), (239, 247, 243), (143, 160, 196), (154, 171, 160), (78, 74, 34), (87, 92, 104), (16, 22, 17), (89, 100, 94), (163, 151, 158), (78, 55, 64), (168, 206, 188), (106, 44, 33), (161, 184, 231), (149, 120, 111), (112, 121, 153), (57, 58, 77), (116, 136, 123), (139, 120, 129), (223, 182, 166), (57, 68, 59), (115, 134, 136), (207, 181, 189), (218, 220, 31), (163, 204, 207), (55, 69, 72)]
print(len(available_colors))


screen = Screen()
screen.bgcolor('pink')
hideturtle()

shape('classic')
x_coordinate = -100
y_coordinate = 0
colormode(255)
pensize(5)


def dots():
    for i in range(10):
        dot(11, random.choice(available_colors))
        forward(20)


penup()

for turtle in range(9):

    goto(x_coordinate, y_coordinate)
    dots()
    y_coordinate += 20


screen.exitonclick()
