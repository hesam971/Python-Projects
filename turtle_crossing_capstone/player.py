from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.x_coordination = 0
        self.y_coordination = -280
        self.turtle_self()

    def turtle_self(self):
        self.goto(self.x_coordination, self.y_coordination)

    def moving_turtle_up(self):
        self.goto(self.x_coordination, self.y_coordination)
        self.y_coordination += 10

    def moving_turtle_down(self):
        self.goto(self.x_coordination, self.y_coordination)
        self.y_coordination -= 10

    def reset_player(self):
        self.x_coordination = 0
        self.y_coordination = -280
        self.turtle_self()
