from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_coordination = 10
        self.y_coordination = 10
        self.ball_speed = 0.1

    def ball_move(self):
        x_cor = self.xcor() + self.x_coordination
        y_cor = self.ycor() + self.y_coordination
        self.goto(x_cor, y_cor)

    def y_bounce(self):
        self.y_coordination *= -1

    def x_bounce(self):
        self.x_coordination *= -1
        self.ball_speed *= 0.9

    def rest_position(self):
        self.home()
        self.ball_speed = 0.1
        self.x_bounce()
