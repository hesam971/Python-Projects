from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

i = 0
number = 3
while i < 8:
    for _ in range(number):
        tim.forward(90)
        tim.right(360 / number)
    i += 1
    number += 1
########### Challenge 3 - Draw Shapes ########


screen.exitonclick()

""" import turtle as t

tim = t.Turtle()
i = 0
number = 3
while  i < 8:
  for _ in range(number):
    t.forward(90)
    t.right(360/number)
  i += 1
  number += 1
########### Challenge 3 - Draw Shapes ######## """