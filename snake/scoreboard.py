from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        # self.max_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        with open("high_score.txt") as score:
            read_score = int(score.read())
            self.max_score = read_score
        self.new_turtle_score()

    def new_turtle_score(self):
        self.goto(0, 230)
        self.write(f"score: {self.current_score}, high score: {self.max_score}", True, align="center",
                   font=('Arial', 18, 'normal'))

    def each_refresh(self):
        self.clear()
        self.current_score += 1
        self.new_turtle_score()

    def high_score(self):
        if self.current_score > self.max_score:
            self.max_score = self.current_score
            with open("high_score.txt", mode="w") as score:
                score.write(str(self.max_score))
        self.clear()
        self.current_score = 0
        self.new_turtle_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=('Arial', 22, 'normal'))
