from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_print()

    def score_print(self):
        self.goto(-100, 250)
        self.write(self.l_score, align = "center",  font = ("Courier", 50, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align = "center", font = ("Courier", 50, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.score_print()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.score_print()







