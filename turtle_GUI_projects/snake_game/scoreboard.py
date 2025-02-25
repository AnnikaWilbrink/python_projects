from turtle import Turtle
import os

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(f"{LOCATION}/highscore.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.update_scoreboard()
        self.hideturtle()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(f"{LOCATION}/highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()