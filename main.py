from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
move_speed = 0.1
screen = Screen()
screen.tracer(0)
is_game_on = True

screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")
screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")

while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 325 or ball.distance(l_paddle) < 60 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()




screen.exitonclick()
