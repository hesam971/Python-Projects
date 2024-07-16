from turtle import Turtle

SEGMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_movement()
        self.head = self.segments[0]

    def snake_movement(self):
        """create snake body"""
        for segment in SEGMENT_POSITION:
            self.add_segments(segment)

    def add_segments(self, seg_position):
        turtle = Turtle()
        turtle.penup()
        turtle.color("white")
        turtle.shape("square")
        turtle.goto(seg_position)
        self.segments.append(turtle)

    def extend_segments(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        """move the snake"""
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)

        self.head.forward(DISTANCE)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.snake_movement()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
