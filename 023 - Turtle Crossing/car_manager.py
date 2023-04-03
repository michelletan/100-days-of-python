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

    def __init__(self, start_x: int, min_x: int, min_y: int, max_y: int, max_cars: int = 50):
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
        self.max_cars = max_cars
        self.cars = []
        self.visible_cars = []
        self.initialise_cars()

    def initialise_cars(self):
        for _ in range(self.max_cars):
            self.initialise_car()

    def initialise_car(self):
        """Creates a Turtle representing a car, sets a random color for the car."""
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=1.5, stretch_wid=0.8)
        car.hideturtle()
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.penup()
        self.cars.append(car)

    def add_car(self):
        """Makes a car visible on the screen, at a randomised starting y-position."""
        car: Turtle = random.choice(self.cars)
        self.cars.remove(car)
        self.visible_cars.append(car)
        car.goto(self.start_x, random.randint(self.min_y, self.max_y))
        car.showturtle()

    def move_cars(self):
        """Moves each car under CarManager's control by self.move_distance. 
        Makes cars that have gone beyond self.min_x invisible.
        """
        for car in self.visible_cars:
            car.forward(self.move_distance)
            if car.position()[0] < self.min_x - 20:
                car.hideturtle()
                self.visible_cars.remove(car)
                self.cars.append(car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
