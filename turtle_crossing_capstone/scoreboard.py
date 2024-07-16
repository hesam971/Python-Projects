from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.score()

    def score(self):
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-290, 270)
        self.write(f"level: {self.scores}", move=False, align='left', font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.clear()
        self.scores += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", move=False, align='center', font=('Arial', 22, 'normal'))
