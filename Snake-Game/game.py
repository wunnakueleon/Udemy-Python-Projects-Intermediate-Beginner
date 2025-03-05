from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake Game')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.segments[0].distance(food) < 20:
        food.food_refresh()
        snake.extend_snake()
        scoreboard.score_increase()

    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        scoreboard.game_over()
        game_is_on = False

    for each_seg in snake.segments[1:]:
        if snake.segments[0].distance(each_seg) < 10:
            scoreboard.game_over()
            game_is_on = False























screen.exitonclick()

