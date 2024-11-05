from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(0,-400)
        self.setheading(90)
        self.forward(800)
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.game_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.game_speed *= 0.9
            
    def reset(self):
        self.goto(0,0)
        self.game_speed = 0.1
        self.bounce_x()
            
            


## If ycor >= 300 or ycor <-= -300 => collision with wall
## if the top ycor = 300 is hit then return balls heading for now