from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car_Manager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def first_car(self):
        if 1 == random.randint(0, 6):
            turtle = Turtle("square")
            turtle.color(random.choice(COLORS))
            turtle.shapesize(stretch_wid=0.8, stretch_len=1.7)
            turtle.penup()
            y_coordinate = random.randint(-235, 235)
            turtle.goto(280, y_coordinate)
            self.cars.append(turtle)

    def moving_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_cars(self):
        self.car_speed += MOVE_INCREMENT
