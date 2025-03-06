from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.highest_score = 0
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f'Highest Score: {self.highest_score} Score: {self.score}', move=False, align='center', font=('Aerial', 18, 'normal'))

    def update_scores(self):
        self.clear()
        self.write(f'Highest Score: {self.highest_score} Score: {self.score}', move=False, align='center', font=('Aerial', 18, 'normal'))

    def reset_game(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_scores()
        with open('highest_score.txt', mode='w') as highest_score_file:
            highest_score_file.write(f'{self.highest_score}')

    def score_increase(self):
        self.score += 1
        self.update_scores()






