from turtle import Turtle

LINE = [200, 80, -40, -160, -200]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def line_middle(self):
        self.color('white')
        for y in LINE:
            self.setheading(270)
            self.penup()
            self.goto(0, y)
            self.pendown()
            self.goto(0, y + 100)

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))
        self.line_middle()

    def left_score_update(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_score_update(self):
        self.right_score += 1
        self.update_scoreboard()



