import random
import time
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_CARS = 30
CAR_FREQUENCY = 10  # The lower this num, the more cars will spawn.

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
car_manager = CarManager(start_x=SCREEN_WIDTH/2, min_x=-SCREEN_WIDTH/2,
                         min_y=-SCREEN_HEIGHT/2, max_y=SCREEN_HEIGHT/2)
scoreboard = Scoreboard(position=(-SCREEN_WIDTH/2 + 20, SCREEN_HEIGHT/2 - 40))

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    # Spawn cars based on MAX_CARS and CAR_FREQUENCY
    if len(car_manager.cars) < MAX_CARS and random.randint(1, CAR_FREQUENCY) == 1:
        car_manager.add_car()
    time.sleep(0.1)
    car_manager.move_cars()
    screen.update()
