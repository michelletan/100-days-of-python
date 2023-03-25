from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
COLLISION_OFFSET = 10
WALL_X = SCREEN_WIDTH/2 - COLLISION_OFFSET
WALL_Y = SCREEN_HEIGHT/2 - COLLISION_OFFSET

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake 2023")
screen.tracer(0)

snake = Snake()
food = Food(screen_bounds_x=WALL_X - COLLISION_OFFSET,
            screen_bounds_y=WALL_Y - COLLISION_OFFSET)
scoreboard = Scoreboard(x=0, y=SCREEN_HEIGHT/2 - 40)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > WALL_X or snake.head.xcor() < -WALL_X or snake.head.ycor() > WALL_Y or snake.head.ycor() < -WALL_Y:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < COLLISION_OFFSET:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
