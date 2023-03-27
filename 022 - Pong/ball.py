from turtle import Turtle
import random

MAX_SPEED = 20
MAX_X = 15
MAX_Y = 10


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("white")
        self.randomise_direction()
        self.speed_x = random.choice([MAX_X, -MAX_X])

    def reset_position(self):
        self.goto(0, 0)
        self.randomise_direction()

    def randomise_direction(self):
        self.speed_y = random.randint(-MAX_Y, MAX_Y)

    def bounce_on_wall(self):
        self.speed_y = -self.speed_y

    def bounce_on_player(self):
        self.speed_x = -self.speed_x

    def move(self):
        pos = self.position()
        self.goto(pos[0] + self.speed_x, pos[1] + self.speed_y)
