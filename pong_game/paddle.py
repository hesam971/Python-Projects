from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.paddle_stick(position)

    def paddle_stick(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=4, stretch_len=0.5)

    def up(self):
        y_pos = self.ycor() + 20
        self.setposition(self.xcor(), y_pos)

    def down(self):
        y_pos = self.ycor() - 20
        self.setposition(self.xcor(), y_pos)
