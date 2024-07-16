from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
game_over = False
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.random_coordinate()
        scoreboard.each_refresh()
        snake.extend_segments()
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        snake.reset_snake()
        scoreboard.high_score()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset_snake()
            scoreboard.high_score()

screen.exitonclick()
