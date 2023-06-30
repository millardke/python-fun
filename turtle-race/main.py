from turtle import Turtle, Screen
import random

race_started = False

screen = Screen()
screen.setup(500, 400)

user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [ -75, -45, -15, 15, 45, 75 ]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-240, y_positions[turtle_index])
    turtles.append(new_turtle)

if user_guess:
    race_started = True

while race_started:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 250 - 20:
            winning_color = turtle.pencolor()

            if winning_color == user_guess:
                print('You won!')
            else:
                print('You lost')

            race_started = False

screen.exitonclick()