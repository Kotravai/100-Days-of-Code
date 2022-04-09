#Challenge 1 - Etch a Sketch app

from turtle import Turtle, Screen
#
# gon = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     gon.forward(10)
#
#
# def move_back():
#     gon.back(10)
#
#
# def turn_right():
#     gon.right(10)
#
#
# def turn_left():
#     gon.left(10)
#
#
# def clear():
#     gon.reset()
#
#
# screen.listen()
# screen.onkey(key= "w", fun = move_forwards)
# screen.onkey(key= "s", fun = move_back)
# screen.onkey(key= "a", fun = turn_left)
# screen.onkey(key= "d", fun = turn_right)
# screen.onkey(key= "c", fun = clear)
# screen.exitonclick()

#Challenge 2 - Turtle race
import random

is_race_on = False
color = ["red", "green", "blue", "yellow", "orange", "violet"]
y_coord = [-150,-75, 0, 50, 100, 150]
turtles = []

screen = Screen()
screen.setup(height = 500, width=400)
user_bet = screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a colr: ")

for turtle_index in range(0, 6):
    gon = Turtle("turtle")
    gon.color(color[turtle_index])
    gon.penup()
    gon.goto(-250, y_coord[turtle_index])
    turtles.append(gon)

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in turtles:
        rand_distance = random.randint(0, 10)
        turt.forward(rand_distance)
        if turt.xcor() > 230:
            winner = turt.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You won!. The {winner} turtle is the winner")
            else:
                print(f"You lose. The {winner} turtle is the winner")




screen.exitonclick()










