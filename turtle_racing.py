from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.setup(width=500, height=400)
my_bet = screen.textinput(title="Make Your Bet", prompt="Enter a Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-80, -40, 0, 40, 80, 120]
all_turtles = []
for index in range(6):
    king = Turtle("turtle")
    king.color(colors[index])
    king.penup()
    king.goto(x=-230, y=y_pos[index])
    all_turtles.append(king)

is_race_on = False
if my_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == my_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        turtle.forward(r.randint(0, 10))


screen.exitonclick()
