from turtle import Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
game_over = False
screen.tracer(0)
player = Player()
car_manager = Car_Manager()
scoreboard = ScoreBoard()
screen.onkey(player.moving_turtle_up, "Up")
screen.onkey(player.moving_turtle_down, "Down")
screen.listen()

while not game_over:
    time.sleep(0.1)
    screen.update()
    car_manager.first_car()
    car_manager.moving_car()
    if player.ycor() > 270:
        player.reset_player()
        scoreboard.increase_score()
        car_manager.speed_cars()

    for car in car_manager.cars:
        if player.distance(car) < 15:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
