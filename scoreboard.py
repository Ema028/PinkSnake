from turtle import Turtle

font = ("Verdana", 20, "normal")
align = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x = 0, y = 270)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"score = {self.score}", font = font, align = align)

    def point(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font = font, align = align)
