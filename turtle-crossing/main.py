import time
from turtle import Screen, Turtle
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Detect player has reached other side
    if player.crossed():
        player.goto_starting_line()
        car_manager.level_up()
        scoreboard.increase_score()


screen.exitonclick()





