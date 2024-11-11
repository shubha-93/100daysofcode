from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.02)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.refresh_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    for item in snake.segments[1:]:
        if snake.head.distance(item) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()