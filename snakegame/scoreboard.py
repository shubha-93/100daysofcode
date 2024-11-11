from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.score = 0
        self.high_score = self.get_high_score()
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            high_sc = file.read()
            file.close()
        return int(high_sc)
        
    def update_high_score(self):
        with open("data.txt",mode="w") as file:
            file.write(str(self.high_score))
            file.close()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.update_high_score()

    def refresh_score(self):
        self.score += 1
        self.update_scoreboard()