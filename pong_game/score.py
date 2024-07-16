from turtle import Turtle


class Score(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.score_number = 0
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.score_coordinate(x_coordinate, y_coordinate)

    def score_coordinate(self, x_coordinate, y_coordinate):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x_coordinate, y_coordinate)
        self.write(f"Score: {self.score_number}", True, align="center", font=('Arial', 28, 'normal'))

    def change_score(self):
        self.score_number += 1
        self.clear()
        self.score_coordinate(self.x_coordinate, self.y_coordinate)
