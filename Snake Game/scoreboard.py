from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score {self.score}", False, align="center", font=('Roboto', 24, 'normal'))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=('Roboto', 24, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as data:
                self.highscore = data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()