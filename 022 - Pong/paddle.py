from turtle import Turtle
from enum import Enum

MOVE_DISTANCE = 15


class Headings(Enum):
    EAST = 0
    SOUTH = 270
    WEST = 180
    NORTH = 90


class Paddle(Turtle):
    def __init__(self, start_x=0, start_y=0) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=3.0)
        self.color("white")
        self.setheading(Headings.NORTH.value)
        self.penup()
        self.goto(start_x, start_y)
        self.start_x = start_x
        self.start_y = start_y

    def move(self, heading):
        self.setheading(heading)
        self.forward(MOVE_DISTANCE)

    def up(self):
        self.move(Headings.NORTH.value)

    def down(self):
        self.move(Headings.SOUTH.value)
