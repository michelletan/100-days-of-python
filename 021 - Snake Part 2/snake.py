from turtle import Turtle
from enum import Enum


class Headings(Enum):
    EAST = 0
    SOUTH = 270
    WEST = 180
    NORTH = 90


class Snake:
    def __init__(self, length=3, block_size=20, start_x=0, start_y=0) -> None:
        self.length = length
        self.block_size = block_size
        self.start_x = start_x
        self.start_y = start_y
        self.create_snake()

    def create_snake(self):
        self.blocks = []
        for i in range(self.length):
            self.create_block(
                pos_x=(self.start_x - i * 20), pos_y=self.start_y)
        self.head = self.blocks[0]

    def create_block(self, pos_x, pos_y):
        t = Turtle("square")
        t.color("white")
        t.up()
        t.goto(x=pos_x, y=pos_y)
        self.blocks.append(t)

    def extend(self):
        self.create_block(self.blocks[-1].xcor(), self.blocks[-1].ycor())

    def move(self):
        for i in range(len(self.blocks) - 1, 0, -1):
            next_pos_x = self.blocks[i - 1].xcor()
            next_pos_y = self.blocks[i - 1].ycor()
            self.blocks[i].goto(x=next_pos_x, y=next_pos_y)
        self.head.forward(self.block_size)

    def turn(self, direction):
        self.head.setheading(direction)

    def up(self):
        if self.head.heading() != Headings.SOUTH.value:
            self.turn(Headings.NORTH.value)

    def down(self):
        if self.head.heading() != Headings.NORTH.value:
            self.turn(Headings.SOUTH.value)

    def left(self):
        if self.head.heading() != Headings.EAST.value:
            self.turn(Headings.WEST.value)

    def right(self):
        if self.head.heading() != Headings.WEST.value:
            self.turn(Headings.EAST.value)
