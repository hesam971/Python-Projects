from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.random_coordinate()

    def random_coordinate(self):
        x_random = random.randint(-230, 230)
        y_random = random.randint(-230, 230)
        self.goto(x_random, y_random)
        