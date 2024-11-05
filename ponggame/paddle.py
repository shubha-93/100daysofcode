from turtle import Turtle

class Paddle:
    def __init__(self, coordinates):
        self.new_turtle = Turtle(shape="square")
        self.new_turtle.color("white")
        self.new_turtle.shapesize(stretch_len=5,stretch_wid=1)
        self.new_turtle.setheading(90)
        self.new_turtle.penup()
        self.new_turtle.goto(coordinates)

    def down(self):
        xcor = self.new_turtle.xcor()
        ycor = self.new_turtle.ycor()
        ycor -= 20
        self.new_turtle.goto(xcor,ycor)

    def up(self):
        xcor = self.new_turtle.xcor()
        ycor = self.new_turtle.ycor()
        ycor += 20
        self.new_turtle.goto(xcor,ycor)