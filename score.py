from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_points = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score_points}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -25)
        self.write("Press R to try again.", align=ALIGNMENT, font=FONT)

    def change_score(self):
        self.score_points += 1
        self.clear()
        self.update_scoreboard()
