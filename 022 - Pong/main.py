from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
COLLISION_OFFSET = 10
PADDLE_OFFSET = 20
WALL_X = SCREEN_WIDTH/2 - COLLISION_OFFSET
WALL_Y = SCREEN_HEIGHT/2 - COLLISION_OFFSET

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong 2023")
screen.tracer(0)

p1 = Paddle(start_x=-WALL_X + PADDLE_OFFSET)
p2 = Paddle(start_x=WALL_X - PADDLE_OFFSET - COLLISION_OFFSET)
ball = Ball()
scoreboard = Scoreboard(x=0, y=SCREEN_HEIGHT/2 - 40)

screen.listen()
screen.onkeypress(p1.up, "q")
screen.onkeypress(p1.down, "a")
screen.onkeypress(p2.up, "Up")
screen.onkeypress(p2.down, "Down")


def draw_board():
    pen = Turtle()
    pen.color("gray")
    pen.pensize(3)
    pen.hideturtle()
    pos_y = -SCREEN_HEIGHT/2
    pen_down = True

    while pos_y <= SCREEN_HEIGHT/2:
        if pen_down == False:
            pen.pendown()
        else:
            pen.penup()
        pen.goto(0, pos_y)
        pos_y += 10
        pen_down = not pen_down


draw_board()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with p1 and ball
    p1_scored = False
    for block in p1.blocks:
        if ball.distance(block) < COLLISION_OFFSET:
            p1_scored = True
    if p1_scored:
        ball.bounce_on_player()

    # Detect collision with p2 and ball
    p2_scored = False
    for block in p2.blocks:
        if ball.distance(block) < COLLISION_OFFSET:
            p2_scored = True
    if p2_scored:
        ball.bounce_on_player()

    # Detect collision with walls behind players
    if ball.xcor() > WALL_X:
        scoreboard.increase_score(isPlayer=True)
        ball.reset_position()

    if ball.xcor() < -WALL_X:
        scoreboard.increase_score(isPlayer=False)
        ball.reset_position()

    # Detect collision with top and bottom walls
    if ball.ycor() > WALL_Y or ball.ycor() < -WALL_Y:
        ball.bounce_on_wall()

screen.exitonclick()
