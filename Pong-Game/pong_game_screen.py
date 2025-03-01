from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game(Udemy)')
screen.tracer(0)

right_paddle = Paddles((350, 0))
left_paddle = Paddles((-350, 0))
pong_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.upward, "Up")
screen.onkey(right_paddle.downward, "Down")

screen.onkey(left_paddle.upward, "w")
screen.onkey(left_paddle.downward, "s")

game_on = True

scoreboard.line_middle()
ball_speed = 0.1
while game_on:
    pong_ball.movements()
    if ball_speed <= 0:
        time.sleep(0.01)
    else:
        time.sleep(ball_speed)

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_frame()

    if (pong_ball.xcor() > 310 and pong_ball.distance(right_paddle) < 50 or
            pong_ball.xcor() < -310 and pong_ball.distance(left_paddle) < 50):
        ball_speed -= 0.01
        pong_ball.bounce_paddles()

    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.left_score_update()

    if pong_ball.xcor() < -380:
        scoreboard.right_score_update()
        pong_ball.reset_position()

    screen.update()


screen.exitonclick()


