from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.listen()
screen.tracer(0)

left_paddle = Paddle(coordinates=(-350,0))
right_paddle = Paddle(coordinates=(350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.game_speed)
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(right_paddle.new_turtle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle.new_turtle) < 50 and ball.xcor() <= -320:
        ball.bounce_x()
        print(ball.speed())

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        

screen.exitonclick()