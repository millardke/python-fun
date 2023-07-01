from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Game setup
game_running = True
player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(player_1.go_up, "w")
screen.onkey(player_1.go_down, "s")
screen.onkey(player_2.go_up, "Up")
screen.onkey(player_2.go_down, "Down")

while(game_running):
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect ball collision with walls
    if abs(ball.ycor()) > 280:
        ball.bounce('y')

    # Detect ball collision with paddles
    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.bounce('x')

    # Detect player scores
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.p1_scores()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.p2_scores()




screen.exitonclick()
