from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_points = 0
        self.color("white")
        with open("data_score.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_points} - High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.reset()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -25)
        self.write("Press R to try again.", align=ALIGNMENT, font=FONT)
        
    def change_score(self):
        self.score_points += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_points > self.high_score:
            self.high_score = self.score_points
            with open("data_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score_points = 0
        self.update_scoreboard()
