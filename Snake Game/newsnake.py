from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.direction_change = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head=self.snakes[0]

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for snake_number in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_number - 1].xcor()
            new_y = self.snakes[snake_number - 1].ycor()
            self.snakes[snake_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.direction_change += 1

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.direction_change += 1
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.direction_change += 1
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.direction_change += 1