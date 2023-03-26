from turtle import Screen
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
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with p1 and ball
    for block in p1.blocks:
        if ball.distance(block) < COLLISION_OFFSET:
            ball.change_direction()
            scoreboard.increase_score(isPlayer=True)

    # Detect collision with p2 and ball
    for block in p2.blocks:
        if ball.distance(block) < COLLISION_OFFSET:
            ball.change_direction()
            scoreboard.increase_score(isPlayer=False)

    # Detect collision with walls behind players
    if ball.xcor() > WALL_X or ball.xcor() < -WALL_X:
        game_on = False
        scoreboard.game_over()

    # Detect collision with top and bottom walls
    if ball.ycor() > WALL_Y or ball.ycor() < -WALL_Y:
        ball.change_direction()

screen.exitonclick()
