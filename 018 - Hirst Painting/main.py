import random
from color_data import color_data
import random
import turtle as t

ROWS = 10
COLS = 10
SIZE = 20
GAP = 50

pen = t.Turtle()
t.colormode(255)
pen.speed(0)
SCREEN_SIZE = t.screensize()


def random_color():
    return random.choice(color_data)


def draw_circle():
    pen.dot(SIZE, random_color())


def main():
    # Center the square
    SQUARE_WIDTH = COLS * GAP
    SQUARE_HEIGHT = ROWS * GAP
    start_x = -(SQUARE_WIDTH - GAP) / 2
    start_y = -(SQUARE_HEIGHT - GAP) / 2
    pen.up()

    curr_x = start_x
    curr_y = start_y
    for i in range(ROWS):
        for j in range(COLS):
            pen.goto(curr_x, curr_y)
            draw_circle()
            curr_y += GAP
        curr_y = start_y
        curr_x += GAP


main()
screen = t.Screen()
screen.exitonclick()
