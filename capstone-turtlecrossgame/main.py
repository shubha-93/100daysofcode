import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

car_manager = CarManager()
scoreboard = Scoreboard()

new_player = Player()
screen.onkey(new_player.player_move,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    screen.update()

    for car in car_manager.all_cars:
        if new_player.distance(car) < 25:
            scoreboard.game_over_sequence()
            screen.mainloop()
        
    if new_player.ycor() >= 250:
        new_player.goto_start_position()
        scoreboard.increment_level()
        car_manager.move_increment += 5
