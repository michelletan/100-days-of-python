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
LEFT_PADDLE_POSITION = -WALL_X + PADDLE_OFFSET
RIGHT_PADDLE_POSITION = WALL_X - PADDLE_OFFSET - COLLISION_OFFSET

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong 2023")
screen.tracer(0)

left_player = Paddle(start_x=LEFT_PADDLE_POSITION)
right_player = Paddle(start_x=RIGHT_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard(x=0, y=SCREEN_HEIGHT/2 - 40)

screen.listen()
screen.onkeypress(left_player.up, "q")
screen.onkeypress(left_player.down, "a")
screen.onkeypress(right_player.up, "Up")
screen.onkeypress(right_player.down, "Down")


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
ball_speed = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move()

    # Detect collision with left_player and ball
    if ball.distance(left_player) < 20 and ball.xcor() < LEFT_PADDLE_POSITION + COLLISION_OFFSET:
        ball.bounce_on_player()
        ball_speed *= 0.9

    # Detect collision with right_player and ball
    if ball.distance(right_player) < 20 and ball.xcor() > RIGHT_PADDLE_POSITION - COLLISION_OFFSET:
        ball.bounce_on_player()
        ball_speed *= 0.9

    # Detect collision with walls behind players
    if ball.xcor() > WALL_X:
        scoreboard.increase_score(player="left")
        ball.reset_position()
        ball_speed = 0.1

    if ball.xcor() < -WALL_X:
        scoreboard.increase_score(player="right")
        ball.reset_position()
        ball_speed = 0.1

    # Detect collision with top and bottom walls
    if ball.ycor() > WALL_Y or ball.ycor() < -WALL_Y:
        ball.bounce_on_wall()

    if scoreboard.has_player_won():
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
