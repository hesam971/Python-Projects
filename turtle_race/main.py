from turtle import Turtle, Screen
import random

screen = Screen()


""" Etch - A - Sketch """
""" 
def f():
    tim.fd(50)

def s():
    tim.backward(30)

def a():
   tim.setheading(tim.heading() - 10)

def d():
   tim.setheading(tim.heading() + 10)

def c():
    tim.reset()

screen.onkey(f, "w")
screen.onkey(s, "s")
screen.onkey(a, "a")
screen.onkey(d, "d")
screen.onkey(c, "c")
screen.listen()
screen.exitonclick()  """



"""
print(screen.window_width())
tim.shape("turtle")
tim.color("red")
tim.penup()
tim.setheading(15)
tim.backward(screen.window_width()/2)
tim.right(15)

tim.forward(screen.window_width() - 50)
#tommy.setpos(120,45)

screen.listen()
screen.exitonclick()
"""

"""race for turtles"""
screen.setup(width=500, height=600)
user_choice = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color: ")
y_position = -250
is_over = False
color_collection = ["red", "blue", "orange", "yellow", "gray", "green"]
turtle_collections = []
for color in color_collection:
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.setposition(-240, y_position)
    y_position += 100
    turtle_collections.append(new_turtle)

while not is_over:
    for turtle in turtle_collections:
        turtle.fd(random.choice([10, 20, 30, 40]))
        if 205 < turtle.xcor():
            is_over = True
            if user_choice == turtle.pencolor():
                print("you win the race")
            else:
                print("your guess wa wrong and you lose")


screen.exitonclick()



