from turtle import Turtle
TEXT_ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
WINNING_SCORE = 10


class Scoreboard(Turtle):
    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        self.left_player_score = 0
        self.right_player_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=x, y=y)
        self.update_scoreboard()

    def increase_score(self, player):
        if player == "left":
            self.left_player_score += 1
        elif player == "right":
            self.right_player_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{str(self.left_player_score)}       {str(self.right_player_score)}", False, align=TEXT_ALIGNMENT,
                   font=FONT)

    def has_player_won(self):
        return self.left_player_score >= WINNING_SCORE or self.right_player_score >= WINNING_SCORE

    def game_over(self):
        self.goto(0, 0)
        if self.left_player_score == self.right_player_score:
            self.write(f"GAME OVER \n It's a draw!", False, align=TEXT_ALIGNMENT,
                       font=FONT)
        else:
            winner = "Left" if self.left_player_score > self.right_player_score else "Right"
            self.write(f"GAME OVER \n {winner} wins!", False, align=TEXT_ALIGNMENT,
                       font=FONT)
