from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250,250)
        self.write(f"Level : {self.level}", align=ALIGNMENT,font=FONT)

    def increment_level(self):
        self.level +=1
        self.update_scoreboard()

    def game_over_sequence(self):
        self.goto(-50,0)
        self.write(f"GAME OVER", align=ALIGNMENT,font=FONT)


