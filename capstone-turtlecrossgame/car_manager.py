from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_increment = MOVE_INCREMENT

    def create_car(self):
        random_chance = random.randint(1,7)
        if random_chance == 1:
            self.new_car = Turtle()
            self.new_car.shape("square")
            self.new_car.shapesize(stretch_len=2,stretch_wid=1)
            self.new_car.setheading(180)
            self.new_car.speed("slowest")
            self.new_car.penup()
            self.new_car.color(random.choice(COLORS))
            self.new_car.starting_x = 280
            self.new_car.starting_y = random.randint(-200,200)
            self.new_car.goto(self.new_car.starting_x,self.new_car.starting_y)
            self.new_car.forward(STARTING_MOVE_DISTANCE)
            self.all_cars.append(self.new_car)

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() > -350:
                car.forward(self.move_increment)

