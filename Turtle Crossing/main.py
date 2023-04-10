import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import create_world

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
turtle.fillcolor("green")
screen.register_shape("carleft.gif")
car_manager = CarManager()
screen.listen()
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")
screen.onkey(turtle.move_left, "Left")
screen.onkey(turtle.move_right, "Right")
scoreboard = Scoreboard()
screen.bgcolor("black")
create_world()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False
    if turtle.ycor() > 230:
        turtle.reset()
        car_manager.speed_up()
        scoreboard.increase_score()

screen.exitonclick()
