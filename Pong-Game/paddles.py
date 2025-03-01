from turtle import Turtle


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.penup()
        self.goto(position)

    def upward(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def downward(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)


