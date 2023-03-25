from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen_bounds_x, screen_bounds_y) -> None:
        super().__init__()
        self.screen_bounds_x = screen_bounds_x
        self.screen_bounds_y = screen_bounds_y
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-self.screen_bounds_x, self.screen_bounds_x)
        random_y = random.randint(-self.screen_bounds_y, self.screen_bounds_y)
        self.goto(random_x, random_y)
