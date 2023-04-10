STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
CURRENT_POSITION_X = 0
CURRENT_POSITION_Y = -280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move_up(self):
        CURRENT_POSITION_Y = self.ycor() + 10
        self.goto(self.xcor(), CURRENT_POSITION_Y)

    def move_down(self):
        CURRENT_POSITION_Y = self.ycor() - 10
        self.goto(self.xcor(), CURRENT_POSITION_Y)

    def move_left(self):
        CURRENT_POSITION_X = self.xcor() - 10
        self.goto(CURRENT_POSITION_X, self.ycor())

    def move_right(self):
        CURRENT_POSITION_X = self.xcor() + 10
        self.goto(CURRENT_POSITION_X, self.ycor())

    def reset(self):
        self.goto(STARTING_POSITION)
