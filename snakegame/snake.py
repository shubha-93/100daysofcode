from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.color("white")
        new_turtle.speed("fastest")
        self.segments.append(new_turtle)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
        
    def create_snake(self):
        for item in STARTING_POSITIONS:
            self.add_segment(item)

    def reposition_snake(self):
        for item in range(len(self.segments)-1,0,-1):
            x_pos = self.segments[item-1].xcor()
            y_pos = self.segments[item-1].ycor()
            self.segments[item].goto(x_pos,y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
            self.reposition_snake()

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
            self.reposition_snake()

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
            self.reposition_snake()

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
            self.reposition_snake()

    


