# # import csv
# # with open("weather_data.csv") as file:
# #     open_file = csv.reader(file)
# #     temp = []
# #     for names in open_file:
# #         if names[1] != "temp":
# #             temp.append(int(names[1]))
# #             print(temp)
#
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# information_gray = data[data["Primary Fur Color"] == "Gray"]
# information_Cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
# information_black = data[data["Primary Fur Color"] == "Black"]
# print(len(information_gray["Primary Fur Color"]))
# print(len(information_Cinnamon["Primary Fur Color"]))
# print(len(information_black["Primary Fur Color"]))
# all_information = {
#     "four colors": ["Gray", "Cinnamon", "Black"],
#     "count":
#         [
#             len(information_gray["Primary Fur Color"]),
#             len(information_Cinnamon["Primary Fur Color"]),
#             len(information_black["Primary Fur Color"])
#         ]
# }
#
# new_file = pandas.DataFrame(all_information)
# new_file.to_csv("new_information.csv")
# # number = 0
# # if data[data["Primary Fur Color"] == "Gray"]:
# #     number += 1
# #
# # print(number)
# #
# # temp_list = data["temp"].max()
# # day_condition = data[data["day"] == "Monday"]
# # f_temp = (day_condition.temp * 9 / 5) + 32

import pandas
from turtle import Screen, Turtle

read_data = pandas.read_csv("50_states.csv")
screen = Screen()
game_end = False
print(read_data.state.tolist())
"""create the new turtle"""
def new_one(x_coordinate, y_coordinate, state_name):
    turtle = Turtle()
    turtle.penup()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.hideturtle()
    turtle.speed("fast")
    turtle.write(f"{state_name}", True, align="center", font=('Arial', 9, 'normal'))


screen.setup(width=730, height=490)
screen.bgpic("blank_states_img.gif")
count_of_guess = 0

while not game_end:
    answer = screen.textinput(f"{count_of_guess}/{len(read_data.state)} State Correct", "What is another state name? ").title()
    my_answer = read_data[read_data.state == f"{answer}"]
    """end of the game when user guess wrong"""
    if my_answer.empty:
        print("by")
        game_end = True
    else:
        new_one(int(my_answer.x), int(my_answer.y), answer)
        count_of_guess += 1
        """end of the game when user guess all of them"""
    if count_of_guess == len(read_data.state):
        print("you won")

screen.listen()
screen.exitonclick()
