import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)


r_paddle = Paddle((400, 0))
l_paddle = Paddle((-400, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision with wall
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.bounce_y()
    # Collision with paddle
    if (r_paddle.distance(ball.pos()) < 60 and ball.xcor() >= 380) or (l_paddle.distance(ball.pos()) < 60 and ball.xcor() <= -380):
        ball.bounce_x()

    # ball miss - right
    if ball.xcor() >= 400:
        ball.reset_position()
        scoreboard.l_point()

    # ball miss - left
    if ball.xcor() <= -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()



# ball.move()
#     if r_paddle.distance(ball.pos()) < 60 or l_paddle.distance(ball.pos()) < 60:
#         print ("made contact")
#         ball.collission()
#     elif ball.ycor() <= -280 or ball.ycor() >= 280:
#         ball.bounce()