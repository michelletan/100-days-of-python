from turtle import Turtle, Screen
import random

WIDTH = 500.0
HEIGHT = 400.0
SPACING = 30
TURTLE_SIZE = 1
TURTLE_OFFSET = 10

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

user_bet = screen.textinput(title="Make your bet",
                            prompt=f"Which turtle will win the race? Enter {'/'.join(COLORS)}: ")


def create_turtle(color, position):
    t = Turtle(shape="turtle")
    t.shapesize(TURTLE_SIZE)
    t.color(color)
    t.up()
    t.goto(x=position[0], y=position[1])
    return t


def race():
    start_x = -WIDTH/2
    y = (len(COLORS) * SPACING)/2
    turtles = []

    # Create turtles and line them up at the start
    for c in COLORS:
        t = create_turtle(color=c, position=(start_x + TURTLE_OFFSET, y))
        turtles.append(t)
        y -= SPACING

    while True:
        for i, t in enumerate(turtles):
            t.forward(random.randint(1, 10))
            if t.position()[0] >= (WIDTH / 2) - TURTLE_OFFSET * 2:
                winner = COLORS[i]
                print(f"{winner.capitalize()} has won the race!")
                if user_bet == winner:
                    print("Congrats! You've won your bet.")
                else:
                    print("Sorry, your bet didn't win.")
                return


race()
screen.exitonclick()
