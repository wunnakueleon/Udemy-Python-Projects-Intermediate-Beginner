from turtle import Turtle, Screen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    #       self.current_x = self.xcor()
    #       self.current_y = self.ycor()
    #       self.x_coordinate_distance = self.current_x - self.initial_x
    #       self.y_coordinate_distance = self.current_y - self.current_x
    #       self.movements()

    def movements(self):
        increase_x = self.xcor() - self.move_x
        increase_y = self.ycor() - self.move_y
        self.goto(increase_x, increase_y)

    def bounce_frame(self):
        self.move_y *= -1

    def bounce_paddles(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move_x *= -1



# Use Pythagoras theorem, find side lengths and find tangent, convert it to degree, then reflect that on the other side.

"""
def ball_bouncing(self, screen, math):
    tangent_x = math.ceil(self.x_coordinate_distance / self.y_coordinate_distance)
    degree = math.degree(math.atan(tangent_x))    def ball_bouncing(self, screen, math):    
"""



