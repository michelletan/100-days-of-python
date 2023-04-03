import random
import time
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_CARS = 50
CAR_FREQUENCY = 5  # The lower this num, the more cars will spawn.

END_POINT = SCREEN_HEIGHT/2

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager(start_x=SCREEN_WIDTH/2, min_x=-SCREEN_WIDTH/2,
                         min_y=-SCREEN_HEIGHT/2, max_y=SCREEN_HEIGHT/2, max_cars=MAX_CARS)
scoreboard = Scoreboard(position=(-SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 - 40))

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    # Check if player has touched any cars
    for car in car_manager.visible_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

    # Check if player has reached the end
    if player.ycor() >= END_POINT:
        scoreboard.increase_level()
        player.reset_position()
        car_manager.increase_speed()

    # Spawn cars based on MAX_CARS and CAR_FREQUENCY
    if random.randint(1, CAR_FREQUENCY) == 1:
        car_manager.add_car()

    time.sleep(0.1)
    car_manager.move_cars()
    screen.update()

screen.exitonclick()
