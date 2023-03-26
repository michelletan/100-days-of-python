from turtle import Turtle
TEXT_ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        self.player_score = 0
        self.computer_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=x, y=y)
        self.update_scoreboard()

    def increase_score(self, isPlayer):
        if isPlayer:
            self.player_score += 1
        else:
            self.computer_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{str(self.player_score)}    {str(self.computer_score)}", False, align=TEXT_ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        winner = "Player" if self.player_score > self.computer_score else "Computer"
        self.write(f"GAME OVER \n {winner} wins!", False, align=TEXT_ALIGNMENT,
                   font=FONT)
