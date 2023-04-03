import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Creates cars and moves them.

    Makes cars invisible once cars have moved beyond min_x value.
    Clears and resets cars at the end of the level.

    Attributes:
        start_x: Starting x-position for all cars.
        min_x: Minimum x-position for cars to remain visible.
        min_y: Minimum y-position for cars to be spawned in.
        max_y: Maximum y-position for cars to be spawned in.
        cars: List containing all visible cars.
    """

    def __init__(self, start_x: int, min_x: int, min_y: int, max_y: int):
        """Sets starting variables needed for CarManager.

        Args:
            start_x: Starting x-position for all cars.
            min_x: Minimum x-position for cars to remain visible.
            min_y: Minimum y-position for cars to be spawned in.
            max_y: Maximum y-position for cars to be spawned in.
        """
        self.start_x = start_x
        self.min_x = min_x
        self.min_y = min_y
        self.max_y = max_y
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def add_car(self):
        """Creates a Turtle representing a car, sets a random color for the car."""
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=1.5, stretch_wid=0.8)
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.penup()
        car.goto(self.start_x, random.randint(self.min_y, self.max_y))
        self.cars.append(car)

    def move_cars(self):
        """Moves each car under CarManager's control by self.move_distance. 
        Removes cars that have gone beyond self.min_x.
        """
        for car in self.cars:
            car.forward(self.move_distance)
            if car.position()[0] < self.min_x - 20:
                car.hideturtle()
                self.cars.remove(car)

    def reset(self):
        self.cars.clear()
