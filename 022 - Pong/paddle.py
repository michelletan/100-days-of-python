from turtle import Turtle
from enum import Enum


class Headings(Enum):
    EAST = 0
    SOUTH = 270
    WEST = 180
    NORTH = 90


class Paddle:
    def __init__(self, length=3, block_size=20, start_x=0, start_y=0) -> None:
        self.length = length
        self.block_size = block_size
        self.start_x = start_x
        self.start_y = start_y
        self.create_paddle()

    def create_paddle(self):
        self.blocks = []
        for i in range(self.length):
            self.create_block(
                pos_x=self.start_x, pos_y=(self.start_y - i * 20))
        self.head = self.blocks[0]

    def create_block(self, pos_x, pos_y):
        t = Turtle("square")
        t.color("white")
        t.up()
        t.goto(x=pos_x, y=pos_y)
        self.blocks.append(t)

    def move(self, heading):
        for i in self.blocks:
            i.setheading(heading)
            i.forward(self.block_size)

    def up(self):
        self.move(Headings.NORTH.value)

    def down(self):
        self.move(Headings.SOUTH.value)
