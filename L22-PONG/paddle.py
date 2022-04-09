from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position)
        self.resizemode('user')
        self.shapesize(6, 0.5, 2)

    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
