from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Creates and manages the scoreboard for the game."""

    def __init__(self, position=(0, 0)):
        super().__init__(shape="classic")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.level = 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", False, align="left",
                   font=FONT)

    def reset_scoreboard(self):
        self.level = 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
