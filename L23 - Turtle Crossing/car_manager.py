import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# POSITIONS = [-220, -190, -160, -130, -100, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210 ]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,7)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(1, 2, 0.5)
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("square")
#         self.penup()
#         self.setheading(270)
#         self.shapesize(2, 1, 0.5)
#         self.instances = 0
#
#     def car_generator(self):

            # random_chance = random.randint(1, 7)
            # if random_chance == 1:
#         colour = random.choice(COLORS)
#         self.hideturtle()
#         self.color(colour)
#         self.goto(280, random.randint(-250, 250))
#         self.setheading(270)
#         self.showturtle()
#
#     def car_mover(self):
#         # if self.instances % 6 == 0:
#         #     self.car_generator()
#         #     self.instances+=1
#         if self.xcor() >= - 280:
#             new_x = self.xcor() - STARTING_MOVE_DISTANCE
#             self.goto(new_x, self.ycor())
#             self.speed("slow")
#         else:
#             self.hideturtle()



