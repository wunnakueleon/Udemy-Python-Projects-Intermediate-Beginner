from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.speed('fastest')
        self.color('green')
        self.food_refresh()

    def food_refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 260))
