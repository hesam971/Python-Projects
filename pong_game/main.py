from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

game_over = False
screen = Screen()

screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pang_game")

r_paddle = Paddle((370, 0))
r_score = Score(100, 250)
l_paddle = Paddle((-370, 0))
l_score = Score(-100, 250)

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "Left")
screen.onkey(l_paddle.down, "Right")

ball = Ball()

screen.listen()

while not game_over:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if (ball.xcor() > 280 and ball.distance(r_paddle) < 20) or (ball.xcor() < -280 and ball.distance(l_paddle) < 20):
        ball.x_bounce()
    if ball.xcor() > 390:
        ball.rest_position()
        l_score.change_score()
    if ball.xcor() < -390:
        ball.rest_position()
        r_score.change_score()

screen.exitonclick()
