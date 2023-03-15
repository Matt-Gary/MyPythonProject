from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_right = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.score_left, False, align="center", font=('Roboto', 24, 'normal'))
        self.goto(100, 260)
        self.write(self.score_right, False, align="center", font=('Roboto', 24, 'normal'))

    def l_point(self):
        self.score_left += 1
        self.update_scoreboard()

    def r_point(self):
        self.score_right += 1
        self.update_scoreboard()