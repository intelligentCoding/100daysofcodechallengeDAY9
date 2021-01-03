from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard1 = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    #  detect when right paddle is missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard1.l_point()

    # Detect when left paddle is missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard1.r_point()


screen.exitonclick()


