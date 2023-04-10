FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.level = 0
            self.penup()
            self.goto(-220, 250)
            self.color("white")
            self.write(f"LEVEL: {self.level}", False, align="center", font=FONT)
            self.hideturtle()

        def game_over(self):
            self.goto(0, 0)
            self.color("white")
            self.write(f"GAME OVER", False, align="center", font=FONT)

        def increase_score(self):
            self.level += 1
            self.color("white")
            self.clear()
            self.write(f"LEVEL: {self.level}", False, align="center", font=FONT)
