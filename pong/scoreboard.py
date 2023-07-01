from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.p2_score, align=ALIGN, font=FONT)

    def p1_scores(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_scores(self):
        self.p2_score += 1
        self.update_scoreboard()