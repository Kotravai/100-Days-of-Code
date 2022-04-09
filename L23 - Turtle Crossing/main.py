import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        position = car.position()
        if player.distance(position) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()







screen.exitonclick()

# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     for i in range(0, 180):
#         if i % 6 == 0:
#             i = CarManager()
#             i.car_mover()