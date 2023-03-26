from turtle import Turtle
import random

DISTANCE = 10
START_DIRECTION = 180


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("white")
        # self.speed("fastest")
        self.setheading(random.randint(0, 360))
        self.move()

    def change_direction(self):
        new_direction = (self.heading() + 90) % 360
        self.setheading(new_direction)

    def move(self):
        self.forward(DISTANCE)
