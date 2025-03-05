from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f'Score: {self.score}', move=False, align='center', font=('Aerial', 18, 'normal'))

    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', move=False, align='center', font=('Aerial', 18, 'normal'))

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write('GAME OVER', move=True, align='center', font=('Aerial', 18, 'normal'))




