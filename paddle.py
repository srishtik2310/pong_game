from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cordinate, y_cordinate):
        super().__init__()
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(x = self.x_cordinate, y = self.y_cordinate)

    def move_paddle_up(self):
        if self.ycor() < 240:
            self.goto(x = self.xcor(), y = self.ycor() + 20)

    def move_paddle_down(self):
        if self.ycor() > -220:
            self.goto(x = self.xcor(), y = self.ycor() - 20)


