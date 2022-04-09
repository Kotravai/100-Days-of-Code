import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left_move, "Left")
screen.onkey(snake.right_move, "Right")

game_is_on = True
i = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.snake_reset()
        #game_is_on = False

    # detect collission with snake body.
    # loop through each segment

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.snake_reset()
            #game_is_on = False

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     if snake.head.distance(segment) < 10:
    #         score.game_over()
    #         game_is_on = False

screen.exitonclick()
