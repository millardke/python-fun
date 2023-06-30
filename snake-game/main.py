from turtle import Screen
import time
from snake import Snake

# Game Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

game_is_on = True

snake = Snake()

# Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


# Run game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()





screen.exitonclick()